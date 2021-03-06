from lz78 import *
import sys

binary_file = "encoding.txt"
recover_file = "outfile.txt"

dev_status = False

if not dev_status:
    if len(sys.argv) <= 2:
        print("Too little args")
    else:
        binary_file      = sys.argv[1]
        recover_file     = sys.argv[2]

dec_lz = LZ78()
dec_lz.dev = dev_status
dec_lz.open(binary_file)
dec_lz.decrypt(recover_file)
