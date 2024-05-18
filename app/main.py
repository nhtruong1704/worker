import httpx
from fastapi import FastAPI, Form
from app.api.workers import workers
from app.api.db import metadata, database, engine
from app.api import models,db
import httpx
from fastapi import FastAPI, Depends, APIRouter, Request, Form ,HTTPException, Header
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from keycloak import KeycloakOpenID
from fastapi.requests import Request

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/workers/openapi.json", docs_url="/api/v1/workers/docs")


KEYCLOAK_URL = "http://keycloak:8080/"
KEYCLOAK_CLIENT_ID = "testClient"
KEYCLOAK_REALM = "testRealm"
KEYCLOAK_CLIENT_SECRET = "bR3HyNLilTz3onsBIMfF9Oy59cpWhyR4"

keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_URL,
                                 client_id=KEYCLOAK_CLIENT_ID,
                                 realm_name=KEYCLOAK_REALM,
                                 client_secret_key=KEYCLOAK_CLIENT_SECRET)


@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    try:
        token = keycloak_openid.token(grant_type=["password"],
                                      username=username,
                                      password=password)

        return token
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Не удалось получить токен")


def user_got_role(token):
    try:
        token_info = keycloak_openid.introspect(token)
        if "testRole" not in token_info["realm_access"]["roles"]:
            raise HTTPException(status_code=403, detail="Access denied")
        return token_info
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token or access denied")


@app.put("/startup/")
async def startup(token: str = Header()):
    if (user_got_role(token)):
        await database.connect()
    else:
        return "Wrong JWT Token"


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(workers, prefix='/api/v1/workers', tags=['workers'])