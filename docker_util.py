import docker

client = docker.from_env()

def build_image(base_image):
    print(f"Building image from {base_image}...")

    dockerfile = f'''
    FROM {base_image}

    RUN apt-get update && \
        apt-get install -y \
            sudo \
            openssh-server \
            vim \
            gnupg

    RUN useradd -m -s /bin/bash newuser && \
        echo 'newuser:password' | chpasswd && \
        adduser newuser sudo

    RUN mkdir /var/run/sshd && \
        echo 'PermitRootLogin no' >> /etc/ssh/sshd_config && \
        echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
        echo 'AllowUsers newuser' >> /etc/ssh/sshd_config

    EXPOSE 22

    CMD ["/usr/sbin/sshd", "-D"]

    '''

    dockerfile_path = "Dockerfile"

    with open(dockerfile_path, "w") as f:
        f.write(dockerfile)

    image, build_logs = client.images.build(path=".", tag="custom_image", rm=True)

    print("Image built successfully.")
    
    return image


def run_container(image,port):
    container = client.containers.run(image, detach=True, ports={"22/tcp": port})
    return container
