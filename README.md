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

🌐 Cloudflare Turnstile Bypass - Craftrise Login Checker (v2.4)

Bu proje, Cloudflare Turnstile (Invisible) koruması bulunan web sitelerinde (örnek: craftrise.com.tr) oturum açma testleri yapmak için geliştirilmiş konsol tabanlı bir araçtır. combo.txt içerisindeki kullanıcı adı ve şifre kombinasyonlarını sırasıyla dener ve geçerli olanları otomatik olarak live.txt dosyasına kaydeder.

🚀 Özellikler

Otomatik API Key Yönetimi (config.json): API anahtarınızı yalnızca ilk çalıştırıldığında bir kez girersiniz; program bunu otomatik olarak kaydeder ve sonraki açılışlarda tekrar sormaz.

API Key Doğrulama: Girilen veya kayıtlı olan RapidAPI anahtarının geçerliliği başlangıçta otomatik olarak test edilir.

Cloudflare Turnstile Çözücüsü: RapidAPI üzerinden otomatik token alma ve kullanma altyapısı.

Renkli Konsol Arayüzü (colorama): Başarılı (LIVE), başarısız (DEAD) ve hata durumları renkli ve düzenli loglarla takip edilir.

Detaylı İstatistikler: Tarama sonrasında toplam taranan, live, dead ve hata sayılarını özetleyen rapor sunar.

🔧 Kurulum

Python 3 sisteminizde kurulu olmalıdır.

Gerekli kütüphaneleri yükleyin:

pip install requests colorama


Aynı dizine combo.txt adında bir dosya oluşturun ve her satıra şu formatta hesap bilgilerinizi ekleyin:

kullanici1:sifre1
kullanici2:sifre2


🅾️ Ücretsiz API Anahtarı

35 ücretsiz istek hakkı sunan API'yi buradan alabilirsiniz:
👉 https://rapidapi.com/ttur5678/api/turnstile-bypass-api1/pricing

Siteye üye olun.

Ücretsiz planı seçin.

Programı ilk kez çalıştırdığınızda konsolda istenen yere X-RapidAPI-Key değerinizi yapıştırın (anahtar otomatik olarak config.json dosyasına kaydedilecektir).

▶️ Kullanım

Aracı çalıştırmak için terminal veya komut istemcisine şunu yazın:

python cr.py


Başarılı girişler anlık olarak konsola yazdırılır ve live.txt dosyasına kaydedilir.

⚠️ Uyarı

Bu araç yalnızca eğitim ve araştırma amaçlı paylaşılmıştır.
Herhangi bir siteye izinsiz giriş yapmak yasalara aykırıdır ve ciddi sonuçlar doğurabilir.
Tüm sorumluluk kullanıcıya aittir.

📌 Geliştirici: wezaxy

🛠️ Katkılar ve pull request'ler memnuniyetle karşılanır.

🤝 Katkıda Bulunmak: Sorunları ve geliştirme taleplerini göndermekten çekinmeyin!

⭐ Destek: Bu aracı faydalı bulursanız, lütfen GitHub'da bir yıldız verin!

Discord: wezaxy

Destek Sunucusu: https://discord.gg/c44FB4PFcW
