import requests

def fetch_calming_images():
    ACCESS_KEY = "rFC_HvU_l26AMtqZ70YF1AuFZr61ExvUna_h8zhBXlk"
    url = "https://api.unsplash.com/photos/random"
    params = {
        "query": "calm+landscape",
        "count": 2  # Fetch two images
    }
    headers = {
        "Authorization": f"Client-ID {ACCESS_KEY}"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return [image["urls"]["regular"] for image in data]  # Return list of image URLs
        else:
            print("Error:", response.status_code, response.json())
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None
