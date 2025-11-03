# ETAP SmartLock - Nasıl Çalışır?

ETAP SmartLock (Akıllı Tahta Otomatik Kilitleme Sistemi), eğitim kurumlarında akıllı tahtaların güvenliğini sağlamak için tasarlanmış bir yazılım çözümüdür.

## 🔑 Temel Özellikler

1. **Otomatik Kilitleme**: Teneffüs zamanlarında akıllı tahtayı otomatik olarak kilitler
2. **Ders Programı Yönetimi**: Öğretmenler günlük/haftalık ders programlarını kolayca düzenleyebilir
3. **PIN Koruması**: Yetkisiz kullanımı engellemek için PIN tabanlı güvenlik sistemi
4. **Aktivite Günlüğü**: Kilit/açma işlemlerinin detaylı kayıtlarını tutar
5. **Esnek Zamanlama**: Özelleştirilebilir ders ve teneffüs süreleri

## 🛠️ Sistem Nasıl Çalışır?

Sistem üç ana bileşenden oluşur:

### 1. Ana Uygulama Arayüzü
- **Ders Takvimi Sekmesi**
  - Haftalık ders programı görüntüleme
  - Ders ekleme/düzenleme/silme
  - Teneffüs sürelerini belirleme

- **Kilit Ayarları Sekmesi**
  - PIN belirleme ve değiştirme
  - Kilit test fonksiyonu
  - Güvenlik seçenekleri

- **Sistem Durumu Sekmesi**
  - Anlık kilit durumu
  - Sonraki ders/teneffüs bilgisi
  - Sistem günlüğü

### 2. Kilit Ekranı
- Teneffüs başladığında otomatik açılır
- Tam ekran modunda çalışır
- PIN girişi olmadan kapatılamaz
- Kalan süre göstergesi

### 3. Arka Plan Servisi
- Sürekli zaman kontrolü yapar
- Ders programına göre otomatik kilitleme
- Sistem başlangıcında otomatik çalışır

## 💾 Veri Yönetimi

- Ders programı JSON formatında saklanır
- Kullanıcı ayarları yerel olarak kaydedilir
- Aktivite günlüğü düzenli olarak güncellenir

## 🔄 Çalışma Döngüsü

1. Öğretmen ders programını sisteme girer
2. Program arka planda çalışmaya başlar
3. Teneffüs başladığında:
   - Kilit ekranı otomatik açılır
   - Tahta kilitlenir
4. Ders başladığında:
   - PIN doğrulaması yapılır
   - Kilit otomatik açılır

## 🚀 Kurulum ve Başlatma

1. Uygulama ETAP sistemine kurulur
2. İlk çalıştırmada temel ayarlar yapılır:
   - PIN belirlenir
   - Ders programı girilir
3. Sistem otomatik başlatma dosyası oluşturulur
4. Program arka planda çalışmaya başlar

## ⚙️ Teknik Gereksinimler

- Python 3.3 veya üzeri
- PyQt5 GUI kütüphanesi
- SQLite veya JSON veri depolama
- ETAP uyumlu sistem

## 🔍 Hata Durumları

- PIN unutulması durumunda yönetici sıfırlama seçeneği
- Sistem çökmesi durumunda otomatik yeniden başlatma
- Veri kaybı durumunda yedekleme sistemi

Bu sistem, eğitim kurumlarında akıllı tahta güvenliğini sağlamak için kolay kullanımlı ve güvenilir bir çözüm sunar.


Geliştirici:
Eyyüp Efe Adıgüzel - CoPdasten