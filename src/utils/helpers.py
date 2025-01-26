"""Method to generate shorturl and return the json object"""

from datetime import datetime
import shortuuid

def map_shorturl(original_url):
    """Create unique id for unique url.
    If same url is found, return eixting short_id
    """
    pass

# Function to generate a short URL
def generate_short_url(original_url):
    """Validate and return short_id associated for the original_url"""
    short_id = shortuuid.uuid()[:6]
    return {
        "short_id": short_id,
        "original_url": original_url,
        "created_at": datetime.now(),
        "short_url": f"http://localhost:8501/{short_id}",
        "clicks": 0
    }
