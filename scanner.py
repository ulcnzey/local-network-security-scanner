import subprocess

target = input("Taramak istediğiniz IP adresini girin: ")

result = subprocess.run(
    ["nmap", "-sV", target],
    capture_output=True,
    text=True
)

lines = result.stdout.splitlines()

print("\nOpen Ports:")

for line in lines:
    if "/tcp" in line and "open" in line:
        parts = line.split()

        port = parts[0]
        state = parts[1]
        service = parts[2]

        print(f"Port: {port}")
        print(f"State: {state}")
        print(f"Service: {service}")
        print()