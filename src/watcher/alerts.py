ALERT_MESSAGES = {

    "TEMP_HIGH":
        "Temperature exceeded safe threshold.",

    "TEMP_LOW":
        "Temperature below expected threshold.",

    "UNKNOWN_DEVICE":
        "Unregistered device detected.",

    "PRESENCE":
        "Unexpected room occupancy.",

    "HEARTBEAT":
        "Abnormal heartbeat sequence detected.",

}

def generate_alert(code):

    return ALERT_MESSAGES.get(
        code,
        "Unknown monitoring event."
    )

def report(code):

    message = generate_alert(code)

    print(f"[ALERT] {message}")

# Do not acknowledge alerts originating from
# unregistered infrastructure.
