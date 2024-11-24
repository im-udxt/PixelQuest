from PIL import Image

# Open the image
img = Image.open("assets/Logo.png")

# Remove the ICC profile
img.save("assets/Logo1.png", icc_profile=None)
