from PIL import Image
import numpy as np
from RSA import encrypt

key = (int(input("first number in public key:")), int(input("second number in public key")))



path = input("image pending encrypt path:")
# convert into np array
try:
    img = np.array(Image.open(path))
except FileNotFoundError:
    exit("Invalid Path")

def batch_encrypt(pixel: np.ndarray):
    ans = []
    for i in pixel:
        ans.append(encrypt(i, key))
    return np.array(ans)


ans = np.empty(img.shape)

for x in range(0, len(img)):
    for y in range(0, len(img[x])):
        if y % 10 == 0 and x % 10 == 0:
            ans[x][y] = batch_encrypt(img[x][y])
            continue
        ans[x][y] = img[x][y]
np.savez("encrypted.npz", ans)