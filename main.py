from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from app.api.v1 import proxy, attack

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/", StaticFiles(directory="Web"), name="Web")
app.include_router(proxy.router, prefix="/v1/proxy", tags=["proxy"])
app.include_router(attack.router, prefix="/v1/attack", tags=["attack"])

if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=8000, reload=True)
