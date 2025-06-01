import os
from decimal import Decimal
from models.history import save_history_entry
from utils.fuel_price import get_fuel_price_by_state
from utils.location_utils import get_state_from_coordinates
from utils.miles import get_deadhead_miles, get_load_miles
from utils.market_rate import get_mock_market_rate
from services.negotiation_ai import negotiate_load
from utils.type_utils import convert_floats_to_decimal

def calculate_load_costs(data: dict, user_id: str):
    try:
        # Validate required fields
        required_fields = [
            "current_lat", "current_lng", "pickup_location", "dropoff_location",
            "truck_mpg", "load_weight", "load_miles", "deadhead_miles",
            "load_type", "broker_offer"
        ]
        for field in required_fields:
            if field not in data:
                return {"error": f"'{field}' is missing from request."}

        # Extract and convert input
        current_lat = float(data["current_lat"])
        current_lng = float(data["current_lng"])
        pickup = data["pickup_location"]
        dropoff = data["dropoff_location"]
        mpg = float(data["truck_mpg"])
        weight = float(data["load_weight"])
        load_miles = float(data["load_miles"])
        deadhead_miles = float(data["deadhead_miles"])
        total_miles = round(load_miles + deadhead_miles, 2)
        load_type = data.get("load_type", "dry van")
        broker_offer = float(data["broker_offer"])
        previous_offers = data.get("previous_offers", [])

        # Step 1: Get state from coordinates
        state = get_state_from_coordinates(current_lat, current_lng)

        # Step 2: Get diesel price for state with fallback
        try:
            diesel_price = get_fuel_price_by_state(state)
        except Exception as e:
            print(f"Error fetching fuel price for state {state}: {e}")
            diesel_price = 4.5  # fallback mock value

        # Step 3: Calculate fuel cost
        fuel_cost = round((total_miles / mpg) * diesel_price, 2)

        # Step 4: Get market rate (mocked)
        market_rate = get_mock_market_rate(load_type, pickup, dropoff)

        # Step 5: AI negotiation logic
        ai = negotiate_load(
            pickup_location=pickup,
            dropoff_location=dropoff,
            load_type=load_type,
            weight=weight,
            distance=total_miles,
            broker_offer=broker_offer,
            previous_offers=previous_offers
        )

        # Step 6: Save load to history
        save_history_entry(
            user_id,
            convert_floats_to_decimal({
                "pickup": pickup,
                "dropoff": dropoff,
                "load_type": load_type,
                "weight": weight,
                "total_miles": total_miles,
                "fuel_cost": fuel_cost,
                "broker_offer": broker_offer,
                "market_rate": market_rate,
                "counter_offer": ai["suggested_counter_offer"]
            })
        )

        # Step 7: Return full response
        response = {
            "state": state,
            "diesel_price": diesel_price,
            "fuel_cost": fuel_cost,
            "total_miles": total_miles,
            "market_rate": market_rate,
            "analysis": ai["analysis"],
            "suggested_counter_offer": ai["suggested_counter_offer"],
            "ai_reply": ai["ai_reply"]
        }

        return convert_floats_to_decimal(response)

    except Exception as e:
        print("❌ Error in load logic:", e)
        return {"error": str(e)}