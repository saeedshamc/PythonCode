import unittest
from unittest.mock import patch

from main import extract_password, get_wifi_profiles


class TestWifiPasswordViewer(unittest.TestCase):
    def test_extract_password_found(self):
        output = """
    SSID name : HomeNetwork
    Key Content : mypassword123
"""
        self.assertEqual(extract_password(output), "mypassword123")

    def test_extract_password_not_found(self):
        self.assertIsNone(extract_password("SSID name : Guest\n"))

    @patch("main.subprocess.check_output")
    def test_get_wifi_profiles(self, mock_check_output):
        mock_check_output.return_value = """
    All User Profile     : NetworkA
    All User Profile     : NetworkB
"""
        profiles = get_wifi_profiles()
        self.assertEqual(profiles, ["NetworkA", "NetworkB"])


if __name__ == "__main__":
    unittest.main()
