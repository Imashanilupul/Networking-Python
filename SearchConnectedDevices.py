import subprocess
import re

def get_connected_devices():
    try:
        # Run the arp command to get connected devices
        result = subprocess.check_output(['arp', '-a'], text=True)

        devices = []
        # Parse the output for IP and MAC addresses
        for line in result.splitlines():
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+.*\s+([0-9a-fA-F:-]{17}|[0-9a-fA-F:-]{12})', line)
            if match:
                ip, mac = match.groups()
                devices.append({'IP Address': ip, 'MAC Address': mac})

        return devices
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

if __name__ == "__main__":
    connected_devices = get_connected_devices()
    if connected_devices:
        print("Connected devices:")
        for device in connected_devices:
            print(f"IP Address: {device['IP Address']}, MAC Address: {device['MAC Address']}")
    else:
        print("No devices found or unable to retrieve devices.")
