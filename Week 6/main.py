import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the image URL: ").strip()

    try:
        # Directory for saving images
        os.makedirs("Fetched_Images", exist_ok=True)

        # Try fetching the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no valid filename, generate one
        if not filename or "." not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        save_path = os.path.join("Fetched_Images", filename)

        # Save image in binary mode
        with open(save_path, "wb") as file:
            file.write(response.content)

        print(f"✅ Image {filename} successfully downloaded and saved to: {save_path}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error: Could not reach the server.")
    except requests.exceptions.Timeout:
        print("❌ Timeout error: The server took too long to respond.")
    except requests.exceptions.RequestException as err:
        print(f"❌ An error occurred: {err}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_image()
 