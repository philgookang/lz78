from lz78 import *

input_file = "infile2.txt"
output_file = "outfile2.bin"
recover_file = "refile2.txt"

enc_lz = LZ78()
enc_lz.encrypt(input_file)
enc_lz.save(output_file)

print(enc_lz.output)

dec_lz = LZ78()
dec_lz.open(output_file)

print(dec_lz.output)

dec_lz.decrypt(recover_file)