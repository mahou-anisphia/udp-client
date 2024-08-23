# UDP Client

This is a basic UDP client that listens for messages and converts them to MQTT.

## Start Command (using Virtual Environment):

To get started, create a virtual environment and activate it:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Then, run the main script:

```bash
python3 main.py
```

## Installation

To install the required packages, use the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Required Packages

The required packages are:

- `paho-mqtt`
- `python-dotenv`

These are listed in the `requirements.txt` file.

## Configuration

You need to create a `.env` file in the root directory of the project with the following format. Replace the sample data with your own configuration:

```plaintext
DEFAULT_PORT=23304
MQTT_BROKER=sample_broker_address
MQTT_PORT=1883
USERNAME=your_username
PASSWORD=your_password
```

Ensure your `.env` file contains valid data to allow the client to connect to the correct MQTT broker and port.
