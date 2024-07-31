from fastapi import FastAPI

app = FastAPI()
'''
@app.post("/")
def read_root():
    return {"Hello World"}
'''
@app.get("/")
def read_item():
    return {"Hello"}


# In Terminal "uvicorn mian:app --reload "
# localhost8000