from fastapi import FastAPI
import uvicorn
from models.FlattenDto import FlattenDto
from decorators.Logger import Logger
import asyncio

app = FastAPI()



@app.get("/")
@Logger
async def health_check():
    await asyncio.sleep(2)
    return {"health_check" : "success health check"}

@app.post("/flat")
@Logger
async def flattenFunc(payload: FlattenDto):
    if payload.action == 'flattenArr':
        def recurArr(arr,finalArr=[]):
            for i in arr:
                if isinstance(i,list):
                    recurArr(i,finalArr)
                else:
                    finalArr.append(i)
            return finalArr
        def recurArrGen(arr):
            for i in arr:
                if isinstance(i,list):
                    yield from recurArrGen(i)
                else:
                    yield i

        gen = recurArrGen(payload.arr)
        return list(gen)
    
    if payload.action == 'flattenObj':
        def recurObj(obj,newObj={},parent=''):
            for key, value in obj.items():
                key_name = f"{parent}->{key}" if parent else key
                if isinstance(value,dict):
                    recurObj(value,newObj,key_name)
                else:
                    newObj[key_name] = value
            return newObj    
        return recurObj(payload.obj)

    return "Action provide did not match"

# Profile with py-spy or pyinstrument to isolate CPU vs. I/O. Common fixes: use async DB drivers (asyncpg/motor), avoid blocking calls in async routes (use run_in_executor), add response caching, tune Uvicorn workers, or move heavy work to a task queue (Celery/ARQ).


if __name__ == '__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=3000,reload=True)
    


