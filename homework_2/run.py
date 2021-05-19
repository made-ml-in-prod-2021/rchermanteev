import uvicorn

from online_inference import app

if __name__ == "__main__":
    uvicorn.run(app)
