import unittest
from unittest.mock import MagicMock, patch

from main import get_location


class TestIpLocationFinder(unittest.TestCase):
    @patch("main.requests.get")
    def test_get_location_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "success",
            "country": "United States",
            "regionName": "California",
            "city": "Mountain View",
            "zip": "94043",
            "lat": 37.4056,
            "lon": -122.0775,
            "isp": "Google LLC",
        }
        mock_get.return_value = mock_response

        with patch("builtins.print") as mock_print:
            get_location("8.8.8.8")

        printed = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("United States", printed)
        self.assertIn("Mountain View", printed)
        self.assertIn("Google LLC", printed)

    @patch("main.requests.get")
    def test_get_location_api_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "fail",
            "message": "invalid query",
        }
        mock_get.return_value = mock_response

        with patch("builtins.print") as mock_print:
            get_location("invalid")

        mock_print.assert_called_with("Error:", "invalid query")

    @patch("main.requests.get")
    def test_get_location_connection_failed(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with patch("builtins.print") as mock_print:
            get_location("8.8.8.8")

        mock_print.assert_called_with("Failed to connect to the API.")


if __name__ == "__main__":
    unittest.main()
