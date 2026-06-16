import argparse
from dotenv import load_dotenv
from settings import Settings
from pathlib import Path
import os
import yaml


def export_envs(environment: str = "dev") -> None:
    # 1. Określamy ścieżkę do folderu 'config' w głównym katalogu projektu
    base_dir = Path(__file__).resolve().parent
    config_file_path = base_dir / "config" / f".env.{environment}"

    # 2. Sprawdzamy, czy plik dla danego środowiska w ogóle istnieje
    if not config_file_path.exists():
        raise FileNotFoundError(
            f"Konfiguracja dla środowiska '{environment}' nie istnieje: {config_file_path}"
        )

    # 3. Ładujemy zmienne z pliku do os.environ
    # override=True sprawia, że jeśli zmienna już istniała w systemie, zostanie nadpisana tą z pliku
    load_dotenv(dotenv_path=config_file_path, override=True)

    secrets_path = base_dir / "secrets.yaml"

    if secrets_path.exists():
        with open(secrets_path, "r") as f:
            # yaml.safe_load parsuje plik do zwykłego słownika Pythonowego (dict)
            secrets = yaml.safe_load(f)

        if secrets:
            for key, value in secrets.items():
                # SOPS dopisuje do pliku swoje metadane (zaczynające się od sops)
                # Ignorujemy je, interesują nas tylko Twoje sekrety
                if not key.startswith("sops"):
                    # os.environ przyjmuje tylko ciągi znaków (str)
                    os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("FAKE API KEY: ", settings.FAKE_API_KEY)
