#!/usr/bin/env python3


import sys


def genin():
    yield '064767aa'
    yield '0000000000000000000000000000000000000000000000000000000000000020'
    with open(sys.argv[1]) as file:
        inputtext = file.read().strip().encode()
    yield '%064x' % len(inputtext)
    for asciicode in inputtext:
        yield '%02x' % asciicode
    rem = (-len(inputtext)) % 32
    yield '00' * rem


sys.stdout.buffer.write(bytes.fromhex(''.join(genin())))
