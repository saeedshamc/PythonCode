# IP Location Finder

Find the approximate location of any IP address using Python and the [ip-api.com](http://ip-api.com) service.

## How it works

1. Takes an IP address from the user.
2. Sends a request to `http://ip-api.com/json/{ip}`.
3. Displays country, region, city, coordinates, and ISP information.

## Requirements

- Python 3.8+
- [requests](https://pypi.org/project/requests/)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Example:

```
Enter an IP address: 8.8.8.8

IP Address    : 8.8.8.8
Country       : United States
Region        : California
City          : Mountain View
ZIP Code      : 94043
Latitude      : 37.4056
Longitude     : -122.0775
ISP           : Google LLC
```

## Project structure

```
ip-location-finder/
├── main.py
├── requirements.txt
└── README.md
```

## License

This project is part of the [PythonCode](https://github.com/saeedshamc/PythonCode) repository. See the root [LICENSE](../LICENSE) file for details.
