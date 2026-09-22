import subprocess
import ipaddress

# Kullanıcıdan hedef IP adresini al
target = input("Taramak istediğiniz IP adresini girin: ")

# IP adresini kontrol et
try:
    ipaddress.ip_address(target)
except ValueError:
    print("Geçersiz IP adresi girdiniz.")
    exit()

# Nmap taramasını başlat
result = subprocess.run(
    ["nmap", "-sV", target],
    capture_output=True,
    text=True
)

# Nmap çıktısını satırlara ayır
lines = result.stdout.splitlines()

# Hedef bilgisi
print("\n========================================")
print("      LOCAL NETWORK SECURITY SCANNER")
print("========================================")

print(f"\nTarget: {target}")

# Host durumunu kontrol et
host_up = False

for line in lines:
    if "Host is up" in line:
        host_up = True
        break

if host_up:
    print("Status: UP")
else:
    print("Status: DOWN")

# Açık portları göster
print("\nOpen Ports:")

found_open_port = False

for line in lines:
    if "/tcp" in line and "open" in line:
        parts = line.split()

        port_protocol = parts[0]
        state = parts[1]
        service = parts[2]

        port, protocol = port_protocol.split("/")

        print(f"\nPort: {port}")
        print(f"Protocol: {protocol.upper()}")
        print(f"State: {state}")
        print(f"Service: {service}")

        found_open_port = True

if not found_open_port:
    print("Açık TCP portu bulunamadı.")

print("\n========================================")
print("          SCAN COMPLETED")
print("========================================")