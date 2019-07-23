import fix_lines # fix_lines.py
import numpy as np
import os.path
import qrcode
import sys

# EO games use qr version 17
QR_VERSION = 17

if len(sys.argv) != 3:
    print("Invalid arguments, only supply a path to a file:")
    print("  "+sys.argv[0]+"<path to binary input file> <path to image file out>")


# load the binary data
with open(sys.argv[1], 'rb') as bin_file:
    bin_data = bin_file.read()
    for i in range(0, 100):
        qr = qrcode.QRCode(
            version=QR_VERSION, 
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=4,
        )
        qr.add_data(bin_data, optimize=i)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(sys.argv[2]+str(i)+".bmp")

