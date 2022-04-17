#  Copyright (c) 2022, Andrea Antonio Perrelli
#  All rigths reserved.

from PIL import Image


def size_of_images():
    image_list = {"28x28", "56x56", "112x112"}
    return image_list


def resize_image(image):
    image_list = size_of_images()
    for image_values in image_list:
        copy_image = image.copy()
        image_values_splitted = image_values.split("x", 2)
        image_value_width = int(image_values_splitted[0])
        image_value_height = int(image_values_splitted[1])
        copy_image.thumbnail((image_value_width, image_value_height))
        copy_image.save(image.filename + image_values_splitted[0] + 'x' + image_values_splitted[1] + '.jpg')

    return image


def show_image(image):
    image.show()


if __name__ == '__main__':
    image_path = 'images/tuturu.png'
    image = Image.open(image_path)
    new_image = resize_image(image)
    show_image(new_image)

