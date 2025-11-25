import sys, os
sys.path.append(os.path.dirname(__file__))

from PIL import Image
from .operations import xor_operation, add_operation, swap_pixels, unswap_pixels

def encrypt_image(input_path, output_path, key, enc_type):
    """Encrypt the image based on selected type."""
    image = Image.open(input_path)
    pixels = list(image.getdata())
    width, height = image.size

    if enc_type == "xor":
        pixels = xor_operation(pixels, key)

    elif enc_type == "add":
        pixels = add_operation(pixels, key)

    elif enc_type == "swap":
        pixels = swap_pixels(pixels, key)

    # Save encrypted image
    encrypted_img = Image.new(image.mode, (width, height))
    encrypted_img.putdata(pixels)
    encrypted_img.save(output_path)

    print(f"[+] Image encrypted → {output_path}")


def decrypt_image(input_path, output_path, key, enc_type):
    """Decrypt image using same process reversed."""
    image = Image.open(input_path)
    pixels = list(image.getdata())
    width, height = image.size

    if enc_type == "xor":
        pixels = xor_operation(pixels, key)   # XOR reverses itself

    elif enc_type == "add":
        pixels = add_operation(pixels, -key)  # reverse add → subtract

    elif enc_type == "swap":
        pixels = unswap_pixels(pixels, key)   # reverse shuffle

    # Save decrypted image
    decrypted_img = Image.new(image.mode, (width, height))
    decrypted_img.putdata(pixels)
    decrypted_img.save(output_path)

    print(f"[+] Image decrypted → {output_path}")
