import os
import requests
from dotenv import load_dotenv

# Load .env file variables into environment
load_dotenv()

EIA_API_KEY = os.getenv("EIA_API_KEY")
DEFAULT_DIESEL_PRICE = 4.15  # fallback price if API fails

def get_fuel_price_by_state(state_abbr: str) -> float:
    url = (
        f"https://api.eia.gov/v2/petroleum/pri/gnd/data/?api_key={EIA_API_KEY}"
        f"&frequency=weekly&data[0]=value&facets[area][]=REGION-{state_abbr.upper()}"
        f"&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=1"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        value = data.get("response", {}).get("data", [])[0].get("value", DEFAULT_DIESEL_PRICE)
        return float(value)

    except requests.exceptions.RequestException as e:
        print(f"❌ Fuel price fetch failed: {e}")
        return DEFAULT_DIESEL_PRICE

    except Exception as e:
        print(f"❌ Unexpected error in get_fuel_price_by_state: {e}")
        return DEFAULT_DIESEL_PRICE