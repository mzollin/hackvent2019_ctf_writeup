# Day 01: HV19.01 censored
We got this censored image with a blurred QR code and the hint that "even the preview icon looks clearer"
![](puzzle.jpg)  
I didn't take the hint at first and looked for layers in Gimp, but then got it and used exiftool to extract the thumbnail:

    exiftool -b -ThumbnailImage puzzle.jpg > solution.jpg

This resulted in a tiny thumbnail but with a sharp QR code, which can be enlarged with a good interpolating image editor like IrfanView and scanned:  
![](solution.png)  
The flag is HV19{just-4-PREview!}
