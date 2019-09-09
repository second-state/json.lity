#!/usr/bin/env python3

import sys

with open('tempdir/outputfile') as file:
    s = file.read().strip()
if s.startswith('0x'):
    s = s[2:]

if len(s) % 64 == 0:
    b = bytes.fromhex(s)
    stringoffset = int.from_bytes(b[:32], 'big', signed=False)
    stringlength = int.from_bytes(b[stringoffset:stringoffset + 32],
                                  'big',
                                  signed=False)
    # print(stringoffset)
    # print(stringlength)
    b = b[stringoffset + 32:stringoffset + 32 + stringlength]
    print(b.decode('utf-8'))
else:
    print('An error occurred:')
    print(s)
