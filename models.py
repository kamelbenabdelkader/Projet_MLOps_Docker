
from typing import Optional, Union
from pydantic import BaseModel

class Prediction(BaseModel):
    id: Optional[int]
    prediction : Optional[str]
    probability : Union[float, None]
