from PIL import Image
import numpy as np
from RSA import encrypt

key = (int(input("first number in public key:")), int(input("second number in public key")))



path = input("image pending encrypt path:")
# convert into np array
try:
    img = np.array(Image.open(path), dtype = np.uint8)
except FileNotFoundError:
    exit("Invalid Path")


# check if the image has only one channel
# if len(img.shape) < 3:
#     # reshape
#     image = np.expand_dims(img, axis=2)
#     image = np.concatenate((image, image, image), axis=-1)
#     img = image
print(img)
Image.fromarray(img).show()

def batch_encrypt(pixel: np.ndarray):
    ans = []
    if type(pixel) == np.uint8:
        if pixel == 1:
            ans = [255, 255, 255]
        else:
            ans = [0, 0, 0]
    else:
        for i in pixel:
            ans.append(encrypt(i, key))
        # print(ans)
    return np.array(ans)



ans = np.empty(img.shape, dtype=np.uint8)

for x in range(0, len(img)):
    for y in range(0, len(img[x])):
        if y % 10 == 0 and x % 10 == 0:
            ans[x][y] = batch_encrypt(img[x][y])
            continue
        ans[x][y] = img[x][y]
Image.fromarray(ans).show()
np.savez("encrypted.npz", ans)