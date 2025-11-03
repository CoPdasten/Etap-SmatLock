#!/bin/bash

# Paket adı ve versiyonu
PACKAGE_NAME="etap-smartlock"
VERSION="1.0.0"

# Geçici dizin oluştur
TEMP_DIR="$(mktemp -d)"
BUILD_DIR="$TEMP_DIR/$PACKAGE_NAME-$VERSION"
mkdir -p "$BUILD_DIR"

# Dizin yapısını oluştur
mkdir -p "$BUILD_DIR/usr/lib/python3/dist-packages/"
mkdir -p "$BUILD_DIR/DEBIAN"
mkdir -p "$BUILD_DIR/etc/systemd/system/"
mkdir -p "$BUILD_DIR/usr/share/icons/hicolor/128x128/apps/"
mkdir -p "$BUILD_DIR/usr/share/icons/hicolor/scalable/apps/"
mkdir -p "$BUILD_DIR/usr/share/polkit-1/actions/"

# Kaynak dosyaları kopyala
cp -r etap-smartlock "$BUILD_DIR/usr/lib/python3/dist-packages/"
cp -r debian "$BUILD_DIR/DEBIAN"
cp debian/etap-smartlock.service "$BUILD_DIR/etc/systemd/system/"
cp debian/com.etap.smartlock.policy "$BUILD_DIR/usr/share/polkit-1/actions/"
cp debian/e-kilit-mehcan-logo.svg "$BUILD_DIR/usr/share/icons/hicolor/scalable/apps/etap-smartlock.svg"

# postinst dosyasını kopyala ve izinleri ayarla
cp debian/postinst "$BUILD_DIR/DEBIAN/"
chmod 755 "$BUILD_DIR/DEBIAN/postinst"

# Yürütme izinlerini ayarla
chmod 755 "$BUILD_DIR/DEBIAN/postinst" 2>/dev/null || true
chmod 755 "$BUILD_DIR/DEBIAN/prerm" 2>/dev/null || true

# İndirici scripti kopyala
cp installer.sh "$BUILD_DIR/usr/bin/etap-smartlock-installer"
chmod +x "$BUILD_DIR/usr/bin/etap-smartlock-installer"

# Paket oluştur
dpkg-deb --build "$BUILD_DIR" "${PACKAGE_NAME}_${VERSION}_all.deb"

# Release klasörüne taşı
mkdir -p releases
mv "${PACKAGE_NAME}_${VERSION}_all.deb" releases/

# Temizlik
rm -rf "$TEMP_DIR"

echo "Debian paketi oluşturuldu: ${PACKAGE_NAME}_${VERSION}_all.deb"
