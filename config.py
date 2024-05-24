from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str
    EMAIL_USE_SSL: bool


settings = Settings(
    NAME='anime',
    USER='postgres',
    PASSWORD='asdf7505',
    HOST='localhost',
    PORT='5432',
    EMAIL_HOST='smtp.yandex.ru',
    EMAIL_PORT=465,
    EMAIL_HOST_USER='apinime@yandex.ru',
    EMAIL_HOST_PASSWORD='vqdyruoqetipnwih',
    EMAIL_USE_SSL=True
)

