import requests
import logging
import time

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Simulated data pipeline health check
def check_data_source(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logging.info("✅ Data source is reachable.")
            return True
        else:
            logging.error(f"❌ Unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        logging.error(f"❌ Error connecting to data source: {e}")
        return False

def validate_data(data):
    if not isinstance(data, dict):
        logging.warning("⚠️ Data is not a dictionary.")
        return False

    if "slideshow" not in data:
        logging.warning("⚠️ Missing 'slideshow' key in data.")
        return False

    slideshow = data["slideshow"]
    if not isinstance(slideshow, dict):
        logging.warning("⚠️ 'slideshow' is not a dictionary.")
        return False

    required_keys = ["title", "author", "slides"]
    for key in required_keys:
        if key not in slideshow:
            logging.warning(f"⚠️ Missing key: '{key}' in slideshow.")
            return False

    if not isinstance(slideshow["slides"], list):
        logging.warning("⚠️ 'slides' is not a list.")
        return False

    logging.info("✅ Data validation passed.")
    return True

def main():
    url = "https://httpbin.org/json"  # Simulating data pipeline endpoint
    logging.info("🔍 Checking data pipeline health...")

    if check_data_source(url):
        try:
            data = requests.get(url).json()
            validate_data(data)
        except Exception as e:
            logging.error(f"❌ Failed to parse JSON: {e}")
    else:
        logging.error("🚨 Health check failed.")

if __name__ == "__main__":
    main()