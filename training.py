import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    """Ładuje i zwraca zbiór danych Iris."""
    return load_iris(as_frame=True)


def train_model(X, y):
    """Trenuje prosty model klasyfikacji i go zwraca."""
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model


def save_model(model, filename="iris_model.joblib"):
    """Zapisuje wytrenowany model do pliku za pomocą joblib."""
    joblib.dump(model, filename)
    print(f"Model zapisany pomyślnie jako {filename}")


if __name__ == "__main__":
    # Uruchomienie procesu trenowania
    iris = load_data()
    X = iris.data
    y = iris.target

    # Mapowanie nazw klas dla czytelności (0, 1, 2 -> setosa, versicolor, virginica)
    # Zapisujemy target_names w modelu, aby móc ich użyć podczas inferencji
    model = train_model(X, y)
    model.target_names = iris.target_names

    save_model(model)
