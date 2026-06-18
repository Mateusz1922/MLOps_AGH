import joblib
import pandas as pd


def load_model(filename="iris_model.joblib"):
    """Ładuje model z pliku."""
    return joblib.load(filename)


def predict(model, input_data: dict) -> str:
    """Przyjmuje słownik z cechami, robi predykcję i zwraca nazwę gatunku."""
    # Konwertujemy słownik na DataFrame z jedną linijką,
    # dopasowując nazwy kolumn do tych użytych podczas trenowania
    df = pd.DataFrame(
        [
            {
                "sepal length (cm)": input_data["sepal_length"],
                "sepal width (cm)": input_data["sepal_width"],
                "petal length (cm)": input_data["petal_length"],
                "petal width (cm)": input_data["petal_width"],
            }
        ]
    )

    # Predykcja (zwraca indeks klasy, np. 0)
    prediction_idx = model.predict(df)[0]

    # Mapujemy indeks na tekstową nazwę (np. "setosa")
    return model.target_names[prediction_idx]
