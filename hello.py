from bleak import discover
import requests
import asyncio

# ASCII Art për të shtuar në mesazhe
ascii_art = """
       ┓      
┓┏┏┓┏┓┏┫┏┓╋╋┏┓
┗┛┗ ┛┗┗┻┗ ┗┗┗┻
"""

async def find_devices():
    try:
        devices = await discover()
        return [(device.address, device.name) for device in devices]
    except Exception as e:
        print(f"Error discovering devices: {e}")
        return []

def get_instagram_username(bluetooth_address):
    try:
        url = f'http://yourserver.com/get_instagram?bluetooth_address={bluetooth_address}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('instagram_username', 'Unknown')
        else:
            print(f"Failed to get Instagram username. Status code: {response.status_code}")
            return 'Error'
    except Exception as e:
        print(f"Error fetching Instagram username: {e}")
        return 'Error'

async def main():
    print(ascii_art)  # Print the ASCII art at the beginning
    print("Searching for Bluetooth devices...")
    devices = await find_devices()
    if not devices:
        print("No devices found.")
        return

    for addr, name in devices:
        print(f"Found Bluetooth device: {name} ({addr})")
        instagram_username = get_instagram_username(addr)
        print(f"Instagram Username for {name} ({addr}): {instagram_username}")

if __name__ == '__main__':
    asyncio.run(main())
