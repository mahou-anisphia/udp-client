import paho.mqtt.client as mqtt
from config.settings import MQTT_BROKER, MQTT_PORT, USERNAME, PASSWORD

client = mqtt.Client()

client.username_pw_set(USERNAME, PASSWORD)
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def publish_message(message):
    # Extract the topic and the actual message
    topic = message["topic"]
    msg = message["msg"]
    msg = str(msg)
    # Publish the message using the topic from the validated JSON
    client.loop_start()
    client.publish(topic, msg)
    client.loop_stop()
