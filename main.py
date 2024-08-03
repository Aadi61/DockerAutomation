from docker_util import build_image, run_container
from base_images import images_list
from db.docker_db import insert_container, check_port, remove_container
import random

print("Welcome to the Docker container manager.")
print("What would you like to do?")
print("1. Start a new container")

print("Choose an OS image to pull:")
for i, image in enumerate(images_list):
    print(f"{i+1}. {image}")

while True:
    try:
        image_index = int(input("Enter the image number: "))
        if 1 <= image_index <= len(images_list):
            break
        else:
            print("Invalid number. Please choose a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

image =build_image(images_list[image_index-1])

while True:
    port = random.randint(10000, 20000)
    if not check_port(port):
        break

container = run_container(image, port)

insert_container(container.id, port)

print(f'''
Container {container.id} is running on port {port}.
Run "ssh newuser@<IP ADDRESS> -p {port}" to connect to the container. Password is "password".

Press Enter to stop the container.'''
)

input()

container.stop()

remove_container(port)



