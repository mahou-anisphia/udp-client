import socket
from converters.udp_package_validator import validate_json
from converters.udp_package_validator import validate_package_format
from converters.mqtt_publisher import publish_message

def start_udp_listener(ip, port, stop_event):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print(f"Listening for messages on {ip}:{port}")

    while not stop_event.is_set():
        sock.settimeout(1)  # Set a timeout to periodically check the stop_event
        try:
            data, addr = sock.recvfrom(1024)
            message = data.decode()
            validate, json_data = validate_json(message)

            if validate:
                if validate_package_format(json_data):
                    publish_message(json_data)
                else:
                    print(f"Invalid package received from {addr}: {message}")
            else:
                print(f"Invalid JSON received from {addr}: {message}")
                # Optionally send a response back

        except socket.timeout:
            continue  # No data received, loop again to check the stop_event

    sock.close()
    print("UDP listener stopped.")
