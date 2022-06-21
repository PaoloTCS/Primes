# %%
#  Get a copy to cloud storage
#  For lists: https://www.mathsisfun.com/numbers/prime-number-lists.html
import numpy as np

# %%
#  Here we load files, like  primes-to-100k.txt 
PrimeArray = np.array([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]);
IndexArray = np.array([0, 1, 2, 5, 7]) ;  #  ordinal postions of the elements in the list 
ax1len = len(PrimeArray)  # 25 - for number 0f primes less than 100 
x = np.array(np.array(PrimeArray)[IndexArray])
print(np.array(np.array(PrimeArray)[IndexArray]))
print(len(PrimeArray))



# %%
def primeOfPrimes(x):
    return [i for i in x if i < ax1len] 

# %%
primeOfPrimes(PrimeArray)
myPrimeOfPrimes = np.array(primeOfPrimes(PrimeArray))
sx1 = np.array(primeOfPrimes(PrimeArray))
print(PrimeArray)
print(myPrimeOfPrimes) 
print(list(np.array(PrimeArray)[sx1]))  #  [5, 7, 13, 19, 37, 43, 61, 71, 89] the first item s/b 3 (0 based)


# %%
# To fix the index off by one position, I added a 0 to the start of the list 
woof = np.array([0, 2, 3, 5, 7, 11, 13, 17, 19, 23])
# ow use a more adult version
npZeros0 = np.zeros((1))
print(npZeros0)

PP2 = np.insert(myPrimeOfPrimes, 0, npZeros0)
print("Second level primes are: ", list(np.array(PrimeArray)[woof]))    # [2, 5, 7, 13, 19, 37, 43, 61, 71, 89]
print("Indeces are: ", PP2)

# %%
print(PP2)

# %%
print(x)
#  End of file


