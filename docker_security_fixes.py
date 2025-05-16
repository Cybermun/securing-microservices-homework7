import json
import os

daemon_path = "/etc/docker/daemon.json"
config = {
    "userns-remap": "default",
    "no-new-privileges": True
}

try:
    with open(daemon_path, 'w') as f:
        json.dump(config, f, indent=4)
    print(f"Updated {daemon_path} with security settings.")
except PermissionError:
    print("Permission denied. Run with sudo.")
