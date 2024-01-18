from fastapi import FastAPI

from .chat_operations import router as chat_operations_router


def create_app():
    app = FastAPI(
        debug=True,
        docs_url='/docs',
        title='FastAPI Mongo Example',
        version='0.1.0',
        description='A simple example of using FastAPI with MongoDB'
    )
    app.include_router(chat_operations_router)

    return app
