from lz78 import *

input_file = "infile.txt"
output_file = "outfile.bin"
recover_file = "refile.txt"

enc_lz = LZ78()
print("encrypt")
enc_lz.encrypt(input_file)
print("save")
enc_lz.save(output_file)


dec_lz = LZ78()
print("open")
dec_lz.open(output_file)
print("decrypt")
dec_lz.decrypt(recover_file)
print("done")