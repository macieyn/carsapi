import requests

from rest_framework import serializers

class ExistInVPIC:

    def __call__(self, data):
        make = data["make"]
        model = data["model"]

        response = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json')
        returned_data = response.json()
        models = returned_data.get('Results')
        
        if not models:
            message = f"There is no car make with name {make}"
            raise serializers.ValidationError(message, 400)
        
        if model not in map(lambda x: x.get('Model_Name'), models):
            message = f"There is no car model with name {model} for {make}"
            raise serializers.ValidationError(message, 400)