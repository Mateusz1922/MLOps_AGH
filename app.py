from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
import inference

app = FastAPI()

# Ładujemy model jako zmienną globalną - wykona się raz przy starcie serwera
MODEL = inference.load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_iris(request: PredictRequest) -> PredictResponse:
    # Do funkcji predict przekazujemy słownik wyciągnięty z Pydantica za pomocą model_dump()
    input_data = request.model_dump()
    species_prediction = inference.predict(MODEL, input_data)

    return PredictResponse(prediction=species_prediction)
