import googlemaps
import os

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def get_deadhead_miles(current_location: str, pickup_location: str) -> float:
    try:
        result = gmaps.distance_matrix(current_location, pickup_location, mode="driving")
        distance = result["rows"][0]["elements"][0]["distance"]["value"]  # in meters
        return round(distance / 1609.34, 2)  # convert to miles
    except Exception as e:
        print(f"Error getting deadhead miles: {e}")
        return 0.0

def get_load_miles(pickup_location: str, dropoff_location: str) -> float:
    try:
        result = gmaps.distance_matrix(pickup_location, dropoff_location, mode="driving")
        distance = result["rows"][0]["elements"][0]["distance"]["value"]  # in meters
        return round(distance / 1609.34, 2)  # convert to miles
    except Exception as e:
        print(f"Error getting load miles: {e}")
        return 0.0