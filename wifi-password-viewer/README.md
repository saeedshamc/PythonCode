# WiFi Password Viewer

View all saved WiFi profiles and passwords stored on your Windows system using Python.

## How it works

1. Runs `netsh wlan show profiles` to list saved WiFi networks.
2. Prompts you to choose a network by number.
3. Runs `netsh wlan show profile "<name>" key=clear` to display profile details, including the password.

## Requirements

- Python 3.8+
- Windows with WiFi enabled
- Administrator privileges may be required for some profiles

## Usage

```bash
python main.py
```

Example output:

```
[1] HomeNetwork
[2] Office_WiFi

Choose WiFi number: 1

    SSID name : HomeNetwork
    ...
    Key Content : mypassword123
```

## Project structure

```
wifi-password-viewer/
├── main.py
└── README.md
```

## License

This project is part of the [PythonCode](https://github.com/saeedshamc/PythonCode) repository. See the root [LICENSE](../LICENSE) file for details.
