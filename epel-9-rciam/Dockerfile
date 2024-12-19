FROM rockylinux/rockylinux:9

ADD epel-9-rciam/files/tmp /tmp
RUN rpm --import /tmp/*.pub
RUN yum clean all
RUN yum -y install \ 
    openssh-clients \
    epel-release \
    sudo \ 
    git 
RUN yum makecache && yum -y install \
    python3-pip \
    python3-devel \
    python3-requests \
    python3-setuptools \
    python3-isodate \
    python3-rdflib \
    python3-selenium \
    rpmdevtools  \
    rpmlint \
    rpm-build \
    which \
    wget
RUN yum -y group install "Development Tools"
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
RUN su - jenkins rpmdev-setuptree
