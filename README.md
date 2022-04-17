Python script to get images in the size needed for Sound Alerts Twitch Extension.
To resize your own image, you need to insert the picture in the 'images' folder
and then modify the path of image in the main.py file with the name of your
current file.

EX  : your name image is 'test.png'
you will first put your image in the 'images' folder and then
substitute 
image_path = 'images/tuturu.png'
with
image_path = 'images/test.png' (line 30)

once you run the script, you will get the images resized generated
in the images folder with the sizes needed.

If you want to use this script for other sizes , you can insert other sizes
by adding elements in the 'image_list' variable defined in the method
size_of_images() of main.py file. (line 10)

Feel free to fork this repo if you want to have a starting point for
manipulating images with python.
