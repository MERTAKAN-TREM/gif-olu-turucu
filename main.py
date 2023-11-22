from PIL import Image

image = ['rick1.jpg', 'rick2.jpg','rick3.jpg','rick4.jpg','rick6.jpg','rick5.jpg']

image_list = [Image.open(file) for file in image]

image_list[0].save('girRick.gif',save_all=True,append_images=image_list[1:],duration=1000,loop=0)
