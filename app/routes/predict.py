from fastapi import APIRouter
from app.schemas.schemas import PatientData, PredictionResponse
from app.services.model_service import predict_diabetes

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(data: PatientData):
    return predict_diabetes(data)