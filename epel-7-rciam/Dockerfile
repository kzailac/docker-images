FROM centos:centos7

ADD epel-7-rciam/files/tmp /tmp
RUN rpm --import /tmp/*.pub
RUN yum clean all
RUN yum -y install \ 
    openssh-clients \
    centos-release-scl \
    epel-release
RUN yum makecache && yum -y install \
    rh-python36-python-pip \
    python27 \
    python-pip \
    python-devel \
    python-requests \
    python2-mock \
    python2-devel \
    python2-setuptools \ 
    python34-devel \
    python34-mock \
    python34-setuptools \
    rpmdevtools  \
    rpmlint \
    rpm-build \
    which \
    wget
RUN wget https://kosjenka.srce.hr/~eimamagi/selenium/RPMS/python3-isodate-0.6.0-1.el7.srce.noarch.rpm --no-check-certificate && yum -y install python3-isodate-0.6.0-1.el7.srce.noarch.rpm
RUN wget https://kosjenka.srce.hr/~eimamagi/selenium/RPMS/python3-rdflib-4.2.1-9.el7.srce.1.noarch.rpm --no-check-certificate && yum -y install python3-rdflib-4.2.1-9.el7.srce.1.noarch.rpm
RUN wget https://kosjenka.srce.hr/~eimamagi/selenium/RPMS/python3-selenium-3.12.0-5.el7.srce.noarch.rpm --no-check-certificate && yum -y install python3-selenium-3.12.0-5.el7.srce.noarch.rpm
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
RUN su - jenkins rpmdev-setuptree

