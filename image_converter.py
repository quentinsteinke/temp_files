from PIL import Image
import os
"""
This script converts .png image files into .jpg files.
It needs a subfolder named "convert" with the images you want to convert in it.
"""
image_path = ".\\convert\\"
images = os.listdir(image_path)
new_name = "Converted"

print("Change name? y/n: ")
convert_name = input()

if convert_name == "y":
    print("New file name: ")
    new_name = input()
    num = 1

    for i in images:
        i = image_path + i
        im = Image.open(i)
        con_im = im.convert("RGB")
        con_im.save(new_name + "_" + str(num) + ".jpg")
        num += 1

if convert_name == "n":
    for i in images:
        i = image_path + i
        im = Image.open(i)
        original_name = im.filename
        original_name = original_name.replace(image_path, "")
        original_name = original_name.replace(".png", "")
        con_im = im.convert("RGB")
        con_im.save(original_name + ".jpg")

print("All done!")
