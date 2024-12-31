from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint of the application."""
    name = "Emmanuel"

    if name:
        return {"message": f"Hello {name}"}

    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8050)
