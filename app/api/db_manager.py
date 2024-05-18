from app.api.models import WorkIn, WorkOut
from app.api.db import workers, database


async def add_work(payload: WorkIn):
    query = workers.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_work():
    query = workers.select()
    return await database.fetch_all(query=query)


async def get_work(id):
    query = workers.select().where(workers.c.id == id)
    return await database.fetch_one(query=query)


async def delete_work(id: int):
    query = workers.delete().where(workers.c.id == id)
    return await database.execute(query=query)

