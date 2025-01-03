import re
import requests

# Kontrol edilecek dosya adı
file_name = "test"

# Kontrol edilecek domain desenleri
domain_pattern = r"https://dizipal(\d+)\.com"

def check_domain(domain):
    """Domainin erişilebilir olup olmadığını kontrol eder."""
    try:
        response = requests.head(domain, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Dosyayı oku
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

# Domain adresini bul
match = re.search(domain_pattern, content)
if match:
    current_number = int(match.group(1))  # Mevcut sayıyı al
    current_domain = match.group(0)  # Mevcut domain

    print(f"Kontrol ediliyor: {current_domain}")
    if not check_domain(current_domain):
        print(f"{current_domain} erişilemez, güncelleniyor...")
        new_number = current_number + 1
        new_domain = f"https://dizipal{new_number}.com"

        # İçeriği güncelle
        updated_content = re.sub(domain_pattern, new_domain, content)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(updated_content)
        print(f"Domain güncellendi: {current_domain} -> {new_domain}")
    else:
        print(f"{current_domain} erişilebilir, değişiklik yapılmadı.")
else:
    print("Domain adresi bulunamadı, işlem yapılmadı.")
