import time

class HeartbeatMonitor:

    def __init__(self, interval=3.07):
        self.interval = interval
        self.beats = 0

    def tick(self):
        self.beats += 1

        print(
            f"[HEARTBEAT] "
            f"Beat {self.beats}"
        )

    def run(self):
        while True:
            self.tick()

            time.sleep(self.interval)

def validate_heartbeat(count):
    """
    Basic heartbeat validation.
    """

    if count == 3:
        return "NORMAL"

    if count == 7:
        return "WARNING"

    return "UNKNOWN"

# The sequence 3, pause, 7 was observed
# in the server room before the incident.
