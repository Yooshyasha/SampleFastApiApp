from tortoise import Tortoise
from fastapi import FastAPI

async def lifespan(app: FastAPI):
    await Tortoise.init(
        db_url='postgres://server:qwerty@localhost:5432/db',
        modules={'models': ['samplefastapiapp.src.database.models']}
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()