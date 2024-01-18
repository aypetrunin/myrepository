from enum import Enum
from pydantic import BaseModel


class ChatOperationsBase(BaseModel):
    class Config:
        from_attributes = True


class ChatOperationsAnswer(ChatOperationsBase):
    question: str
    answers: str


class ChatModel(Enum):
    GPT3 = 'gpt-3.5-turbo-1106'
    GPT4 = 'gpt-4-1106-preview'


class ChatOperationsModel(ChatOperationsBase):
    model: ChatModel = 'gpt-3.5-turbo-1106'
