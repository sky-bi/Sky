import requests
import json
import os

# URL'den JSON verisini al
url = "https://vavoo.to/channels"
response = requests.get(url)

# Eğer isteğin sonucu başarılıysa
if response.status_code == 200:
    try:
        data = response.json()  # JSON verisini al
        # Eğer veri boşsa, hata mesajı göster
        if not data:
            print("JSON verisi boş döndü.")
        else:
            # 'v.json' dosyasının var olup olmadığını kontrol et
            if os.path.exists('v.json'):
                # Dosya varsa, yeni veriyi eski dosya ile değiştir
                with open('v.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    print("Yeni veri dosyaya kaydedildi.")
            else:
                # Dosya yoksa, yeni dosya oluştur ve veriyi yaz
                with open('v.json', 'w') as f:
                    json.dump(data, f, indent=4)
                    print("Yeni v.json dosyası oluşturuldu ve veri kaydedildi.")
    except ValueError:
        print("JSON verisi geçersiz veya hatalı.")
else:
    print(f"Veri çekilemedi. HTTP Durum Kodu: {response.status_code}")
