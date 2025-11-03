#!/bin/bash

echo "Etap Smart Lock Kurulumu Başlatılıyor..."

# Gerekli paketlerin kurulumu
echo "Gerekli paketler yükleniyor..."
sudo apt-get update
sudo apt-get install -y wget python3-pyqt5

# Paket indirme ve kurulum
DOWNLOAD_URL="https://github.com/DePdasten/Etap-SmartLock/Etap-SmartLock/releases/latest/download/etap-smartlock_1.0.0_all.deb"
echo "Etap Smart Lock paketi indiriliyor..."
wget "$DOWNLOAD_URL" -O etap-smartlock.deb

# Paketi kur
echo "Paket kuruluyor..."
sudo dpkg -i etap-smartlock.deb
sudo apt-get install -f -y

# Temizlik
rm etap-smartlock.deb

echo "Kurulum tamamlandı!"
