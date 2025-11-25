import sys, os
sys.path.append(os.path.dirname(__file__))

import argparse
from encryptor import encrypt_image, decrypt_image

def main():
    parser = argparse.ArgumentParser(description="Simple Image Encryption Tool")

    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode of operation")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--key", type=int, required=True, help="Encryption key")
    parser.add_argument("--type", choices=["xor", "add", "swap"], required=True, help="Encryption type")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_image(args.input, args.output, args.key, args.type)
    else:
        decrypt_image(args.input, args.output, args.key, args.type)

if __name__ == "__main__":
    main()

