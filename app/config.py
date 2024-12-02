class Settings:
    SECRET_KEY: str = 'secret_key'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(30)
    DATABASE_URL: str = 'mysql+pymysql://root@localhost/league'

settings = Settings()