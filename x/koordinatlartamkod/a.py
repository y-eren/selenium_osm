import requests
import time

def get_coordinates(address, api_key):
    url = f'https://api.opencagedata.com/geocode/v1/json?q={address}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        if results['results']:
            return results['results'][0]['geometry']['lat'], results['results'][0]['geometry']['lng']
        else:
            print(f"No results found for {address}.")
    else:
        print(f"Failed to retrieve data for {address}. HTTP Status code: {response.status_code}")
    return None

api_key = 'ba9835744fde4e60bedf57a1223c387f'

addresses = [
     "Taş Köprü, Adana",
    			    "Adana Kalesi, Adana",
    			    "Ulu Camii, Adana",
    			    "Bebekli Kilisesi, Adana",
    			    "Kız Kulesi, İstanbul",
    			    "Eyüp Sultan Camii, İstanbul",
    			    "Aya Yorgi Manastırı, İstanbul",
    			    "Rumeli Hisarı, İstanbul",
    			    "Kilitbahir Kalesi, Çanakkale",
    			    "Çimenlik Kalesi, Çanakkale",
    			    "Assos Antik Kenti, Çanakkale",
    			    "Parion Antik Kenti, Çanakkale",
    			    "Efes Antik Kenti, İzmir",
    			    "Pergamon Antik Kenti, İzmir",
    			    "Yeşilova Höyüğü, İzmir",
    			    "Bayraklı Smyrnası, İzmir",
    			    "Agora Ören Yeri, İzmir",
    			    "Metropolis Antik Yerleşimi, İzmir",
    			    "Teos Antik Kenti, İzmir",
    			    "Erythrai Antik Kenti, İzmir",
    			    "Alanya Kalesi, Antalya",
    			    "Apollon Tapınağı, Antalya",
    			    "Perge Antik Kenti, Antalya",
    			    "Antalya Müzesi, Antalya",
    			    "Patara Antik Kenti, Antalya",
    			    "Side Antik Kenti, Antalya",
    			    "Olympos Antik Kenti, Antalya",
    			    "Xanthos Antik Kenti, Antalya",
    			    "Kayseri Kalesi, Kayseri",
    			    "Diyarbakır Kalesi, Diyarbakır",
    			    "Aziziye Tabyası, Erzurum",
    			    "Çifte Minareli Medrese, Erzurum",
    			    "Erzurum Kalesi, Erzurum"
]

coordinates_list = []

for address in addresses:
    coordinates = get_coordinates(address, api_key)
    if coordinates:
        coordinates_list.append((address, coordinates))
        print(f"Mekan: {address}")
        print(f"Koordinatlar : {coordinates[0]},{coordinates[1]}")
    else:
        print(f"{address}: Coordinates not found")
    time.sleep(1)  # Respectful delay to avoid rate limiting

# Print final list of coordinates
print("\nTüm Mekanlar ve Koordinatları:")
for address, coordinates in coordinates_list:
    print(f"Mekan: {address}")
    print(f"Koordinatlar : {coordinates[0]},{coordinates[1]}")
