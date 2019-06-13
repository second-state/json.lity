with open('tempdir/outputfile') as file:
    s = file.read().strip()
if s.startswith('0x'):
    s = s[2:]

assert len(s) % 64 == 0
b = bytes.fromhex(s)
stringoffset = int.from_bytes(b[:32], 'big', signed=False)
stringlength = int.from_bytes(b[stringoffset:stringoffset + 32],
                              'big',
                              signed=False)
# print(stringoffset)
# print(stringlength)
print(b[stringoffset + 32:stringoffset + 32 + stringlength].decode('utf-8'))
