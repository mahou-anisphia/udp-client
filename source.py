import socket

UDP_IP = "0.0.0.0"  # Listen on all interfaces
UDP_PORT = 23304

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for messages on {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message: {data.decode()} from {addr}")
