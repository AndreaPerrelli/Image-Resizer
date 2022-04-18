#  Copyright (c) 2022, Andrea Antonio Perrelli
#  All rigths reserved.
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys
from  PIL  import Image


def size_of_images():
    image_list = {"28x28", "56x56", "112x112"}
    return image_list


def convert_png_transparent(src_file, dst_file):
    img = cv.imread(src_file, cv.IMREAD_UNCHANGED)
    original = img.copy()

    l = int(max(5, 6))
    u = int(min(6, 6))

    ed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.GaussianBlur(img, (21, 51), 3)
    edges = cv.cvtColor(edges, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(edges, l, u)

    _, thresh = cv.threshold(edges, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    mask = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=4)

    data = mask.tolist()
    sys.setrecursionlimit(10 ** 8)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 255:
                data[i][j] = -1
            else:
                break
        for j in range(len(data[i]) - 1, -1, -1):
            if data[i][j] != 255:
                data[i][j] = -1
            else:
                break
    image = np.array(data)
    image[image != -1] = 255
    image[image == -1] = 0

    mask = np.array(image, np.uint8)

    result = cv.bitwise_and(original, original, mask=mask)
    result[mask == 0] = 255
    cv.imwrite('bg.png', result)

    img = Image.open('bg.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] >= 230 and item[1] >= 230 and item[2] >= 230:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(dst_file, "PNG")
    print ("successfully")
    return img


def resize_image(image_to_resize, dst_file):
    image_list = size_of_images()
    for image_values in image_list:
        copy_image = image_to_resize.copy()
        image_values_splitted = image_values.split("x", 2)
        image_value_width = int(image_values_splitted[0])
        image_value_height = int(image_values_splitted[1])
        copy_image.thumbnail((image_value_width, image_value_height))
        copy_image.save(dst_file + image_values_splitted[0] + 'x' + image_values_splitted[1] + '.png', "PNG")


    print('image resized generated successfully')
    return image_to_resize


def show_image(image):
    image.show()


if __name__ == '__main__':
    const_src_file = 'images/tuturu.png'
    const_dst_file = 'images/tuturu_transparent.png'
    result_transparent_image = convert_png_transparent(const_src_file, const_dst_file)
    new_image = resize_image(result_transparent_image, const_dst_file)
    show_image(new_image)
