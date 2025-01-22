"""Method to generate shorturl and return the json object"""

# Function to generate a short URL
def generate_short_url(original_url):
    short_id = shortuuid.uuid()[:6]
    return {
        "short_id": short_id,
        "original_url": original_url,
        "created_at": datetime.now(),
        "clicks": 0
    }
