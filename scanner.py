import subprocess
import ipaddress


def scan_target(target):
    """
    Verilen IP adresini Nmap ile tarar
    ve sonuçları Flask'ın kullanabileceği
    Python sözlüğü olarak döndürür.
    """

    # IP adresinin geçerli olup olmadığını kontrol et
    try:
        ipaddress.ip_address(target)
    except ValueError:
        return {
            "success": False,
            "error": "Geçersiz IP adresi."
        }

    # Nmap taramasını başlat
    result = subprocess.run(
        ["nmap", "-sV", target],
        capture_output=True,
        text=True
    )

    # Nmap çıktısını satırlara ayır
    lines = result.stdout.splitlines()

    # Hedef bilgisayarın durumunu kontrol et
    host_up = False

    for line in lines:
        if "Host is up" in line:
            host_up = True
            break

    # Açık portları saklamak için liste
    open_ports = []

    for line in lines:

        if "/tcp" in line and "open" in line:

            parts = line.split()

            # Beklenen Nmap formatı:
            # PORT   STATE   SERVICE
            if len(parts) < 3:
                continue

            port_protocol = parts[0]
            state = parts[1]
            service = parts[2]

            # Örnek: 80/tcp
            port, protocol = port_protocol.split("/")

            open_ports.append({
                "port": port,
                "protocol": protocol.upper(),
                "state": state,
                "service": service
            })

    # Tarama sonuçlarını döndür
    return {
        "success": True,
        "target": target,
        "status": "UP" if host_up else "DOWN",
        "open_ports": open_ports
    }
