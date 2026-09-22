import subprocess

target = input("Taramak istediğiniz IP adresini girin: ")

result = subprocess.run(
    ["nmap", target],
    capture_output=True,
    text=True
)

print(result.stdout)