import socket
import subprocess

print("=== NETWORK TROUBLESHOOTING TOOLKIT ===\n")

# Hostname
hostname = socket.gethostname()
print(f"Hostname: {hostname}")

# IP Address
ip = socket.gethostbyname(hostname)
print(f"Local IP Address: {ip}\n")

# Ping Test
website = input("Enter website to ping (example: google.com): ")

print(f"\nPinging {website}...\n")

response = subprocess.run(
    ["ping", "-c", "4", website],
    capture_output=True,
    text=True
)

print(response.stdout)