import requests


def get_models_for_car_make(make):
    response = requests.get(
        f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
    )
    returned_data = response.json()
    models = returned_data.get("Results")
    return models
