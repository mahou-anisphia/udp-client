from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get environment variables
DEFAULT_PORT = int(os.getenv('DEFAULT_PORT'))
MQTT_BROKER = os.getenv('MQTT_BROKER')
MQTT_PORT = int(os.getenv('MQTT_PORT'))
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
