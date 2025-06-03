from fastapi import APIRouter, Depends, HTTPException
from models.truck_settings import save_truck_settings, get_truck_settings, update_truck_settings, TruckSettings
from schemas.truck_settings_schema import TruckSettingsRequest, TruckSettingsResponse
from dependencies.auth import get_current_user

router = APIRouter(
    prefix="/truck-settings",
    tags=["Truck Settings"]
)

@router.post("/", response_model=TruckSettingsResponse)
def create_settings(payload: TruckSettingsRequest, current_user: dict = Depends(get_current_user)):
    settings = TruckSettings(user_id=current_user["sub"], **payload.model_dump())
    return save_truck_settings(settings)

@router.get("/", response_model=TruckSettingsResponse)
def read_settings(current_user: dict = Depends(get_current_user)):
    result = get_truck_settings(current_user["sub"])
    if not result:
        raise HTTPException(status_code=404, detail="Truck settings not found")
    return result

@router.put("/", response_model=dict)
def update_settings(payload: TruckSettingsRequest, current_user: dict = Depends(get_current_user)):
    update_truck_settings(current_user["sub"], payload.model_dump())
    return {"message": "Truck settings updated successfully"}