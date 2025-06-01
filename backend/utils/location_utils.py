import requests
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_state_from_coordinates(lat: float, lng: float) -> str:
    try:
        url = (
            f"https://maps.googleapis.com/maps/api/geocode/json"
            f"?latlng={lat},{lng}&key={GOOGLE_MAPS_API_KEY}"
        )
        response = requests.get(url)
        response.raise_for_status()
        results = response.json().get("results", [])

        for result in results:
            for component in result.get("address_components", []):
                if "administrative_area_level_1" in component["types"]:
                    return component["short_name"]

        return "Unknown"
    except Exception as e:
        print(f"Error getting state from coordinates: {e}")
        return "Unknown"