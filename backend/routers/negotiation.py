from fastapi import APIRouter, Depends, HTTPException
from dependencies.auth import get_current_user
from services.negotiation_ai import negotiate_load
from schemas.negotiation_schema import NegotiationRequest, NegotiationResponse

router = APIRouter(
    prefix="/negotiation",
    tags=["Negotiation"]
)

@router.post("/negotiate", response_model=NegotiationResponse)
def negotiate(
    payload: NegotiationRequest,
    current_user: dict = Depends(get_current_user)
):
    try:
        result = negotiate_load(
            broker_offer=payload.broker_offer,
            market_rate=payload.market_rate,
            previous_offers=payload.previous_offers,
            countered_amount=payload.countered_amount
        )
        return result
    except Exception as e:
        print(f"❌ Negotiation failed: {e}")
        raise HTTPException(status_code=500, detail="Negotiation AI failed to respond.")