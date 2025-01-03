import json
import random
import string

# Rastgele bir metin oluştur
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

# JSON dosyasının yolunu belirle
json_file_path = 'v.json'

# v.json dosyasına yazma işlemi
data = {'random_string': random_string}

with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file)

print(f"Random string '{random_string}' başarıyla {json_file_path} dosyasına yazıldı.")
