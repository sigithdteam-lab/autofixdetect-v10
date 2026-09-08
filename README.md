AutoFixDetect Perbaikan versi sebelumnya 

GNU General Public License v3.0
Copyright (C) 2026 sigithdteam-lab


AutoFixDetect AI adalah alat diagnostik sistem bertenaga AI yang dapat:· ✅ Mendeteksi error secara otomatis dari log sistem· 🧠 Memperbaiki error dengan kecerdasan buatan (AI improvisasi)
· 🌐 Mencari solusi dari internet (Stack Overflow, GitHub, dll)
· 📚 Belajar dari pengalaman (self-learning database)
· 🌐 Antarmuka web dengan progress real-time

---

📦 Instalasi & Persiapan

Persyaratan Sistem

· Python 3.6+
· Linux (Debian/Ubuntu/derivat)
· Akses root/sudo (untuk perbaikan sistem)
· Koneksi internet (untuk pencarian solusi)

Instalasi

```bash
# 1. Download file
wget https://your-server/autofixdetect.py
# atau salin manual file ke server

# 2. Beri izin eksekusi
chmod +x autofixdetect.py

# 3. Jalankan (tanpa sudo untuk scan, dengan sudo untuk fix)
sudo python3 autofixdetect.py --web
```

Dependensi

TIDAK PERLU instalasi dependensi eksternal! Semua library yang dibutuhkan sudah ada di Python standard library:

· os, sys, subprocess, json, re, threading
· urllib, ssl, hashlib, socket, datetime

---

🎮 Mode Penggunaan

1. Mode Web Interface (Direkomendasikan)

```bash
sudo python3 autofixdetect.py --web
# atau
sudo python3 autofixdetect.py -w
```

· Buka browser: http://localhost:8080
· Interface interaktif dengan real-time progress
· Tombol: Scan, AI Fix All, Fast Fix, Stop, Clear Logs

2. Mode CLI (Command Line)

```bash
# Tanpa flag → mode CLI interaktif
sudo python3 autofixdetect.py
```

· Menampilkan hasil scan di terminal
· Tanya apakah ingin menjalankan AI fix
· Output detail error dan perbaikan

3. Mode Background

```bash
# Jalankan di background
sudo nohup python3 autofixdetect.py --web > /dev/null 2>&1 &
```

---

⚡ Fitur Lengkap

🔍 1. Diagnostik Sistem

Fitur Deskripsi
Log Scanner Membaca /var/log/syslog, journalctl, kern.log
Service Check Mendeteksi service gagal dengan systemctl --failed
Resource Monitor Cek memory usage >90%, disk usage >90%
Error Pattern 7 kategori error: SYSTEMD, SERVICE, MEMORY, DISK, NETWORK, PACKAGE

🧠 2. AI Improvisation Engine

Fitur Deskripsi
Pattern Matching 50+ error pattern bawaan
Internet Search Stack Overflow, GitHub, DuckDuckGo, Linux Forums
Command Extraction Ekstrak perbaikan dari hasil pencarian
Smart Testing Uji solusi satu per satu sampai berhasil
Self-Learning Simpan solusi berhasil di /var/log/autofixdetect/
Cache System Cache hasil pencarian untuk akses cepat

🌐 3. Web Interface

Fitur Deskripsi
Dashboard Health score, error count, fixes applied
Progress Bar Real-time progress perbaikan
Live Logs Streaming log aktivitas
Error Summary Breakdown error per kategori
SSE (Server-Sent Events) Update real-time tanpa polling

📚 4. Self-Learning Database

```
/var/log/autofixdetect/
├── learning_db.json      # Solusi berhasil/gagal
├── search_cache.json     # Cache pencarian internet
├── error_patterns.json   # Pola error yang dikenali
└── solutions/            # Backup solusi
```

---

📖 Cara Penggunaan Detail

A. Mode Web - Langkah demi Langkah

1️⃣ Start Server

```bash
sudo python3 autofixdetect.py --web
```

Output:

```
╔══════════════════════════════════════════════════════════╗
║    AUTOFIXDETECT AI v10.0 - ULTIMATE FINAL EDITION     ║
╚══════════════════════════════════════════════════════════╝
🌐 Web interface: http://localhost:8080
🧠 AI Improvisation Engine active
   Press Ctrl+C to stop
```

2️⃣ Buka Browser

· Akses http://localhost:8080
· Tampilan dashboard dengan tombol-tombol

3️⃣ Scan System

· Klik "🔍 Scan System"
· AI akan membaca log dan mendeteksi error
· Dashboard terupdate dengan:
  · Health Score
  · Critical Errors
  · Warnings
  · Total Errors

4️⃣ AI Fix All

· Klik "🧠 AI Fix All" untuk perbaikan penuh
· Proses:
  1. AI menganalisis setiap error
  2. Mencari solusi dari database belajar
  3. Jika tidak ada, mencari di internet
  4. Menguji solusi satu per satu
  5. Menerapkan solusi yang berhasil
  6. Mencatat solusi berhasil untuk masa depan

5️⃣ Fast Fix

· Klik "⚡ Fast Fix" untuk perbaikan cepat
· Hanya menggunakan solusi yang sudah diketahui
· Tidak melakukan pencarian internet

6️⃣ Stop & Clear Logs

· "⏹ Stop" menghentikan proses perbaikan
· "🗑 Clear Logs" membersihkan tampilan log

---

B. Mode CLI - Langkah demi Langkah

```bash
sudo python3 autofixdetect.py
```

1️⃣ Scan Otomatis

```bash
🔍 Running AI-powered diagnostic...
✅ Scan complete: 5 errors found
   Critical: 3, Warnings: 2
   SYSTEMD errors: 3
🧠 AI has 47 learned solutions
```

2️⃣ Lihat Hasil

```bash
📊 Results:
  ❤️  Health: 70/100
  📌 Total Errors: 5
  🔴 Critical: 3
  🟡 Warnings: 2

📋 Error Details:
  1. [CRITICAL] SYSTEMD_FAILURE
     Failed to query local AF_VSOCK CID
  2. [CRITICAL] SERVICE_CRASHED
     Service ssh.service failed
  3. [WARNING] MEMORY_HIGH
     Memory usage: 85%
```

3️⃣ Konfirmasi Fix

```bash
Run AI fixes? (y/n): y
```

4️⃣ Proses Fix

```bash
🧠 AI Improvising...
📋 Testing 5 solutions
  🔧 Trying: systemctl daemon-reload... ✅ Success
  🔧 Trying: systemctl restart systemd-logind... ✅ Success
✅ SYSTEMD_FAILURE fixed
❌ SERVICE_CRASHED unresolved
```

5️⃣ Hasil Akhir

```bash
✅ AI fixed 3/5 errors
⚠ 2 errors still need manual intervention
```

---

🏗️ Struktur & Komponen

Arsitektur Kode

```
autofixdetect.py
│
├── 📦 Colors          # Warna terminal
├── 📦 WEB_UI_HTML     # HTML/CSS/JS web interface
├── 📦 ImprovisationEngine
│   ├── 🔍 search_internet()
│   ├── 🧠 improvise_fix()
│   ├── 🔧 try_fix()
│   └── 📚 _load_learning_db()
├── 📦 ProgressTracker # SSE progress tracking
├── 📦 HTTPServer      # Web server built-in
├── 📦 SystemInfo      # Info CPU, memory, disk
├── 📦 ErrorDetector   # Deteksi error dari log
├── 📦 DiagnosticEngine
│   ├── 🔍 run_diagnostic()
│   ├── 📋 _check_logs()
│   └── ⚙️ _check_services()
└── 📦 AutoFixDetectAI # Main application
```

Database Schema

learning_db.json

```json
{
  "successful": {
    "SYSTEMD_FAILURE": [
      {"command": "systemctl daemon-reload", "timestamp": "2026-09-08..."}
    ]
  },
  "failed": {
    "SYSTEMD_FAILURE": [
      {"command": "rm -rf /etc/systemd", "timestamp": "2026-09-08..."}
    ]
  },
  "ai_solutions_count": 47,
  "last_updated": "2026-09-08T10:30:00"
}
```

error_patterns.json

```json
{
  "systemd_af_vsock": {
    "patterns": ["Failed to query local AF_VSOCK CID", ...],
    "severity": "critical",
    "known_fixes": ["systemctl daemon-reload", ...],
    "search_terms": ["AF_VSOCK CID failed systemd fix", ...]
  }
}
```

---

🔧 Troubleshooting

Error: Permission denied

```bash
# Jalankan dengan sudo
sudo python3 autofixdetect.py --web
```

Error: Port 8080 sudah digunakan

```bash
# Ubah port di file (cari port=8080)
# atau matikan proses yang menggunakan port
sudo lsof -i :8080
sudo kill -9 [PID]
```

Error: Tidak bisa membaca log

```bash
# Pastikan user punya akses
sudo usermod -a -G adm $USER
sudo chmod 644 /var/log/syslog
```

Web interface tidak muncul

```bash
# Cek apakah server berjalan
curl http://localhost:8080

# Cek log error
sudo journalctl -u autofixdetect -f
```

AI tidak menemukan solusi

· Pastikan koneksi internet aktif
· Coba jalankan Scan System ulang
· Periksa /var/log/autofixdetect/learning_db.json
· Tambahkan pattern baru di error_patterns.json

Fix tidak berhasil

```bash
# Cek log detail
sudo journalctl -p err -b --no-pager

# Cek status service
systemctl --failed

# Lihat command apa yang dicoba AI
cat /var/log/autofixdetect/learning_db.json | grep failed
```

---

📊 Perbandingan Mode

Fitur Web Mode CLI Mode
Interface Grafis Terminal
Real-time Progress ✅ ❌
Dashboard ✅ ❌
Tombol Interaktif ✅ ❌
Live Logs ✅ ❌
Auto-Fix ✅ ✅ (dengan konfirmasi)
Resource Usage Sedang Rendah
Remote Access ✅ (browser) ❌ (SSH)

---

🎯 Tips & Trik

1. Optimasi Self-Learning

```bash
# Backup database
cp /var/log/autofixdetect/learning_db.json ~/backup/

# Reset database
rm -rf /var/log/autofixdetect/
```

2. Menambah Pattern Custom

Edit /var/log/autofixdetect/error_patterns.json:

```json
{
  "my_custom_error": {
    "patterns": ["MyApp failed to start"],
    "severity": "critical",
    "known_fixes": ["systemctl restart myapp"],
    "search_terms": ["myapp failed to start linux"]
  }
}
```

3. Schedule Auto-Fix

```bash
# Tambahkan ke crontab
sudo crontab -e
# Scan setiap jam
0 * * * * /usr/bin/python3 /path/to/autofixdetect.py --web
```

4. Monitoring

```bash
# Cek status
curl http://localhost:8080/diagnostic -X POST

# Cek progress
curl "http://localhost:8080/fix/progress?thread_id=xxx"
```

---

📝 Ringkasan

Fitur Status
Deteksi Error ✅
AI Improvisasi ✅
Internet Search ✅
Self-Learning ✅
Web Interface ✅
Real-time Progress ✅
No External Dependencies ✅
Cross-Platform ⚠️ Linux Only

---
