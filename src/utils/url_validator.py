"""
Validates a given URL using regex
Returns:
    bool: True if the URL is valid, False otherwise.
"""
import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Validates a given URL using regex and URL parsing.
    
    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    # Regex pattern to check the general structure of a URL
    url_regex = re.compile(
        r'^(https?|ftp):\/\/'  # Scheme (http, https, or ftp)
        r'((([A-Za-z0-9-]+\.)+[A-Za-z]{2,})|'  # Domain (e.g., example.com)
        r'(\d{1,3}\.){3}\d{1,3})'  # IPv4 (e.g., 192.168.1.1)
        r'(:\d+)?'  # Optional port (e.g., :80)
        r'(\/[^\s]*)?$',  # Optional path (e.g., /path/to/resource)
        re.IGNORECASE
    )

    # Check if the URL matches the regex
    if not url_regex.match(url):
        return False

    # Parse the URL using urlparse
    parsed = urlparse(url)

    # Validate the scheme and netloc (domain/IP)
    if parsed.scheme not in ["http", "https", "ftp"] or not parsed.netloc:
        return False

    # Exclude localhost and empty netloc
    if parsed.netloc in ["localhost", "127.0.0.1", "::1"]:
        return False

    return True
