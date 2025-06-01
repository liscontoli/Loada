from fastapi import APIRouter, Depends
from schemas.load_schema import LoadRequest
from services.load_logic import calculate_load_info
from dependencies.auth import verify_token

router = APIRouter(prefix="/load", tags=["Load"])

@router.post("/calculate")
def calculate_load(data: LoadRequest, claims: dict = Depends(verify_token)):
    result = calculate_load_info(data)
    return result
