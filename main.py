import sys
import threading
import time
from config.settings import DEFAULT_PORT
from converters.udp_listener import start_udp_listener
from converters.mqtt_publisher import client
from logs.log_config import setup_logging

def display_help():
    help_message = """
    Available commands:
    --help            : Show this help message
    q                 : Quit the application
    """
    print(help_message)

def run_udp_listener(ip, port, stop_event):
    start_udp_listener(ip, port, stop_event)

def main():
    setup_logging()

    stop_event = threading.Event()

    # Get port number from user input
    user_input = input(f"Enter port number (default {DEFAULT_PORT}): \n")
    port = int(user_input) if user_input else DEFAULT_PORT

    # Start UDP listener in a separate thread with the stop event
    listener_thread = threading.Thread(target=run_udp_listener, args=("0.0.0.0", port, stop_event))
    listener_thread.start()

    # Main loop for handling user commands
    while True:
        user_command = input("Application running (type '--help' for command options): \n").strip()

        if user_command == '--help':
            display_help()
        elif user_command == 'q':
            print("Quitting the application.")
            client.disconnect()  # Disconnect MQTT client cleanly
            stop_event.set()  # Signal the UDP listener to stop
            listener_thread.join()  # Wait for the listener thread to finish
            sys.exit(0)
        else:
            print("Unknown command. Type '--help' for options.")

if __name__ == "__main__":
    main()
