from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import WorkOut, WorkIn
from app.api import db_manager

workers = APIRouter()

@workers.post('/', response_model=WorkOut, status_code=201)
async def create_work(payload: WorkIn):
    work_id = await db_manager.add_work(payload)

    response = {
        'id': work_id,
        **payload.dict()
    }

    return response


@workers.get('/', response_model=List[WorkOut])
async def get_workers():
    return await db_manager.get_all_work()


@workers.get('/{id}/', response_model=WorkOut)
async def get_work(id: int):
    company = await db_manager.get_work(id)
    if not company:
        raise HTTPException(status_code=404, detail="work not found")
    return company


@workers.delete('/{id}/', response_model=None)
async def delete_work(id: int):
    company = await db_manager.get_work(id)
    if not company:
        raise HTTPException(status_code=404, detail="work not found")
    return await db_manager.delete_work(id)



