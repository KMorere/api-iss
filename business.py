import requests
from datetime import datetime

def call_api(call, path):
    try:
        response = requests.request(call, path, timeout=10)
        return response.json()
    except requests.exceptions as e:
        return f"API Call Error {e}"


def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)


def get_iss_position():
    """
    Get the ISS coordinates at a specific time.
    :return: The latitude, longitude of the ISS at 'timestamp'.
    """
    data = call_api("GET", "http://api.open-notify.org/iss-now.json")

    if data:
        formatted_data = {
            "latitude": data["iss_position"]["latitude"],
            "longitude": data["iss_position"]["longitude"],
            "timestamp": format_timestamp(data["timestamp"])
        }
    else:
        return "No data available"
    return formatted_data


def get_astronaut_data():
    """
    Get the amount of astronauts of the ISS and their name.
    """
    data = call_api("GET", "http://api.open-notify.org/astros.json")
    people = data["people"]

    if data:
        formatted_data = []
        formatted_data.append(len(people))
        for i, p in enumerate(people):
            formatted_data.append({
                "name": p["name"]
            })
    else:
        return "No data available"
    return formatted_data