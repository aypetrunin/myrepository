from fastapi import FastAPI
# from common.settings import settings


def create_app():
    app = FastAPI(
        debug=True,
        docs_url='/docs',
        title='FastAPI Mongo Example2',
        version='0.1.0',
        description='A simple example of using FastAPI with MongoDB'
    )

    return app
