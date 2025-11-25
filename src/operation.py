import random

# -------------------------------
# XOR Encryption / Decryption
# -------------------------------
def xor_operation(pixels, key):
    new_pixels = []
    for pixel in pixels:
        r = pixel[0] ^ key
        g = pixel[1] ^ key
        b = pixel[2] ^ key
        new_pixels.append((r, g, b))
    return new_pixels


# -------------------------------
# ADD / SUBTRACT Encryption
# -------------------------------
def add_operation(pixels, key):
    new_pixels = []
    for pixel in pixels:
        r = (pixel[0] + key) % 256
        g = (pixel[1] + key) % 256
        b = (pixel[2] + key) % 256
        new_pixels.append((r, g, b))
    return new_pixels


# -------------------------------
# PIXEL SWAPPING (shuffle)
# -------------------------------
def swap_pixels(pixels, key):
    random.seed(key)  # same key → same shuffle pattern
    index_list = list(range(len(pixels)))
    random.shuffle(index_list)

    new_pixels = [None] * len(pixels)
    for i, new_index in enumerate(index_list):
        new_pixels[new_index] = pixels[i]

    return new_pixels


# -------------------------------
# REVERSE PIXEL SWAPPING
# -------------------------------
def unswap_pixels(pixels, key):
    random.seed(key)
    index_list = list(range(len(pixels)))
    random.shuffle(index_list)

    original_pixels = [None] * len(pixels)

    for i, new_index in enumerate(index_list):
        original_pixels[i] = pixels[new_index]

    return original_pixels
