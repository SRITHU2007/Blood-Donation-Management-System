import requests


def get_nearby_hospitals(city):

    headers = {
        "User-Agent": "BloodDonationApp/1.0"
    }

    try:
        # ----------------------------
        # Step 1: Get City Coordinates
        # ----------------------------
        geo_response = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={
                "q": city,
                "format": "json",
                "limit": 1
            },
            headers=headers,
            timeout=10
        )

        geo_response.raise_for_status()

        city_data = geo_response.json()

        if not city_data:
            print("City not found.")
            return []

        lat = city_data[0]["lat"]
        lon = city_data[0]["lon"]

        print("City Coordinates:", lat, lon)

        # ----------------------------
        # Step 2: Search Hospitals
        # ----------------------------
        query = f"""
        [out:json][timeout:25];
        (
          node["amenity"="hospital"](around:10000,{lat},{lon});
          way["amenity"="hospital"](around:10000,{lat},{lon});
          relation["amenity"="hospital"](around:10000,{lat},{lon});
        );
        out center;
        """

        response = requests.post(
            "https://lz4.overpass-api.de/api/interpreter",
            data=query,
            headers=headers,
            timeout=30
        )

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print(response.text)
            return []

        try:
            data = response.json()
        except Exception as e:
            print("JSON Error:", e)
            print(response.text[:500])
            return []

        hospitals = []

        for item in data.get("elements", []):

            if "lat" in item:
                h_lat = item["lat"]
                h_lon = item["lon"]
            elif "center" in item:
                h_lat = item["center"]["lat"]
                h_lon = item["center"]["lon"]
            else:
                continue

            hospitals.append({
                "display_name": item.get("tags", {}).get(
                    "name",
                    "Unnamed Hospital"
                ),
                "lat": h_lat,
                "lon": h_lon
            })

        print("Hospitals Found:", len(hospitals))
        print("Status Code:", response.status_code)
        print("Response:", response.text[:300])
        print("Hospitals Found:", len(hospitals))

        return hospitals

    except Exception as e:
        print("Map Service Error:", e)
        return []