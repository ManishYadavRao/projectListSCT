from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = np.array(img, dtype=np.uint16)  # Convert to uint16 to avoid overflow

    # Apply a simple encryption algorithm (e.g., add a key to each pixel value)
    encrypted_pixels = (pixels + key) % 256

    # Convert back to uint8
    encrypted_pixels = encrypted_pixels.astype('uint8')

    # Create a new image from the encrypted pixel array
    encrypted_img = Image.fromarray(encrypted_pixels)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the encrypted image
    encrypted_img.save(output_path)

    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = np.array(img, dtype=np.uint16)  # Convert to uint16 to avoid overflow

    # Apply the decryption algorithm (e.g., subtract the key from each pixel value)
    decrypted_pixels = (pixels - key) % 256

    # Convert back to uint8
    decrypted_pixels = decrypted_pixels.astype('uint8')

    # Create a new image from the decrypted pixel array
    decrypted_img = Image.fromarray(decrypted_pixels)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the decrypted image
    decrypted_img.save(output_path)

    print(f"Decrypted image saved to {output_path}")

# Example usage
if __name__ == "__main__":
    original_image_path = r"C:\Users\manis\Downloads\bulkImages\th (46).jpeg"
    encrypted_image_path = r"C:\path\to\save\encrypted_image.jpeg"
    decrypted_image_path = r"C:\path\to\save\decrypted_image.jpeg"
    encryption_key = 50  # Example key

    encrypt_image(original_image_path, encrypted_image_path, encryption_key)
    decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)

