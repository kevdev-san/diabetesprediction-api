from pydantic import BaseModel

#datos que se van a recibir para hacer la prediccion
class PatientData(BaseModel):
    age: int
    hypertension: int
    heart_disease: int
    bmi: float
    HbA1c_level: float


#datos que se van a enviar como respuesta de la prediccion
class PredictionResponse(BaseModel):
    prediction: int
    label: str
    probability: float