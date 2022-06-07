import uvicorn
from fastapi import FastAPI

from api import price

app = FastAPI(
    title="Median Price",
    description="Median price form 5 api",
    version="1.0",
    docs_url="/api/docs"
)

app.include_router(
    price.router,
    prefix="/api",
    tags=["price"],
    responses={404: {"message": "Not Found"}}
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000)