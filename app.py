from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint of the application."""
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def hello(name: str):
    """Hello endpoint of the application."""
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8050, reload=True)
