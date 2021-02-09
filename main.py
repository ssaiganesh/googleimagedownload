from simple_image_download import simple_image_download as simp
query = input('What images are you searching for? ')
n_images = int(input("How many images do you want to download? "))

response = simp.simple_image_download
response().download(query, n_images)