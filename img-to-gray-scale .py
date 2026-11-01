# Install required package via terminal: --"pip install pillow"--


from PIL import Image
import os

path = "./images.jpeg"  
if not os.path.exists(path):
    raise FileNotFoundError(f"Not found: {os.path.abspath(path)}")

img = Image.open(path)
gray = img.convert("L")
gray.save("./Gray.jpeg")
print("Saved:", os.path.abspath("./Gray.jpeg"))
gray.show()