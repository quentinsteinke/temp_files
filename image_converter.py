from PIL import Image
import os

image_path = ".\\convert\\"

print(image_path)

# print(os.listdir(image_path))
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
    pass

for i in images:
    i = image_path + i
    im = Image.open(i)
    con_im = im.convert("RGB")
    con_im.save(im.info("filename") + ".jpg")
