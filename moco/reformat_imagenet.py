#import moco.unpickle as up
import unpickle as up
from PIL import Image

filename = "/home/tyler/PycharmProjects/val_imagenet_downsampled/val_data"
dir = "/home/tyler/PycharmProjects/train/"
d = up.unpickle(filename)
data = d['data']
n = data.shape[0]
img_size = 64
num_channels = 3
for i in range(n):
    arr = data[i].reshape(img_size,img_size,3,order="F")
    im = Image.fromarray(arr)
    im = im.rotate(270)
    im.save(dir + str(i) + ".jpg")