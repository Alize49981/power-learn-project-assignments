import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for URL
    url = input("Please enter the image URL: ")

    try:
        # Create folder if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Send request to fetch image
        response = requests.get(url, timeout=10)

        # Check if request was successful
        response.raise_for_status()

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If URL has no filename
        if not filename:
            filename = "downloaded_image.jpg"

        # File path
        filepath = os.path.join("Fetched_Images", filename)

        # Save image in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    # Handle request errors
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")

    # Handle other errors
    except Exception as e:
        print(f"✗ An error occurred: {e}")

    if os.path.exists(filepath):
        print("Image already exists. Skipping download.")
    return
    if "image" not in response.headers.get("Content-Type", ""):
        print("This URL does not contain an image.")
    return


if __name__ == "__main__":
    main()
