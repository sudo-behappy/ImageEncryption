from PIL import Image
from RSA import decrypt
import numpy as np

key = (int(input("first number in private key:")), int(input("second number in private key")))

path = input("encrypted npz file path:")
try:
    img = np.load(path)['arr_0']
except FileNotFoundError:
    exit("Invalid Path")

def batch_decrypt(pixel: np.ndarray, x, y):
    ans = []
    for i in pixel:
        ans.append(decrypt(i, key))
    return np.array(ans)

ans = np.empty(img.shape, dtype=np.uint8)
for x in range(0, len(img)):
    for y in range(0, len(img[x])):
        if y % 10 == 0 and x % 10 == 0:
            ans[x][y] = batch_decrypt(img[x][y], x, y)            
            continue
        ans[x][y] = img[x][y]
try:
    Image.fromarray(ans).save("decrypted.png")
    print("decrypted.png saved")
    Image.fromarray(ans).show()
except Exception:
    print("decryption failed: image corrupted invalid key")

