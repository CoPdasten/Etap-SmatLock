#!/bin/bash

echo "Etap Smart Lock Kurulum Başlatılıyor..."

# Hata kontrolü
set -e

# Sudo kontrolü
if [ "$EUID" -ne 0 ]; then 
    echo "Bu script root yetkisi gerektirir. Lütfen sudo ile çalıştırın."
    exit 1
fi

# Gerekli paketleri kur
echo "Gerekli paketler yükleniyor..."
apt-get update
apt-get install -y python3 python3-pyqt5 xdg-utils

# Uygulama dizinlerini oluştur
mkdir -p /usr/lib/etap-smartlock
mkdir -p /etc/etap-smartlock
mkdir -p /usr/share/applications

# Kaynak dosyaları kopyala
cp -r etap-smartlock/* /usr/lib/etap-smartlock/
chmod +x /usr/lib/etap-smartlock/src/main.py

# Assets dizinini oluştur ve dosyaları kopyala
mkdir -p /usr/lib/etap-smartlock/assets
cp -r etap-smartlock/assets/* /usr/lib/etap-smartlock/assets/
chmod 644 /usr/lib/etap-smartlock/assets/*

# Masaüstü kısayolu oluştur
cat > /usr/share/applications/etap-smartlock.desktop << EOF
[Desktop Entry]
Name=Etap Smart Lock
Exec=pkexec python3 /usr/lib/etap-smartlock/src/main.py
Icon=/usr/lib/etap-smartlock/assets/logo.svg
Type=Application
Categories=Utility;
EOF

echo "Kurulum tamamlandı!"
