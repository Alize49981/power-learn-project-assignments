import requests
response = requests.get("https://en.wikipedia.org/wiki/Motorcycle")
print(f"the elder says : (response.status_code) ")
print(response.text)
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Motorcycle"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text

print("Page Title:", title)
print(response.status_code)

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = "https://en.wikipedia.org/wiki/Motorcycle"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# create folder
folder = "images"
os.makedirs(folder, exist_ok=True)

images = soup.find_all("img")

print(f"Total images found: {len(images)}")

downloaded = 0
max_images = 5   # limit (you can change)

seen_urls = set()

for img in images:
    if downloaded >= max_images:
        break

    img_url = img.get("src")

    if not img_url:
        continue

    # convert relative URL to full URL
    img_url = urljoin(url, img_url)

    # skip duplicates
    if img_url in seen_urls:
        continue
    seen_urls.add(img_url)

    # skip small/icons images
    if "icon" in img_url or "logo" in img_url:
        continue

    try:
        img_data = requests.get(img_url, headers=headers).content

        # skip very small files (likely icons)
        if len(img_data) < 5000:
            continue

        file_name = f"image_{downloaded + 1}.jpg"
        file_path = os.path.join(folder, file_name)

        with open(file_path, "wb") as f:
            f.write(img_data)

        print(f"Downloaded: {file_name}")
        downloaded += 1

    except Exception as e:
        print("Error:", e)

print(f"\nDone! Downloaded {downloaded} images.")

