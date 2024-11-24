from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
import os

root = Tk()
root.geometry("300x200")
root.title("Image Encryptor & Decryptor")


def process_image(mode):
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg;*.png;*.jpeg')])
    if not file_path:
        messagebox.showwarning("Warning", "No file selected.")
        return

    # Custom popup to enter a numeric key with an explanatory note
    key = simpledialog.askstring(
        "Enter Key",
        "Enter a custom numeric key (e.g., 123):\n\nNote: The same key must be used for encryption and decryption."
    )
    if not key:
        messagebox.showerror("Error", "Key is required to proceed.")
        return
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a valid integer.")
        return

    key = int(key)  # Convert the key to an integer

    try:
        with open(file_path, 'rb') as file:
            original_data = bytearray(file.read())  # Read original image data

        # Perform XOR operation for encryption/decryption
        processed_data = bytearray(original_data)  # Make a copy of original data
        for i in range(len(processed_data)):
            processed_data[i] ^= key

        # Validate decryption success
        if mode == "decrypt" and processed_data == original_data:
            messagebox.showerror(
                "Decryption Failed",
                "Incorrect key entered. Please try again with the correct key."
            )
            return

        # Write the modified data back to the file
        with open(file_path, 'wb') as file:
            file.write(processed_data)

        if mode == "decrypt":
            os.startfile(file_path)

        messagebox.showinfo(
            "Success",
            f"Image {mode}ed successfully!\n\nNote: Remember your key for future use."
        )

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def encrypt_image():
    process_image("encrypt")


def decrypt_image():
    process_image("decrypt")


# GUI Components
Label(root, text="Click below to Encrypt or Decrypt").place(x=60, y=50)
Label(root, text="Note: Encrypt or Decrypt same key").place(x=60, y=70)  # Added new label for "dummy"
Button(root, text="Encrypt", command=encrypt_image).place(x=110, y=100)  # Adjusted position
Button(root, text="Decrypt", command=decrypt_image).place(x=110, y=140)  # Adjusted position

root.mainloop()

