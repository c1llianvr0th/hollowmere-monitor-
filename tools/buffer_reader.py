# Experimental buffer inspection utility.
# Abandoned before production.

def inspect_buffer(buffer):

    if not buffer:
        return "EMPTY"

    if len(buffer) < 8:
        return "INCOMPLETE"

    if all(value == 0 for value in buffer):
        return "NULL BUFFER"

    if all(value == 255 for value in buffer):
        return "UNINITIALIZED BUFFER"

    return "UNKNOWN BUFFER"

def describe_device(device):

    print("DEVICE:", device)
    print("STATUS: UNKNOWN")
    print("RESPONSE: RECEIVED")

    # Do not send a second request.
