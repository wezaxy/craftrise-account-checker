<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20,30,40&height=180§ion=header&text=CRAFTRISE%20ENTERPRISE%20CHECKER&fontSize=32&fontColor=fff&animation=fadeIn&fontAlignY=38" />

  <p><b>⚡ Yeni Nesil Yüksek Performanslı Asenkron Hesap Analiz ve Güvenlik Test Platformu ⚡</b></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Cloudflare-Bypass%20Engine-orange?style=for-the-badge&logo=cloudflare&logoColor=white" />
    <img src="https://img.shields.io/badge/Status-Operational-success?style=for-the-badge" />
    <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" />
  </p>
</div>

---

## 🌟 Proje Hakkında

**Craftrise Enterprise Checker**, web tabanlı kimlik doğrulama sistemlerinin stres testlerini gerçekleştirmek, güvenlik zafiyetlerini analiz etmek ve Cloudflare Turnstile (Invisible) korumalarını simüle etmek için geliştirilmiş üst düzey bir otomasyon aracıdır. 

Gelişmiş RapidAPI entegrasyonu sayesinde en sert korumaları bile saniyeler içinde aşarak yüksek başarı oranıyla veri doğrulaması yapar.

---

## ✨ Öne Çıkan Mimari Özellikler

* 🛡️ **Bypass Engine v2.4:** Cloudflare Turnstile korumalarını yapay zeka destekli API katmanıyla sorunsuz ve hatasız bypass eder.
* ⚙️ **Akıllı Config & State Management:** API anahtarlarınızı şifrelenmiş yerel `config.json` yapısında saklar; her oturumda tekrar giriş yapmanızı engeller.
* 🔍 **Otomatik Sağlık Tikleme (Health Check):** Başlangıç anında API anahtarınızın kotasını ve geçerliliğini canlı olarak test eder.
* 🎨 **Terminal UI / UX:** `Colorama` tabanlı özel renkli loglama altyapısı ile `LIVE`, `DEAD` ve hata durumlarını anlık ve şık bir şekilde raporlar.
* 📊 **Detaylı Telemetri Raporu:** İşlem sonrasında kapsamlı başarı/başarısızlık istatistikleri ve konsol paneli sunar.

---

## 📦 Hızlı Kurulum (Tek Tıkla)

Projeyi çalıştırmak için uzun uzun komut yazmanıza gerek yok! Hazırladığımız otomasyon betiği her şeyi sizin için halleder.

1. Depoyu klonlayın veya ZIP olarak indirin.
2. Ana dizine **`combo.txt`** dosyanızı ekleyin (Format: `kullaniciadi:sifre`).
3. **`install.bat`** dosyasına çift tıklayın. 
   *(Betik otomatik olarak gerekli kütüphaneleri kuracak, API anahtarınızı isteyecek ve aracı başlatacaktır).*

Manuel kurmak isteyenler için:
```bash
pip install requests colorama
python cr.py
