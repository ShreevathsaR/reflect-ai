from fastapi import FastAPI
from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

HF_TOKEN=os.getenv("HUGGING_FACE_TOKEN")
API_URL=os.getenv("API_URL")

prompt = (
    """The user has the personality type INFJ. They are feeling anxious today,
    and their journal sentiment is negative. The journal discusses topics like 
    career, stress, and time management. Based on this information, generate a reflective journal prompt."""
)

HEADER={"Authorization":f"Bearer {HF_TOKEN}"}

app = FastAPI()

@app.get('/')
def welcome():
    return ({"message":f"Welcome,{HF_TOKEN}"})

@app.get('/result')
async def result():

    headers = {"Authorization":f"Bearer {HF_TOKEN}"}

    prompt = (
    """The user has the personality type INFJ. They are feeling anxious today,
    and their journal sentiment is negative. The journal discusses topics like 
    career, stress, and time management. Based on this information, generate a reflective journal advice."""
    )

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, headers=headers, json={
            "inputs": prompt,
            "min-length":1000
            }) as response:

                if response.status == 200:
                    result = await response.json()
                    return {"result": result}
                else:
                    return {"API call failed": {await response.text()}}




