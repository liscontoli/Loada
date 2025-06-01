from pydantic import BaseModel

class LoadRequest(BaseModel):
    current_location: str         # Example: "Miami, FL"
    pickup_location: str          # Example: "Orlando, FL"
    dropoff_location: str         # Example: "Atlanta, GA"
    truck_mpg: float              # Example: 6.5
    broker_offer: float           # Example: 1400.00
    load_type: str                # Example: "Dry Van"
