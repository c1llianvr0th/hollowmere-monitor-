import time
import random
import yaml

from colorama import Fore, Style

ALERTS = [
    "rack 13 temperature: 4°C (impossible)",
    "heartbeat detected in empty room",
    "badge scan: C.VROTH (deceased?)",
    "disk write: 'help' x 4096",
    "fans stopped. humming continues.",
    "unknown device connected to eth0",
    "room 4 occupancy: 1",
    "monitoring service received an empty response",
]

def load(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def print_status():
    print(Fore.GREEN + "[OK] Monitoring service initialized")
    print(Fore.GREEN + "[OK] Environmental checks enabled")
    print(Fore.GREEN + "[OK] Access logging enabled")

def watch(cfg):
    print_status()

    while True:
        # TODO: remove this. it started writing itself.
        event = random.choice(ALERTS)

        print(Fore.RED + "[WARNING] " + event + Style.RESET_ALL)

        time.sleep(cfg["poll_interval"])

if __name__ == "__main__":
    watch(load())
