from pydantic import BaseModel, Field


class RoomsPostRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=255, description="Nome da sala")
    location: str = Field(
        ..., min_length=3, max_length=255, description="Localização da sala"
    )
    capacity: int = Field(
        ..., gt=2, description="Capacidade mínima da sala (deve ser maior que 2)"
    )

    class Config:
        from_attributes = True
