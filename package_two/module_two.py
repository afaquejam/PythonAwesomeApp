import requests
from requests.exceptions import RequestException
import json

from package_two.errors import PublicIPAddressError

class PublicIPAddress(object):
    def __init__(self):
        self.ip_address = None
        self.ip_address_service_url = "https://api.ipify.org?format=json"

    def get_public_ip_address(self):
        try:
            http_response = requests.get(self.ip_address_service_url)
            
            if http_response.status_code != 200:
                raise PublicIPAddressError("HTTP Response Code: {}".format(http_response.status_code))
        except (RequestException, PublicIPAddressError) as http_exception:
            raise PublicIPAddressError(http_exception)
        
        self.parse_and_save_ip_address(http_response.text)
        
    
    def parse_and_save_ip_address(self, ip_address_response):
        self.ip_address = json.loads(ip_address_response)["ip"]
        
    def print_public_ip_address(self):
        print("Your public IP address is {}.".format(self.ip_address))
