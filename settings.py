# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    # Dodajemy nowe pole na sekret z pliku secrets.yaml
    # Pydantic dopasuje je po nazwie wielkimi literami
    FAKE_API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        allowed_environments = {"dev", "test", "prod"}
        if value not in allowed_environments:
            raise ValueError(
                f"Invalid environment: '{value}'. Must be one of: {', '.join(allowed_environments)}"
            )

        return value
