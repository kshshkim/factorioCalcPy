from fastapi import FastAPI
from FactorioCalcFastAPI.static_req_handle import *
from FactorioCalcFastAPI.calc_instance import Calculator
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from FactorioCalcFastAPI.data.icon_ref_dict import icon_ref_dict
from fastapi.responses import HTMLResponse

from typing import Optional
import asyncio

app = FastAPI()
app.instance_dict = {}

origins = [
    # 개발 편의를 위함. 배포시 수정 필요
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def check_instance(rand_id, conf):
    if app.instance_dict.get(rand_id) is None:
        await create_new_instance(rand_id, conf)


async def create_new_instance(rand_id, conf):
    app.instance_dict[rand_id] = Calculator(conf)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/icon_url/{name}")
async def icon_url(name: str):
    return "https://cdn.privatelaw.net/" + icon_ref_dict.get(name)


@app.get("/recipe_list")
async def recipe_list():
    results = get_recipe_list()
    return results


@app.get("/recipe/{recipe_name}")
async def recipe_spec(recipe_name: str):
    results = get_recipe_spec(recipe_name=recipe_name)
    return results


@app.get("/machine/{machine_name}")
async def machine_spec(machine_name: str):
    results = await get_machine_spec(machine_name=machine_name)
    return results


class Conf(BaseModel):
    recipe_name: str
    amount: float
    mining_research_modifier: float


class Action(BaseModel):
    action_name: str
    action_detail: dict


class Instruction(BaseModel):
    rand_id: float
    conf: Conf
    action: Action


async def get_result_base(rand_id: float):
    target = app.instance_dict.get(rand_id)
    await target.async_update_result()
    return target.results


@app.get("/visualize/{rand_id}", response_class=HTMLResponse)
async def diagram_out(rand_id: float):
    target: Calculator = app.instance_dict.get(rand_id)
    diagram_data: dict = target.diagram_data_out()
    from FactorioCalcBase.dependency_diagram import DependencyDiagram
    dd = DependencyDiagram(conf=target.conf, diagram_data=diagram_data)
    return dd.get_html()


@app.get("/calc/get_results/{rand_id}")
async def get_result(rand_id: float):
    if rand_id in app.instance_dict.keys():
        to_return = await get_result_base(rand_id=rand_id)
        return to_return


@app.post("/calc")
async def calc_control(instruction: Instruction):
    await check_instance(instruction.rand_id, instruction.conf)
    target_instance: Calculator = app.instance_dict.get(instruction.rand_id)
    if (target_instance.conf != instruction.conf) or (instruction.action.action_name == 'initialize'):
        await create_new_instance(instruction.rand_id, instruction.conf)

    target_instance.parse_action(instruction.action)
    to_return = await get_result_base(instruction.rand_id)

    return to_return
