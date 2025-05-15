import requests
import json

# API URL (assuming local development)
URL = "http://localhost:8000/prediction/predict"

# Sample data for testing
test_data = {
    "sqft_living": 2000,
    "grade": 8,
    "bathrooms": 2.5,
    "bedrooms": 3,
    "waterfront": 0,
    "view": 0,
    "sqft_basement": 0,
    "yr_built": 1990,
    "lat": 47.6062,
    "long": -122.3321
}

# Make POST request
def test_api():
    try:
        # Send POST request
        response = requests.post(URL, json=test_data)
        
        # Check response
        if response.status_code == 200:
            result = response.json()
            print("API test successful!")
            print(f"Predicted price: ${result['predicted_price']:,.2f}")
            return True
        else:
            print(f"API test failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error testing API: {str(e)}")
        return False

if __name__ == "__main__":
    test_api()