from PIL import Image

image = Image.open('code.png')
scanline = image.size[1] / 2
separated = True
for i in range(image.size[0]):
    pixel = image.getpixel((i, scanline))
    hex = '{:02x}'.format(pixel[2])
    if hex == 'ff':
        separated = True
    elif separated:
        separated = False
        print(bytearray.fromhex(hex).decode(), end='')
print('')
