import requests
import os

# Google API anahtarı ve arama motoru ID'si
API_KEY = 'AIzaSyDhU-SpyPmFm9AfJC2HjkwMOqgvm8xHOVU'
CX = '0289707bcf90947b5'

url = 'https://www.googleapis.com/customsearch/v1'

veriler = ["Eiffel Kulesi", "Colessium"]

# Arama yapma ve görüntüleri indirme fonksiyonu
def download_images(query):
    params = {
        'q': query,        # Aranacak kelime
        'key': API_KEY,
        'cx': CX,
        'searchType': 'image',
        'num': 2,          # Sonuç sayısı
        'safe': 'high',    # Güvenli arama
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # HTTP hata durumunda hata fırlatır
        results = response.json()['items']

        # 'images' klasörünü oluşturma
        if not os.path.exists('images'):
            os.makedirs('images')

        # Görüntüleri indirme ve kaydetme
        for i, item in enumerate(results):
            image_url = item['link']
            image_name = f'{query}_{i}.jpg'  # Görüntü dosya adı
            image_path = os.path.join('images', image_name)  # Dosya yolu

            # Görüntüyü indirme
            with open(image_path, 'wb') as f:
                response = requests.get(image_url)
                f.write(response.content)

            print(f"'{image_name}' başarıyla indirildi ve 'images' klasörüne kaydedildi.")

    except Exception as e:
        print(f"Hata: {e}")

# "veriler" listesinin her bir elemanı için arama yapma
for veri in veriler:
    download_images(veri)