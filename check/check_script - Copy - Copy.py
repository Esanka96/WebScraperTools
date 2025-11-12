from PIL import Image, ImageEnhance
import pytesseract
import re
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    image = image.convert('L')  # grayscale
    image = ImageEnhance.Contrast(image).enhance(2)  # increase contrast
    image = image.resize((image.width * 3, image.height * 3), Image.LANCZOS)  # upscale
    return image


def ocr_image(image_path):
    image = Image.open(image_path)
    processed_image = preprocess_image(image)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(processed_image, config=custom_config)
    return text


def process_image(image_path):
    text = ocr_image(image_path)
    numbers = text
    print(numbers)


# === MAIN ===
image_path = 'image.gif'   # Change this to your actual image file

cas_number_list = process_image(image_path)


