import fix_lines # fix_lines.py
import numpy as np
import os.path
import sys
import zbar

def convert_to_arr(qr_code):
    # zbar requires the image to be 8-bit greyscale 
    grey_qr = qr_code.convert('L')

    return np.array(grey_qr)


if len(sys.argv) != 3:
    print("Invalid arguments, only supply a path to a file:")
    print("  "+sys.argv[0]+" <path to image file> <path to binary out>")

# fix the lines
new_qr = fix_lines.fix_eo_qr(sys.argv[1])

qr_arr = convert_to_arr(new_qr)

# scan the qr code
scanner = zbar.Scanner()
results = scanner.scan(qr_arr)

# there should only be 1 qr code in the scan
bin_data = results[0].data

with open(sys.argv[2], "wb") as bin_file:
    bin_file.write(bin_data)

