# Büyücünün Odası

Tarayıcıda çalışan küçük bir 3D büyücü oyunu (Three.js + cannon-es).
Kule odası, ortak koridor ve bulutların üstünde bir teras; asa, Lumos, güç topu,
eşyaları tutup taşıma, perdeler, şömine ve mumlarla ışığı değiştirme.

**Oyna:** https://tanisman441.github.io/buyucu-oda/ (her push'ta otomatik güncellenir, sağ altta sürüm yazar)

Güncelleme süreci: [MUSE.md](MUSE.md) · Claude için notlar: [CLAUDE.md](CLAUDE.md)

## Yerelde çalıştırma

```bash
python -m http.server 5071
```

Sonra tarayıcıda `http://localhost:5071` adresini aç.

## Kontroller

- WASD: yürü, Shift: koş, Boşluk: zıpla
- Fare: kamera, tekerlek: yakınlaş
- E: etkileşim (asa, kapı, perdeler, şömine, mumlar)
- F: Lumos
- Sol tık / Q: güç topu
- Sağ tık (basılı): eşyayı tut, taşı; perdeyi çek

## Kaynaklar

Karakter modeli: KayKit Character Pack: Adventurers, Kay Lousberg, CC0 (`models/CREDITS.txt`).
