# 🌐 Cloudflare Turnstile Bypass - Craftrise Login Checker

Bu proje, **Cloudflare Turnstile (Invisible)** koruması bulunan web sitelerinde (örnek: [craftrise.com.tr](http://craftrise.com.tr)) oturum açmayı test etmek için hazırlanmıştır.
Kullanıcı adı ve şifre kombinasyonlarını dener, geçerli olanları (`live.txt`) dosyasına kaydeder.

## 🚀 Özellikler

* Cloudflare Turnstile çözücüsü (RapidAPI üzerinden)
* Otomatik token alma ve kullanma
* JSON kontrolü ile başarılı giriş ayrımı
* Geçerli girişlerin `live.txt` dosyasına yazılması
* combo.txt den kullanıcıad:şifre olarak kaydedilmiş verileri alıp kontrol etmeye yarar

## 🔧 Kurulum

1. Python 3 yüklü olmalıdır.
2. Gerekli kütüphane:

```bash
pip install requests
```

3. `combo.txt` adında bir dosya oluşturun ve her satıra şu şekilde kullanıcı adı ve şifre ekleyin:

```
kullanici1:sifre1
kullanici2:sifre2
```

4. Kod dosyasındaki şu satırı bulun:

```python
"x-rapidapi-key": "YOUR API KEY",
```

Ve `"YOUR API KEY"` kısmını kendi API anahtarınızla değiştirin.

## 🅾️ Ücretsiz API Anahtarı

* **35 ücretsiz istek hakkı** sunan API'yi buradan alabilirsiniz:
  👉 [https://rapidapi.com/ttur5678/api/turnstile-bypass-api1/pricing](https://rapidapi.com/ttur5678/api/turnstile-bypass-api1/pricing)

1. Siteye üye olun.
2. Ücretsiz planı seçin.
3. Size verilen `X-RapidAPI-Key` değerini kodda ilgili yere yapıştırın.

## ▶️ Kullanım

Kod dosyasını çalıştır:

```bash
python cr.py
```

Başarılı girişler terminale yazdırılır ve `live.txt` dosyasına kaydedilir.

## ⚠️ Uyarı

> Bu araç yalnızca **eğitim ve araştırma** amaçlı paylaşılmıştır.
> Herhangi bir siteye izinsiz giriş yapmak **yasalara aykırıdır** ve ciddi sonuçlar doğurabilir.
> Tüm sorumluluk kullanıcıya aittir.

---

📌 Geliştirici: wezaxyy
🛠️ Katkılar ve pull request'ler memnuniyetle karşılanır.
🤝 Katkıda Bulunmak
Sorunları ve geliştirme taleplerini göndermekten çekinmeyin!

⭐ Destek
Bu aracı faydalı bulursanız, lütfen GitHub'da bir yıldız verin!

Discord: wezaxyy
