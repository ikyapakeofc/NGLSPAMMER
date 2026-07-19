# 🌟🔐🌌 SCRIPT INI DILINDUNGI OLEH ALIEN DARI GALAXY ANDROMEDA 🌌🔐🌟
# 👤 Author: www.instagram.com/@iky.apake
# 🛸 JANGAN COBA-COBA DECRYPT, NANTI DIAMBIL ALIEN! 👽

# ====== ANTI-DEBUG & ANTI-TAMPER (CROSS-PLATFORM) ======
import sys, os, time, random, string, warnings, requests
warnings.filterwarnings("ignore")

try:
    import platform
    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW("🔥 System32/drivers/etc/hosts/config.sys/destroy.exe 🔥")
    else:
        sys.stdout.write("\033]0;🔥 ROOT/SYSTEM/BIN/DESTROY/HAK_WIFI_TETANGGA 🔥\007")
except:
    pass

os.system("cls" if os.name == "nt" else "clear")

# ====== FAKE LOADING BAR ======
print("\033[92m╔══════════════════════════════════════════════╗\033[0m")
print("\033[92m║\033[0m" + "🔥 INISIALISASI SISTEM PERANG DUNIA KE-4 🔥".center(48) + "\033[92m║\033[0m")
print("\033[92m╚══════════════════════════════════════════════╝\033[0m\n")
time.sleep(0.3)

for i in range(101):
    bar = "█" * (i // 5)
    space = "░" * (20 - (i // 5))
    sys.stdout.write(f"\r\033[93m[🔰] Loading alien technology... [{bar}{space}] {i}% \033[0m")
    sys.stdout.flush()
    time.sleep(0.01)
print("\n\033[92m✅ SYSTEM COMPROMISED!\033[0m\n")
time.sleep(0.3)

# ====== MAIN CODE ======
print("🔥" * 25)
print("🔥 NGL SPAMMER - ULTIMATE EDITION 🔥")
print("👤 Author: instagram.com/@iky.apake 👤")
print("🔥" * 25)

ngl_username = input("\n🎯 Masukin username target (tanpa @): ")
message = input("💬 Masukin pesan lo: ")
spam_count = int(input("🔢 Mau kirim berapa kali? "))
max_retry = int(input("🔄 Max retry kalo gagal (rekomendasi 3-5): "))
delay = float(input("⏱️ Delay antar kirim (rekomendasi 0.5-2): "))

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Android 14; Pixel 8 Pro) AppleWebKit/537.36 Chrome/120.0.6099.144 Mobile Safari/537.36",
]

print(f"\n🔥 MULAI SPAM KE @{ngl_username} 🔥\n")

success = 0
failed_total = 0

for i in range(1, spam_count + 1):
    retry_count = 0
    sent = False
    
    while retry_count <= max_retry and not sent:
        device_id = ''.join(random.choices(string.hexdigits.lower(), k=24))
        user_agent = random.choice(user_agents)
        
        headers = {
            "User-Agent": user_agent,
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Origin": "https://ngl.link",
            "Referer": f"https://ngl.link/{ngl_username}",
        }
        
        payload = {
            "username": ngl_username,
            "question": message,
            "deviceId": device_id,
            "gameSlug": "",
            "referrer": ""
        }
        
        try:
            response = requests.post("https://ngl.link/api/submit", json=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                success += 1
                sent = True
                print(f"✅ [{i}/{spam_count}] Berhasil! 🎉")
            else:
                retry_count += 1
                if retry_count <= max_retry:
                    print(f"🔄 [{i}/{spam_count}] Retry {retry_count}/{max_retry}")
                    time.sleep(1)
                else:
                    failed_total += 1
                    print(f"❌ [{i}/{spam_count}] Gagal!")
        except:
            retry_count += 1
            if retry_count <= max_retry:
                print(f"🔄 [{i}/{spam_count}] Retry {retry_count}/{max_retry}")
                time.sleep(1)
            else:
                failed_total += 1
                print(f"💀 [{i}/{spam_count}] Error!")
    
    if i < spam_count:
        time.sleep(delay)

print("\n" + "🎉" * 20)
print(f"🏆 Berhasil: {success} ✅")
print(f"💩 Gagal: {failed_total} ❌")
print(f"📊 Success rate: {(success/spam_count)*100:.1f}%")
print("👤 Author: instagram.com/@iky.apake 👤")
print("🎉" * 20)

# ====== ANTI-DECODE TRAP DENGAN EMOJI ======
# 🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️🛡️
# 😈 WARNING: AREA TERLARANG! MONITORED BY CIA, FBI, KGB, NASA, PSSI 😈
# 👽 KALO LO BACA INI, ARTINYA LO ADALAH ALIEN YANG SEDANG MENGINVASI BUMI 👽
# 🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗🦗
# 💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
# 🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭🎭
# 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡
# 🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️🗑️