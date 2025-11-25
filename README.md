#  Simple Image Encryption Tool

![Demo Preview](/mnt/data/ad60f3e8-e900-48d2-b075-75540f0425e8.png)

A lightweight Python application that encrypts and decrypts images using **pixel-level manipulation**. This project is designed for learning cryptography basics, image processing, and simple cybersecurity concepts.

---

##  Features

* **XOR Encryption** — Applies XOR to each RGB channel using a numeric key.
* **Add/Subtract Encryption** — Adds (or subtracts) a numeric key to pixel values.
* **Pixel Swap (Permutation)** — Deterministic pixel shuffle based on a key.
* **Reversible** — Use the same `mode` + `key` to decrypt.

---

##  Project structure

```
img_-crypto/ (your repo)
├── README.md
├── requirements.txt
├── src/
│   └── img_crypto/
│       ├── __init__.py
│       ├── main.py
│       ├── encryptor.py
│       ├── operations.py
│       └── utils.py
└── images/
    ├── sample.jpg
    ├── encrypted.jpg
    └── decrypted.jpg
```

---

##  Requirements

* Python 3.8+
* Pillow
* (optional) numpy

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Quick start (CLI)

Encrypt an image (example):

```bash
python -m img_crypto.main encrypt images/sample.jpg images/encrypted.jpg --key 123 --type xor
```

Decrypt the image (example):

```bash
python -m img_crypto.main decrypt images/encrypted.jpg images/decrypted.jpg --key 123 --type xor
```

**Available modes:** `xor`, `add`, `swap` (you can combine `xor+swap` if you implement it).

---

##  How it works (short)

1. The program loads the image pixel-by-pixel using Pillow.
2. For `xor` and `add`, each R/G/B value is transformed arithmetically.
3. For `swap`, all pixels are shuffled using a deterministic pseudorandom permutation seeded by the key.
4. Decryption reverses the transformation using the same key and mode.

---

## README image preview

The image at the top is a demo preview. To update it, replace `/images/sample.jpg` with your preferred screenshot and update this README accordingly.

---

##  Usage tips

* Always keep a copy of the **original** image before testing.
* Use numeric integer keys (e.g., `123`, `2024`) for predictable behavior.
* Large images will take longer to process; start with a small sample.

---

##  Development notes

* `main.py` parses CLI arguments and forwards to `encryptor.py`.
* `encryptor.py` coordinates loading, calling functions in `operations.py`, and saving results.
* `operations.py` contains `xor_operation`, `add_operation`, `swap_pixels`, and `unswap_pixels`.
* `utils.py` includes simple helpers for loading/saving and key validation.

---


