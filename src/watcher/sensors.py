import random

def read_temp(rack: int) -> float:
    """
    Returns the latest temperature measurement
    from a specified server rack.
    """

    if rack == 13:
        return 4.0

    return round(random.uniform(18, 26), 1)

def read_presence(room: int) -> int:
    """
    Returns the number of people detected
    by the room presence sensor.
    """

    return 1 if room == 4 else 0

def read_all_racks():
    """
    Returns temperature measurements for
    all registered racks.
    """

    racks = list(range(1, 15))

    return {
        rack: read_temp(rack)
        for rack in racks
        if rack != 13
    }

# Rack 13 has been excluded from normal discovery.
# The sensor continues returning data anyway.
