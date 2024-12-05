from PIL import Image

# Load the image
image_path = r"C:\Code\andrew-seaford.co.uk\content\posts\programming\python\pil\How To Crop An Image Using Python Image Library (PIL)\s020NT8_product_page_1.png"  # Replace with the path to your image
image = Image.open(image_path)

# Define the cropping box (left, upper, right, lower)
# Adjust these values based on where you want the 100x100 section
left = 10  # X-coordinate of the left edge
top = 90   # Y-coordinate of the top edge
right = left + 95  # X-coordinate of the right edge
bottom = top + 95  # Y-coordinate of the bottom edge

# Crop the image
cropped_image = image.crop((left, top, right, bottom))

# Save the cropped section to a new file
cropped_image.save("cropped_image.png")
print("Cropped image saved as 'cropped_image.png'")
