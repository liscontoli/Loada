import math
from utils.fuel_price import get_fuel_price_by_state
from services.negotiation_ai import negotiate_load
from utils.location_utils import get_state_from_coordinates
from fastapi import HTTPException
import logging

DEFAULT_DIESEL_PRICE = 4.15  # fallback price if fuel API fails

def calculate_load_costs(data: dict, user_id: str) -> dict:
    try:
        print(f"📦 Incoming payload: {data}")

        # Extract data
        current_lat = data["current_lat"]
        current_lng = data["current_lng"]
        pickup_location = data["pickup_location"]
        dropoff_location = data["dropoff_location"]
        truck_mpg = data["truck_mpg"]
        load_weight = data["load_weight"]
        load_miles = data["load_miles"]
        deadhead_miles = data["deadhead_miles"]
        load_type = data["load_type"]
        broker_offer = data["broker_offer"]
        previous_offers = data.get("previous_offers", [])

        # Total miles
        total_miles = load_miles + deadhead_miles

        # Get current state for fuel price lookup
        try:
            state_abbr = get_state_from_coordinates(current_lat, current_lng)
        except Exception as e:
            logging.warning(f"⚠️ Could not extract state from coordinates: {e}")
            state_abbr = "US"

        # Fetch fuel price
        diesel_price = get_fuel_price_by_state(state_abbr)
        if diesel_price == 0.0:
            diesel_price = DEFAULT_DIESEL_PRICE
            logging.warning("⚠️ Using default diesel price.")

        # Fuel cost calculation
        gallons_needed = total_miles / truck_mpg
        estimated_fuel_cost = round(gallons_needed * diesel_price, 2)

        # Offer per mile
        offer_per_mile = round(broker_offer / total_miles, 2)

        # Simulated market rate (TODO: plug in real API or model later)
        market_rate = 2.05  # USD/mile
        market_total = round(market_rate * total_miles, 2)

        # Profitability
        net_profit = broker_offer - estimated_fuel_cost
        is_profitable = net_profit > 0
        offer_comparison = "Above Market" if offer_per_mile > market_rate else "Below Market"

        # AI negotiation advice
        ai_result = negotiate_load(
            broker_offer=broker_offer,
            market_rate=market_rate,
            previous_offers=previous_offers
        )

        result = {
            "total_miles": total_miles,
            "estimated_fuel_cost": estimated_fuel_cost,
            "offer_per_mile": offer_per_mile,
            "market_rate_per_mile": market_rate,
            "market_total": market_total,
            "net_profit": net_profit,
            "is_profitable": is_profitable,
            "offer_comparison": offer_comparison,
            "ai_analysis": ai_result["analysis"],
            "suggested_counter_offer": ai_result["suggested_counter_offer"],
            "ai_reply": ai_result["ai_reply"]
        }

        print(f"✅ Load analysis result: {result}")
        return result

    except KeyError as e:
        logging.error(f"❌ Missing field in request: {e}")
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")

    except Exception as e:
        logging.error(f"❌ Error in load logic: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")