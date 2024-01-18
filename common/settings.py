from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 8000
    debug: bool = False
    # database_uri: str = 'sqlite:///./database.sqlite3'

    # jwt_secret: str
    # jwt_algorithm: str = 'HS256'
    # jwt_expiration: int = 60 * 60 * 24


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)

print(settings.debug)
