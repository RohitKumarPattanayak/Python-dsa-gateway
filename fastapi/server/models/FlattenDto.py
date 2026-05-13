from pydantic import BaseModel
from typing import Optional,List,Dict,Any,Literal

# class DummyDto(BaseModel):
#     name: str
#     age: int

class FlattenDto(BaseModel):
    arr : Optional[List[Any]] = None
    obj : Optional[Dict[str, Any]] = None
    arrobj : Optional[Any] = None
    action : Literal[
        "flattenArr",
        "flattenObj",
        "flattenArrObj"
    ] = "flattenArr"
    # dummy : DummyDto


