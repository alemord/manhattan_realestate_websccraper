import requests

def get_data_from_api(api_url, limit=1000):
    
    params = {
        "$limit": limit,
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from the API: {api_url}")

def main():
    base_url = "https://data.cityofnewyork.us/resource/4e2n-s75z.json"
    data = get_data_from_api(base_url)

    for property in data:
        print(f"Name: {property.get('property_name')}")
        print(f"Address: {property.get('address')}")
        print(f"Price: {property.get('price')}")
        print("-" * 30)

if __name__ == "__main__":
    main()
