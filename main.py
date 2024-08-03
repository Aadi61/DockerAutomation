from docker_util import build_image, run_container
from base_images import images_list
from db import insert_container, check_port, remove_container
import random

print("Choose an OS image to pull:")
for i, image in enumerate(images_list):
    print(f"{i+1}. {image}")

image_index = int(input("Enter the image number: "))

image =build_image(images_list[image_index-1])

while True:
    port = random.randint(10000, 20000)
    if not check_port(port):
        break

container = run_container(image, port)

insert_container(container.id, port)

print(f'''
Container {container.id} is running on port {port}.
Run "ssh newuser@<IP ADDRESS> -p {port}" to connect to the container.

Press Enter to stop the container.'''
)

input()

container.stop()

remove_container(port)



