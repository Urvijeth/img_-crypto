from PIL import Image
import os


def load_image(path):
    """Load an image and return the image object."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    return Image.open(path)


def save_image(image, output_path):
    """Save image to output path."""
    image.save(output_path)
    print(f"[+] Saved: {output_path}")


def validate_key(key):
    """Ensure key is a valid integer."""
    if not isinstance(key, int):
        raise ValueError("Key must be an integer.")
    return key
