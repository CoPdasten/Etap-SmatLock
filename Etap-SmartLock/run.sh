#!/bin/bash

# Uygulama çalışıyor mu kontrol et
if pgrep -f "etap-smartlock" > /dev/null; then
    echo "Uygulama zaten çalışıyor!"
    exit 1
fi

# Uygulamayı başlat
if [ -f "/usr/lib/etap-smartlock/src/main.py" ]; then
    pkexec python3 /usr/lib/etap-smartlock/src/main.py
else
    echo "Uygulama kurulu değil! Önce kurulum yapın."
    echo "Kurulum için: sudo ./install.sh"
fi
