from PIL import Image , ImageEnhance, ImageFilter
import os

path1= os.path.abspath('./image_filter/imgs')
pathOut1 = os.path.abspath('./image_filter/editedImgs')

for filename in os.listdir(path1):
    img= Image.open(f"{path1}/{filename}")
    edit= img.filter(ImageFilter.SHARPEN)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name=os.path.splitext(filename)[0]
    edit.save(f'{pathOut1}/{clean_name}.jpg' )
   