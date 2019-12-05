# Day 05: HV19.05 Santa Parcel Tracking
Yes, I really liked this one.  
>To handle the huge load of parcels Santa introduced this year a parcel tracking system. He didn't like the black and white barcode, so he invented a more solemn barcode. Unfortunately the common barcode readers can't read it anymore, it only works with the pimped models santa owns. Can you read the barcode?  

![](code.png)  

The first obvious thing to try is of course to scan the barcode, which gets us the text "Not the solution" and the information that it's a "Code 128" linear barcode. I did analyze the file with binwalk and pngcheck, but I had no high hopes because a barcode should be optically readable to be useful, right?  

My next ideas were that maybe we had to remove bars with a certain color to get a new code or that the colors represented the bar thickness of a hidden barcode. But I looked at the histogram of the image and there were too many discrete color values for any of this to be a likely solution.  

A friend who was also trying to solve the challenge mentioned that he tried mapping the colors to ASCII codes but got nothing useful out of it. But this caught my attention, that seemed like the perfect way to do it. So I opened the image in Gimp and read the hex values of the first few bars. It did not make any sense indeed, but it was all valid ASCII letters or numbers, which couldn't be a coincidence.  

So I wrote a small Python script to extract the colors from the bars in a horizontal scanline from left to right and convert their hex values to ASCII:  
```python
from PIL import Image

image = Image.open('code.png')
scanline = image.size[1] / 2
separated = True
for i in range(image.size[0]):
    pixel = image.getpixel((i, scanline))
    hex = '{:02x}{:02x}{:02x}'.format(*pixel)
    if hex == 'ffffff':
        separated = True
    elif separated:
        separated = False
        print(bytearray.fromhex(hex).decode(), end=' ')
print('')
```  
Which results in the following output:  

    sPX tY8 lPY mEI r1O y3F sP0 eQZ g8P z94 uLS hT8 eGH z0V aX1 g09 lO{ tOD lJ1 gJf xIf zIi gUc jSu iHl iQt v6_ v0t sMo sI_ aQg iI3 e4t wS_ b9a tE_ uGS h4P a8T lN_ qVR cV3 lPa f6d q5e rGr cO} wXS fL1 q00 vV9 eW0 nJO gWM x2Z e3E k20 o3E aS3 lRN tUF y8P vB6 eBE

It may seem like gibberish, but remember, we're still playing a CTF. If you look closely at the blue channel (the third character of the bar values) you can see some underscores and curly braces, which indicate a flag buried in there. So we modify the script to read only the blue channel and string it together, which gives us this:  

    X8YIOF0ZP4S8HV19{D1fficult_to_g3t_a_SPT_R3ader}S1090OMZE0E3NFP6E

And indeed, we got the flag. The final script (spt_reader.py) is available in this repo.  

[Next day](../06)
