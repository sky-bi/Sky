import requests
import re

def get_new_domain(url):
    try:
        # URL'ye HTTP isteği gönder
        response = requests.get(url, allow_redirects=True)

        # Yönlendirme varsa, yeni URL'yi al
        if response.history:
            # Yönlendirilmiş URL
            return response.url
        else:
            return None
    except requests.RequestException:
        # Eğer URL erişilemezse, sayıyı artırarak yeni domain oluştur
        match = re.search(r"https://dizipal(\d+)\.com", url)
        if match:
            number = int(match.group(1))
            new_number = number + 1
            return f"https://dizipal{new_number}.com"
        else:
            return None

def update_domain_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()

    new_domain = get_new_domain(content)

    if new_domain:
        # Yeni domain'i dosyaya yaz
        with open(file_path, 'w') as file:
            file.write(new_domain)
        print(f"Domain güncellendi: {new_domain}")
    else:
        print("Domain değişiklik yapılacak bir durum yok.")

if __name__ == "__main__":
    file_path = "test"  # test dosyasının yolu
    update_domain_in_file(file_path)
