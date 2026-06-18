from settings import Settings


def test_settings_load_correctly():
    """Weryfikuje, czy klasa Settings poprawnie ładuje wartości z .env.test"""
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ML_API_Testing_Environment"
    assert settings.FAKE_API_KEY == "mock_secret_test_key_12345"
