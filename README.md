Özellikler

 🛡️ Akıllı Cloudflare Bypass: RapidAPI altyapısı üzerinden Cloudflare Turnstile (Invisible) korumasını otomatik olarak çözer ve token üretir.

 🔑 Konfigürasyon Yönetimi (config.json): API anahtarınızı yalnızca ilk çalıştırıldığında bir kez girersiniz; sistem otomatik olarak kaydeder ve sonraki oturumlarda tekrar sormaz.

 🔍 Otomatik API Sağlık Testi: Başlangıç aşamasında API anahtarınızın geçerliliğini ve kotasını canlı olarak doğrular, geçersiz veya süresi dolmuş anahtarlarda güvenli yönlendirme sağlar.

 🎨 Gelişmiş Terminal Arayüzü (colorama): LIVE, DEAD ve hata durumlarını özel renk paleti ve şık bir banner arayüzüyle anlık olarak raporlar.

 📊 Detaylı İstatistik Raporu: Tarama tamamlandığında toplam taranan, geçerli, geçersiz ve hata sayımlarını içeren özet bir tablo sunar.

Kurulum

Projeyi bilgisayarınıza kurmak ve çalıştırmaya hazır hale getirmek için aşağıdaki adımları takip edin:

Depoyu Klonlayın veya İndirin

Proje dosyalarını bilgisayarınıza indirin.

Gerekli Kütüphaneleri Yükleyin

Terminal veya komut istemcisini açarak gerekli Python kütüphanelerini yükleyin:

pip install requests colorama


Combo Dosyasını Hazırlayın

Proje klasörünün içine combo.txt adında bir metin dosyası oluşturun. Hesap bilgilerini her satıra kullaniciadi:sifre formatında ekleyin:

kullanici1:sifre1
kullanici2:sifre2


Kullanım

Tüm hazırlıklar tamamlandıktan sonra aracı çalıştırmak oldukça basittir:

Terminalde proje dizinine gelin.

Komut satırına şunu yazarak çalıştırın:

python cr.py


İlk çalıştırmada sizden istenen RapidAPI Turnstile Bypass anahtarınızı girin (anahtarınız şifrelenmiş olarak config.json dosyasına kaydedilecektir).

Tarama süreci otomatik olarak başlayacak; başarılı girişler hem konsola renklendirilerek yazılacak hem de otomatik olarak live.txt dosyasına kaydedilecektir.

🅾️ API Anahtarı Temini

Sistemin kararlı çalışabilmesi ve Turnstile doğrulamalarını geçebilmesi için bir RapidAPI anahtarına ihtiyacınız vardır.

35 ücretsiz istek hakkı sunan ilgili API planına göz atmak ve temin etmek için: 👉 RapidAPI Turnstile Bypass Pricing
