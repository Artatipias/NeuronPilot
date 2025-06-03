from fastapi import FastAPI
from .routers import auth

# Create an instance of the FastAPI class with metadata
app = FastAPI(
    title="NeuronPilot API",
    description="Backend API for the NeuronPilot Intelligent System.",
    version="0.1.0"
)

# Include the authentication router
app.include_router(auth.router)

# Define a GET endpoint at the root ("/") path
@app.get("/")
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Hello World - NeuronPilot Backend is Running!"}

# Define another GET endpoint at "/items/{item_id}"
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """
    Endpoint to read an item by its ID, with an optional query parameter 'q'.
    """
    return {"item_id": item_id, "q": q}
