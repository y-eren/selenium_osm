import requests
import os

# Google API anahtarı ve arama motoru ID'si
API_KEY = 'AIzaSyANWvekQ2q1rDD0XDjRG6zSqr2P3m0AI2c'
CX = '0289707bcf90947b5'

url = 'https://www.googleapis.com/customsearch/v1'

veriler = [
    
    "Tokyo, Tokyo Metropolitan Government Main Building 1",
    "Tokyo, Akihabara"
    
]

def url_al(query):
    params = {
        'q': query,        # Aranacak kelime
        'key': API_KEY,
        'cx': CX,
        'searchType': 'image',
        'num': 2,          # Sonuç sayısı
        'safe': 'high',    # Güvenli arama
    }
    
    response = requests.get(url, params=params)
    
    data = response.json()
    
    # Gelen veriden resim URL'sini alma
    if 'items' in data:
        image_url = data['items'][0]['link']
        return image_url
    else:
        return None

# Örnek olarak her bir veri için resim URL'lerini alalım
for veri in veriler:
    image_url = url_al(veri)
    if image_url:
        print(f"{veri} : {image_url}")
    else:
        print(f"No image found for query: {veri}")
