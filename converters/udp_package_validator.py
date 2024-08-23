import json

def validate_json(data):
    try:
        decoded = json.loads(data)
        return True, decoded
    except json.JSONDecodeError:
        return False, None

def validate_package_format(json_data):
    if "topic" in json_data and "msg" in json_data:
        return True
    else:
        return False
