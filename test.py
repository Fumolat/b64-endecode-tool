import tkinter as tk
import base64
#import clipboard

def encode(text):
  return base64.b64encode(text.encode()).decode()

def decode(text):
  return base64.b64decode(text.encode()).decode()

# Create the main window
window = tk.Tk()
window.title("Base64 Encoder/Decoder")

# Create the input and output fields
input_field = tk.Text(window)
output_field = tk.Text(window)

# Create the encode and decode buttons
encode_button = tk.Button(window, text="Encode", command=lambda: encode_handler())
decode_button = tk.Button(window, text="Decode", command=lambda: decode_handler())

# Create the copy and paste buttons
copy_button = tk.Button(window, text="Copy", command=lambda: copy_handler())
paste_button = tk.Button(window, text="Paste", command=lambda: paste_handler())

# Create the handler functions for the buttons
def encode_handler():
  input_text = input_field.get("1.0", "end")
  output_text = encode(input_text)
  output_field.delete("1.0", "end")
  output_field.insert("1.0", output_text)

def decode_handler():
  input_text = input_field.get("1.0", "end")
  output_text = decode(input_text)
  output_field.delete("1.0", "end")
  output_field.insert("1.0", output_text)

def copy_handler():
  output_text = output_field.get("1.0", "end")
  clipboard.copy(output_text)

def paste_handler():
  input_text = clipboard.paste()
  input_field.delete("1.0", "end")
  input_field.insert("1.0", input_text)


# Add the widgets to the window and start the application
input_field.pack()
encode_button.pack()
decode_button.pack()
copy_button.pack()
output_field.pack()
window.mainloop()
