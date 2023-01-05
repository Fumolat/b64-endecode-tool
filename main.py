import base64
import tkinter as tk
import sys

def encode():
    # 入力されたテキストを取得する
    text = input_text.get()
    # テキストをBase64でエンコードする
    encoded_text = base64.b64encode(text.encode()).decode()
    # 結果を出力する
    output_text.set(encoded_text)

def decode():
    # 入力されたテキストを取得する
    text = input_text.get()
    # テキストをBase64でデコードする
    decoded_text = base64.b64decode(text.encode()).decode()
    # 結果を出力する
    output_text.set(decoded_text)

def copy_to_clipboard():
    # 結果をクリップボードにコピーする
    window.clipboard_clear()
    window.clipboard_append(output_text.get())

# ウィンドウを作成する
window = tk.Tk()
window.title("Base64 Encoder/Decoder")
window.geometry("500x350")# ウィンドウサイズ

# 入力用のテキストボックスを作成する
input_text = tk.StringVar()
input_entry = tk.Entry(window, textvariable=input_text, font=("Helvetica",20))
input_entry.pack(expand=True, padx=5, pady=5, fill=tk.BOTH)

# エンコード/デコード用のボタンを作成する
encode_button = tk.Button(window, text="Encode", command=encode, font=("Helvetica",20))
encode_button.pack(side = tk.LEFT, padx=5, pady=5, fill=tk.BOTH)
decode_button = tk.Button(window, text="Decode", command=decode, font=("Helvetica",20))
decode_button.pack(side = tk.RIGHT, padx=5, pady=5, fill=tk.X)

# 結果を表示するラベルを作成する
output_text = tk.StringVar()
output_label = tk.Label(window, textvariable=output_text)
output_label.pack()

# クリップボードにコピーするボタンを作成する
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side = tk.BOTTOM)

# ウィンドウを表示する
window.mainloop()
