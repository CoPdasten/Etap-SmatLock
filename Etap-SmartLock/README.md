# Etap Smart Lock

Sınıflarda bilgisayar kullanımını kontrol etmek ve yönetmek için geliştirilmiş bir kilit sistemi.

## Özellikler

- Ders saatlerine göre otomatik kilit sistemi
- Sudo yetkilendirme sistemi
- Masaüstü kısayol desteği
- Grafiksel kullanıcı arayüzü
- Sistemle entegre çalışma

## Kurulum Gereksinimleri

- Ubuntu/Debian tabanlı Linux dağıtımı
- Python 3.6+
- Root/Sudo yetkisi
- İnternet bağlantısı

## Hızlı Kurulum
```bash
wget -O - https://raw.githubusercontent.com/CoPdasten/Etap-SmatLock/main/install.sh | sudo bash
```

## Manuel Kurulum Adımları

1. Depoyu indirin:
```bash
git clone https://github.com/CoPdasten/Etap-SmatLock.git
cd Etap-SmatLock
```

2. Kurulum scriptini çalıştırın:
```bash
sudo chmod +x install.sh
sudo ./install.sh
```

## Sorun Giderme

- Eğer kurulum sırasında hata alırsanız:
```bash
sudo apt-get update
sudo apt-get install -f
```

- Kilit çalışmıyorsa:
```bash
sudo systemctl restart etap-smartlock
```

## Kullanım

1. Masaüstündeki "Etap Smart Lock" kısayolunu çalıştırın
2. Sudo şifrenizi girin
3. Uygulama ayarlarını yapılandırın
4. Ders programını düzenleyin

## Test Etme

### Kurulum Testi
```bash
# Test ortamında kurulum
sudo ./install.sh --test

# Kurulum loglarını kontrol etme
cat /var/log/etap-smartlock-install.log
```

### Uygulama Testi
1. Test modunda başlatma:
```bash
etap-smartlock --test
```

2. Kilit sistemini test etme:
```bash
# Kilidi manuel test etme
sudo etap-smartlock-test --lock
sudo etap-smartlock-test --unlock

# Zamanlayıcı testi
sudo etap-smartlock-test --schedule
```

### Hata Ayıklama
```bash
# Debug modunda çalıştırma
etap-smartlock --debug

# Log dosyalarını kontrol etme
tail -f /var/log/etap-smartlock.log
```

## Proje Yapısı
```
etap-smartlock/
├── debian/
│   ├── control
│   ├── postinst
│   ├── etap-smartlock.service
│   └── com.etap.smartlock.policy
├── src/
│   ├── main.py
│   ├── gui/
│   │   └── main_window.py
│   ├── core/
│   │   ├── lock_controller.py
│   │   └── schedule_manager.py
│   ├── models/
│   │   └── lock_status.py
│   └── utils/
│       └── config.py
├── setup.py
├── install.sh
├── build_deb.sh
└── README.md
```

## Sistem Gereksinimleri

- Python 3.6 veya üzeri
- PyQt5
- Debian tabanlı Linux dağıtımı (Ubuntu, Linux Mint vb.)

## Güvenlik

- Uygulama her çalıştırıldığında sudo yetkilendirmesi ister
- PolicyKit ile güvenli yetkilendirme
- Sistem servisi olarak çalışma

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

Eyüp ATILGAN
- Email: eyupatilgan41@gmail.com
- GitHub: [@CoPdasten](https://github.com/CoPdasten)

## Çalıştırma

1. Masaüstündeki kısayoldan:
   - Masaüstündeki "Etap Smart Lock" simgesine çift tıklayın
   - Yönetici şifrenizi girin

2. Terminal üzerinden:
```bash
# Çalıştırma scriptini çalıştırılabilir yap
chmod +x run.sh

# Uygulamayı başlat
./run.sh
```

3. Servis olarak:
```bash
# Servisi başlat
sudo systemctl start etap-smartlock

# Otomatik başlatmayı etkinleştir
sudo systemctl enable etap-smartlock
```

### Hata Durumunda
- "Uygulama zaten çalışıyor" hatası alırsanız:
```bash
pkill -f "etap-smartlock"
./run.sh
```
