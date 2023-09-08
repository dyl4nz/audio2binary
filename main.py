# import modules
import tkinter as tk
from tkinter import filedialog
import os

# defines mp3-binary function

def convert_mp3_to_binary():

    # Prompts to open file 
    input_mp3_file = filedialog.askopenfilename(
        title="Select an MP3 file",
        filetypes=[("MP3 Files", "*.mp3")],
    )

    # No input error
    if not input_mp3_file:
        print("File selection canceled.")
        return

    
    output_folder = filedialog.askdirectory(title="Select an output folder")

    # No output error catching 
    if not output_folder:
        print("Output folder selection canceled.")
        return

    # Open and read mp3 data
    with open(input_mp3_file, "rb") as mp3_file:
        mp3_binary = mp3_file.read()

    # Output path
    output_binary_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_mp3_file))[0] + ".bin")

    # Save the binary data to the output file
    with open(output_binary_file, "wb") as binary_file:
        binary_file.write(mp3_binary)

    print(f"MP3 file '{input_mp3_file}' converted to binary file '{output_binary_file}'.")


# definsed binary-mp3 function
def convert_binary_to_mp3():
    # prompts to choose the binary file
    binary_file = filedialog.askopenfilename(
        title="Select a binary file",
        filetypes=[("Binary Files", "*.bin")],
    )

    # Check if file isnt binary
    if not binary_file:
        print("File selection canceled.")
        return

    # prompts to choose the output folder 
    output_folder = filedialog.askdirectory(title="Select an output folder")

    # Check if folder selection is cancelled
    if not output_folder:
        print("Output folder selection canceled.")
        return

    # Read the bin data from the file
    with open(binary_file, "rb") as file:
        binary_data = file.read()

    # Define the output path
    output_mp3_file = os.path.join(output_folder, os.path.splitext(os.path.basename(binary_file))[0] + ".mp3")

    # Save as mp3
    with open(output_mp3_file, "wb") as mp3_file:
        mp3_file.write(binary_data)

    print(f"Binary file '{binary_file}' converted to MP3 file '{output_mp3_file}'.")

# Create a tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Ask the user whether to convert MP3 to binary or binary to MP3
choice = input("Enter '1' to convert MP3 to binary or '2' to convert binary to MP3: ")

if choice == '1':
    convert_mp3_to_binary()
elif choice == '2':
    convert_binary_to_mp3()
else:
    print("Invalid choice. Please enter '1' or '2'.")

# Close the tkinter root window
root.destroy()
