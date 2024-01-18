from fastapi import APIRouter, Depends

from ..models.chat_operations import ChatOperations


router = APIRouter(
    prefix="/chat_operations",
    tags=["chat_operations"]
)


@router.get("/answer")
def get_answer(question: str):
    return question


@router.post("/model", description='Модель ChatGPT')
def set_model(model: str):
    return model


@router.post("/temterature", description='Температура ChatGPT')
def set_temperature(temperature: int):
    return temperature
