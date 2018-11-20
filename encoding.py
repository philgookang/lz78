from lz78 import *
import sys

input_file = "infile.txt"
binary_file = "encoding.txt"

dev_status = False

if not dev_status:
    if len(sys.argv) <= 2:
        print("Too little args")
    else:
        input_file      = sys.argv[1]
        binary_file     = sys.argv[2]

enc_lz = LZ78()
enc_lz.dev = dev_status
enc_lz.encrypt(input_file)
enc_lz.save(binary_file)