from pydantic import BaseModel
from typing import List


class GeometryData(BaseModel):
    type: str
    coordinates: List[float]


class AggregationRequest(BaseModel):
    geometry: GeometryData
    field: str
    aggr: str
    r: int


class AggregationRequestPolyfill(BaseModel):
    geometry: GeometryData
    field: str
    aggr: str
