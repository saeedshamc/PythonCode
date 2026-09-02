import requests


def get_location(ip_address):
    """Fetch and print location details for the given IP address."""
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("Failed to connect to the API.")
        return

    data = response.json()

    if data.get("status") != "success":
        print("Error:", data.get("message", "Unknown error"))
        return

    print(f"\nIP Address    : {ip_address}")
    print(f"Country       : {data['country']}")
    print(f"Region        : {data['regionName']}")
    print(f"City          : {data['city']}")
    print(f"ZIP Code      : {data['zip']}")
    print(f"Latitude      : {data['lat']}")
    print(f"Longitude     : {data['lon']}")
    print(f"ISP           : {data['isp']}")


def main():
    ip = input("\nEnter an IP address: ").strip()
    if not ip:
        print("No IP address provided.")
        return
    get_location(ip)


if __name__ == "__main__":
    main()
