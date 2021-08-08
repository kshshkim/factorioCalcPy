from fastapi import FastAPI
from FactorioCalcFastAPI.static_req_handle import *
from FactorioCalcFastAPI.calc_instance import Calculator
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from FactorioCalcFastAPI.data.icon_ref_dict import icon_ref_dict
from fastapi.responses import HTMLResponse
from FactorioCalcFastAPI.redis_handle import rdc
import pickle

from typing import Optional
import asyncio

app = FastAPI()

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
    if rdc.get(rand_id) is None:
        await create_new_instance(rand_id, conf)


async def create_new_instance(rand_id, conf):
    new_instance = Calculator(conf)
    pickled_instance = pickle.dumps(new_instance)
    rdc.set(rand_id, pickled_instance)


async def get_target(rand_id):
    if rdc.get(rand_id) is not None:
        pickled_instance = rdc.get(rand_id)
        unpickled_instance = pickle.loads(pickled_instance)
        target: Calculator = unpickled_instance
        return target


async def redis_overwrite(rand_id, instance):
    pickled_instance = pickle.dumps(instance)
    rdc.set(rand_id, pickled_instance)


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


@app.get("/visualize/{rand_id}", response_class=HTMLResponse)
async def diagram_out(rand_id: float):
    target = await get_target(rand_id=rand_id)
    diagram_html = await target.diagram_data_update()
    return diagram_html


@app.get("/calc/get_results/{rand_id}")
async def get_results(rand_id: float):
    if rdc.get(rand_id) is not None:
        target: Calculator = await get_target(rand_id)
        return target.results


@app.post("/calc")
async def calc_control(instruction: Instruction):
    await check_instance(instruction.rand_id, instruction.conf)
    target_instance: Calculator = await get_target(instruction.rand_id)
    if (target_instance.conf != instruction.conf) or (instruction.action.action_name == 'initialize'):
        target_instance = Calculator(instruction.conf)
    target_instance.parse_action(instruction.action)
    await target_instance.async_update_result()
    await redis_overwrite(rand_id=instruction.rand_id, instance=target_instance)
    to_return = target_instance.results

    return to_return
