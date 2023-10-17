from pydantic import BaseModel


class GeometryData(BaseModel):
    type: str
    coordinates: list


class AggregationRequest(BaseModel):
    geometry: GeometryData
    field: str
    aggr: str
    r: int


class AggregationRequestPolyfill(BaseModel):
    geometry: GeometryData
    field: str
    aggr: str
