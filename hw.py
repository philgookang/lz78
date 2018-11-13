from lz78 import *

input_file = "infile.txt"
output_file = "outfile.bin"
recover_file = "refile.txt"

enc_lz = LZ78()
enc_lz.encrypt(input_file)
enc_lz.save(output_file)

dec_lz = LZ78()
dec_lz.open(output_file)
dec_lz.decrypt(recover_file)
