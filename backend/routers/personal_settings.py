from fastapi import APIRouter, Depends, HTTPException
from dependencies.auth import get_current_user
from schemas.personal_settings_schema import PersonalSettingsCreate, PersonalSettingsResponse
from models.personal_settings import create_or_update_personal_settings, get_personal_settings

router = APIRouter(prefix="/personal-settings", tags=["Personal Settings"])

@router.get("/", response_model=PersonalSettingsResponse)
def read_settings(current_user: dict = Depends(get_current_user)):
    user_id = current_user["sub"]
    item = get_personal_settings(user_id)
    if not item:
        raise HTTPException(status_code=404, detail="Settings not found")
    return item

@router.post("/", response_model=PersonalSettingsResponse)
def save_settings(
    data: PersonalSettingsCreate,
    current_user: dict = Depends(get_current_user)
):
    user_id = current_user["sub"]
    item = create_or_update_personal_settings(user_id, data.dict())
    return item