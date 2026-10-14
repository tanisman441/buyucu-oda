# Muse için çalışma rehberi

Bu oyunu sen (Muse) güncelleyeceksin: isteği Claude'a yazacaksın, Claude kodu değiştirip yayınlayacak, sen oynayıp deneyecek ve sonucu yine Claude'a bildireceksin.

## Adresler

- **İstek yazma yeri:** claude.ai/code → `tanisman441/buyucu-oda` deposuna bağlı **bulut oturumu**. Hep **aynı oturumu** kullan ki Claude önceki konuşmayı hatırlasın. Oturum çok uzarsa yeni bir oturum açıp ilk mesajda ne üzerinde çalışıldığını kısaca yaz.
- **Oyun:** https://tanisman441.github.io/buyucu-oda/

## Döngü

1. **İste:** Oturuma tek ve net bir istek yaz. Örnek: "Terastaki ağacın yanına bir baykuş ekle, E'ye basınca uçsun."
2. **Bekle:** Claude değişikliği yapıp gönderince bir **sürüm kodu** (ör. `a1b2c3d`) ve "Nasıl denenir" adımları yazar.
3. **Aç:** `https://tanisman441.github.io/buyucu-oda/?v=SÜRÜMKODU` adresini aç. Yayınlanması 1–2 dakika sürer. Sağ alt köşede `sürüm a1b2c3d` yazmıyorsa biraz bekleyip sayfayı yenile.
4. **Dene:** Başlangıç ekranına tıkla, Claude'un verdiği adımları uygula.
5. **Bildir:** Aynı oturuma şunları yaz:
   - Ne çalıştı, ne çalışmadı (adım adım).
   - Gördüğün hata mesajları (tarayıcı konsolu varsa oradan).
   - Görüntüde garip olan şeyler (ne, nerede).
   - Sonraki istek.

## Kontroller

| Tuş | İş |
|---|---|
| W A S D | yürü (Shift: koş) |
| Boşluk | zıpla |
| Fare / sürükle | kamera |
| Tekerlek | yakınlaş / uzaklaş |
| E | etkileşim: asa, kapı, perdeler, şömine, mumlar |
| F | Lumos |
| Sol tık / Q | güç topu |
| Sağ tık (basılı) | eşyayı tut ve taşı, perdeyi çek |
| Tab | görev listesi |

Önce masadaki asayı almak gerekir. Kapı odanın ön duvarında, koridorun sonundaki kemerden terasa çıkılır.

## Notlar

- Fare kilitlenmezse (sağ/sol tık çalışmazsa) bunu Claude'a söyle; klavye alternatifi eklenebilir.
- Oyun yavaş çalışıyorsa bunu da yaz; görsel kalite düşürülebilir.
