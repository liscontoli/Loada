import json
import os

# Define path to the mock data file
MOCK_DATA_PATH = os.path.join(os.path.dirname(__file__), "mock_market_rates.json")

def get_mock_market_rate(load_type: str, pickup: str, dropoff: str) -> float:
    try:
        with open(MOCK_DATA_PATH, "r") as file:
            data = json.load(file)
        
        route_key = f"{pickup} to {dropoff}"
        rate = data.get(load_type, {}).get(route_key)

        if rate is None:
            raise ValueError(f"No market rate found for {load_type} from {pickup} to {dropoff}")
        
        return float(rate)

    except FileNotFoundError:
        raise Exception("Market rate mock file not found.")
    except json.JSONDecodeError:
        raise Exception("Error decoding market rate mock file.")