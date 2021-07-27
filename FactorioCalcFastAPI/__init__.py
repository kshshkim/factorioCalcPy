from fastapi import FastAPI
from FactorioCalcFastAPI.static_req_handle import *
from FactorioCalcFastAPI.calc_instance import Calculator
from pydantic import BaseModel
from typing import Optional
import asyncio

app = FastAPI()
app.instance_dict = {}


async def check_instance(rand_id, conf):
    if app.instance_dict.get(rand_id) is None:
        await create_new_instance(rand_id, conf)


async def create_new_instance(rand_id, conf):
    app.instance_dict[rand_id] = Calculator(conf)


@app.get("/")
async def root():
    return {"message": "Hello World"}


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

async def get_result_base(rand_id:float):
    target = app.instance_dict.get(rand_id)
    await target.async_update_result()
    return target.results

@app.get("/calc/get_results/{rand_id}")
async def get_result(rand_id: float):
    if rand_id in app.instance_dict.keys():
        return await get_result_base(rand_id=rand_id)

@app.post("/calc")
async def calc_control(instruction: Instruction):
    await check_instance(instruction.rand_id, instruction.conf)
    target_instance = app.instance_dict.get(instruction.rand_id)
    if instruction.action.action_name != 'initialize':
        target_instance.parse_action(instruction.action)
    else:
        await create_new_instance(instruction.rand_id, instruction.conf)

    to_return = await get_result_base(instruction.rand_id)

    return to_return
