import base64

Ans = int(input('エンコード:0 , デコード:1\n'))

if Ans == 1:
    b64Str = str(input('デコードしたい文字列を入力してください。\n'))
    txbt = base64.b64decode(b64Str.encode())
    print(txbt.decode())
else:
    b64Str = str(input('エンコードしたい文字列を入力してください。\n'))
    txbt = base64.b64encode(b64Str.encode())
    print(txbt.decode())


#print(base64.b64encode('abcあいうえABC'.encode()))

#ba64ed = 'YWJj44GC44GE44GG44GIQUJD'
#txBy = base64.b64decode(ba64ed.encode())

#print(base64.b64decode(txBy.decode()))


#base64String = 'YWJj44GC44GE44GG44GIQUJD'
#textBytes = base64.b64decode(base64String.encode())
#print(textBytes.decode())
    
#text = '~~~ Hello? ~~~'
#base64Bytes = base64.b64encode(text.encode())

# 結果 fn5+IEhlbGxvPyB+fn4=
#print(base64Bytes.decode())
