import requests
import json
import os

# URL'den JSON verisini al
url = "https://vavoo.to/channels"
response = requests.get(url)

# Eğer isteğin sonucu başarılıysa
if response.status_code == 200:
    data = response.json()  # JSON verisini al

    # 'v.json' dosyasının var olup olmadığını kontrol et
    if os.path.exists('v.json'):
        # Dosya varsa, yeni veriyi eski dosya ile değiştir
        with open('v.json', 'w') as f:
            json.dump(data, f, indent=4)
    else:
        # Dosya yoksa, yeni dosya oluştur ve veriyi yaz
        with open('v.json', 'w') as f:
            json.dump(data, f, indent=4)
else:
    print("Veri çekilemedi. HTTP Durum Kodu:", response.status_code)
