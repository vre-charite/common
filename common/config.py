from pydantic import BaseSettings, Extra
from typing import Dict, Set, List, Any
from functools import lru_cache


class Settings(BaseSettings):
    port: int = 5001
    host: str = "127.0.0.1"
    env: str = "test"
    namespace: str = ""
    
    api_modules: List[str] = ["common.api"]
    VAULT_SERVICE: str = "https://vault.vault:8200/v1/vre/app/config"
    VAULT_CRT: str = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"
    VAULT_TOKEN: str = "s.p97lqlxBZ61C6sx5aHAFB4Ya"
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        extra = Extra.allow

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                env_settings,
                init_settings,
                file_secret_settings,
            )
    

@lru_cache(1)
def get_settings():
    settings =  Settings()
    return settings

class ConfigClass(object):
    settings = get_settings()
    env = settings.env
    api_modules = settings.api_modules

    VAULT_SERVICE = settings.VAULT_SERVICE
    VAULT_CRT = settings.VAULT_CRT
    VAULT_TOKEN = settings.VAULT_TOKEN
