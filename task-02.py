from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    # Open the input image
    img = Image.open(input_path).convert("RGB")  # Ensure the image is in RGB mode
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    # Save the encrypted image
    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key=None):
    # Open the encrypted image
    img = Image.open(input_path).convert("RGB")  # Ensure the image is in RGB mode
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    # Save the decrypted image
    img.save(output_path)
    print("Image decrypted successfully!")

# File paths
input_image = r"/home/gowda/PRODIGY_CS-02/input.jpg"
encrypted_image = r"/home/gowda/PRODIGY_CS-02/encrypted_image.jpg"
decrypted_image = r"/home/gowda/PRODIGY_CS-02/decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image)
