from models.history import get_history_by_user
from schemas.load_schema import LoadHistoryResponse
from fastapi import HTTPException
from typing import List

def get_user_history(user_id: str) -> List[LoadHistoryResponse]:
    try:
        records = get_history_by_user(user_id)
        response = [LoadHistoryResponse(**record) for record in records]
        return response
    except Exception as e:
        print(f"❌ Error fetching history for user {user_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve load history.")