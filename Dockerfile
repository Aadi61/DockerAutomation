
    FROM debian:latest

    RUN apt-get update &&         apt-get install -y             sudo             openssh-server             vim             gnupg

    RUN useradd -m -s /bin/bash newuser &&         echo 'newuser:password' | chpasswd &&         adduser newuser sudo

    RUN mkdir /var/run/sshd &&         echo 'PermitRootLogin no' >> /etc/ssh/sshd_config &&         echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config &&         echo 'AllowUsers newuser' >> /etc/ssh/sshd_config

    EXPOSE 22

    CMD ["/usr/sbin/sshd", "-D"]

    