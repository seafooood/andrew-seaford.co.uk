
import requests
from PIL import Image
from io import BytesIO

def download_png_as_pil(url):
    """
    Downloads a PNG image from the specified URL and returns it as a PIL Image object.

    Args:
        url (str): The URL of the PNG image.

    Returns:
        PIL.Image.Image: A PIL Image object of the downloaded image.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Convert the content of the response into a PIL Image
        image = Image.open(BytesIO(response.content))
        
        # Ensure it's a PNG
        if image.format != 'PNG':
            raise ValueError("The downloaded file is not a PNG image.")
        
        return image
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    image_url = "https://stitching.andrew-seaford.co.uk/wp-content/uploads/2023/09/s020NT8_product_page_1.png"
    pil_image = download_png_as_pil(image_url)

    if pil_image:
        pil_image.show()  # Displays the image
    else:
        print("Failed to download or process the image.")
