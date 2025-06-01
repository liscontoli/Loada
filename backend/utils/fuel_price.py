import requests
import os

EIA_API_KEY = os.getenv("EIA_API_KEY")

def get_fuel_price_by_state(state_abbr: str) -> float:
    url = f"https://api.eia.gov/v2/petroleum/pri/gnd/data/?api_key={EIA_API_KEY}&frequency=weekly&data[0]=value&facets[area][]=REGION-{state_abbr.upper()}&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        value = data.get("response", {}).get("data", [])[0].get("value", 0.0)
        return float(value)
    except Exception as e:
        print(f"Error fetching fuel price for state {state_abbr}: {e}")
        return 0.0