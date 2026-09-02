import subprocess
import sys


def get_wifi_profiles():
    """Return a list of saved WiFi profile names on Windows."""
    output = subprocess.check_output(
        "netsh wlan show profiles",
        shell=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    profiles = []
    for line in output.splitlines():
        if "All User Profile" in line:
            name = line.split(":", 1)[1].strip()
            if name:
                profiles.append(name)
    return profiles


def get_wifi_password(profile_name):
    """Return the full netsh output for a WiFi profile (includes password)."""
    return subprocess.check_output(
        f'netsh wlan show profile "{profile_name}" key=clear',
        shell=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def extract_password(profile_output):
    """Extract the Key Content (password) from netsh profile output."""
    for line in profile_output.splitlines():
        if "Key Content" in line:
            return line.split(":", 1)[1].strip()
    return None


def main():
    if sys.platform != "win32":
        print("This tool only works on Windows.")
        sys.exit(1)

    try:
        names = get_wifi_profiles()
    except subprocess.CalledProcessError:
        print("Failed to retrieve WiFi profiles. Make sure WiFi is enabled.")
        sys.exit(1)

    if not names:
        print("No saved WiFi profiles found.")
        sys.exit(0)

    for i, name in enumerate(names, 1):
        print(f"[{i}] {name}")

    try:
        choice = int(input("\nChoose WiFi number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

    if choice < 1 or choice > len(names):
        print(f"Please choose a number between 1 and {len(names)}.")
        sys.exit(1)

    wifi = names[choice - 1]

    try:
        result = get_wifi_password(wifi)
    except subprocess.CalledProcessError:
        print(f"Failed to retrieve details for '{wifi}'.")
        sys.exit(1)

    print("\n" + result)


if __name__ == "__main__":
    main()
