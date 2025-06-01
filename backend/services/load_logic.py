import requests
from pydantic import BaseModel

# Google APIs
GOOGLE_MAPS_API_KEY = "GOOGLE_API_KEY"
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
DISTANCE_MATRIX_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

# EIA Fuel API
EIA_API_KEY = "EIA_API_KEY"
EIA_FUEL_URL = "https://api.eia.gov/v2/petroleum/pri/gnd/data/?api_key={}&frequency=weekly&data[0]=value&facets[area][]=STATE_CODE&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=1"

class LoadCalculationResult(BaseModel):
    deadhead_miles: float
    load_miles: float
    total_miles: float
    diesel_price: float
    diesel_cost: float
    market_rate_per_mile: float
    market_total: float
    profitability: str

def get_state_from_location(lat: float, lng: float):
    params = {
        "latlng": f"{lat},{lng}",
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(GEOCODE_URL, params=params)
    results = response.json().get("results", [])
    for component in results[0]["address_components"]:
        if "administrative_area_level_1" in component["types"]:
            return component["short_name"]
    return None

def get_diesel_price(state_code: str):
    url = EIA_FUEL_URL.replace("STATE_CODE", state_code).format(EIA_API_KEY)
    response = requests.get(url)
    data = response.json()
    return float(data["response"]["data"][0]["value"])

def get_miles(origin: str, destination: str):
    params = {
        "origins": origin,
        "destinations": destination,
        "key": GOOGLE_MAPS_API_KEY
    }
    response = requests.get(DISTANCE_MATRIX_URL, params=params)
    elements = response.json()["rows"][0]["elements"][0]
    return elements["distance"]["value"] / 1609.34  # convert meters to miles

def calculate_load_info(current_location: str, pickup: str, dropoff: str, mpg: float, offer: float, load_type: str):
    # Get distances
    deadhead = get_miles(current_location, pickup)
    load_miles = get_miles(pickup, dropoff)
    total_miles = round(deadhead + load_miles, 2)

    # Get diesel price
    geo_resp = requests.get(GEOCODE_URL, params={"address": current_location, "key": GOOGLE_MAPS_API_KEY})
    geo_data = geo_resp.json()
    location = geo_data["results"][0]["geometry"]["location"]
    state_code = get_state_from_location(location["lat"], location["lng"])
    diesel_price = get_diesel_price(state_code)

    # Diesel cost
    diesel_cost = round((total_miles / mpg) * diesel_price, 2)

    # Simulate market rate
    market_rate = 2.75
    market_total = round(load_miles * market_rate, 2)

    profitability = "Above Market" if offer >= market_total else "Below Market"

    return LoadCalculationResult(
        deadhead_miles=round(deadhead, 2),
        load_miles=round(load_miles, 2),
        total_miles=total_miles,
        diesel_price=round(diesel_price, 2),
        diesel_cost=diesel_cost,
        market_rate_per_mile=market_rate,
        market_total=market_total,
        profitability=profitability
    )
