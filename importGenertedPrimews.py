# %%
# Importing txt files 
#  For more prime lists: https://www.mathsisfun.com/numbers/prime-number-lists.html

import numpy as np

# %%
# Convert txt files to integers 

#  File_data = np.loadtxt("primes-to-100k.txt", dtype=int)
#  print(File_data)

file_100kprimes = np.loadtxt("primes-to-100k.txt", dtype=int)
print(file_100kprimes)


