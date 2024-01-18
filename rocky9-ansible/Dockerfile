FROM rockylinux:9

RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
RUN yum -y install \
    python3.11 \
    python3.11-pip
RUN pip3.11 install ansible==9.1.0 ansible-lint==6.22.1
