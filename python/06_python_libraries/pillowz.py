from PIL import image, imagefilter, imageenhance
image = image.open('images.jpg')
print("original image size:", image.size)
resized_image = image.resize(400, 600)
print("resized_image size:", resized_image.size)
resized_image.save("resized_images.jpg")
rotate_image = image.rotate(65)
rotate_image.save("rotate_image.jpg")
rotate_image.show()