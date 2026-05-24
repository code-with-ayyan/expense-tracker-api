from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    db_connection : str
    
setting = Settings()