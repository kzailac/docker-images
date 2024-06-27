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
    python3-mock \
    python3-setuptools \
    rpmdevtools  \
    rpmlint \
    rpm-build \
    which \
    wget
RUN yum -y group install "Development Tools"
RUN wget https://kosjenka.srce.hr/~eimamagi/selenium/RPMS/python3-isodate-0.6.0-1.el7.srce.noarch.rpm --no-check-certificate && yum -y install python3-isodate-0.6.0-1.el7.srce.noarch.rpm
RUN wget https://kosjenka.srce.hr/~eimamagi/selenium/RPMS/python3-rdflib-4.2.1-9.el7.srce.1.noarch.rpm --no-check-certificate && yum -y install python3-rdflib-4.2.1-9.el7.srce.1.noarch.rpm
RUN wget https://kosjenka.srce.hr/~eimamagi/selenium/RPMS/python3-selenium-3.12.0-5.el7.srce.noarch.rpm --no-check-certificate && yum -y install python3-selenium-3.12.0-5.el7.srce.noarch.rpm
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
RUN su - jenkins rpmdev-setuptree
