from PIL import Image
import numpy as np

def generate_key_image(image_shape, key):
    # Create a key image with the same shape as the original image
    np.random.seed(key)
    key_image = np.random.randint(0, 256, image_shape, dtype=np.uint8)
    return key_image

def encrypt_image(image_path, key):
    # Open the image and convert it to RGB mode
    original_image = Image.open(image_path).convert('RGB')
    
    # Convert the image to a numpy array
    image_array = np.array(original_image)

    # Generate a key image
    key_image = generate_key_image(image_array.shape, key)

    # Encrypt the image by XORing each pixel value with the key image
    encrypted_image_array = image_array ^ key_image

    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_image_array.astype(np.uint8))

    # Save the encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"Image encrypted successfully. Encrypted image saved at: {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image and convert it to RGB mode
    encrypted_image = Image.open(encrypted_image_path).convert('RGB')

    # Convert the encrypted image to a numpy array
    encrypted_image_array = np.array(encrypted_image)

    # Generate a key image
    key_image = generate_key_image(encrypted_image_array.shape, key)

    # Decrypt the image by XORing each pixel value with the key image
    decrypted_image_array = encrypted_image_array ^ key_image

    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_image_array.astype(np.uint8))

    # Save the decrypted image
    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Image decrypted successfully. Decrypted image saved at: {decrypted_image_path}")

def main():
    while True:
        print("Type 'e' for image encryption, 'd' for image decryption, or 'q' to quit.")
        choice = input("Your choice: ")

        if choice == 'e':
            encrypt_choice()
        elif choice == 'd':
            decrypt_choice()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please type 'e' for encryption, 'd' for decryption, or 'q' to quit.")

def encrypt_choice():
    try:
        key = int(input("Enter encryption key (an integer): "))
        image_location = input("Enter the location or URL of the image: ")
        encrypt_image(image_location, key)
    except FileNotFoundError:
        print("Invalid location. Image not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_choice():
    try:
        key = int(input("Enter decryption key (an integer): "))
        encrypted_image_location = input("Enter the location of the encrypted image: ")
        decrypt_image(encrypted_image_location, key)
    except FileNotFoundError:
        print("Invalid location. Encrypted image not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
