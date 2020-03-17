FROM centos:6.10
MAINTAINER dvrcic@srce.hr 

COPY epel-6/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
COPY epel-6/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
COPY epel-6/files/tmp /tmp
RUN rpm --import /tmp/*.pub && \
    useradd jenkins
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
RUN yum clean all && yum -y install \ 
    centos-release-scl \
    epel-release \
    openssh-clients
RUN yum makecache && yum -y install \
    rh-python36-python-pip \
    python27 \
    python-pip \
    python-requests \
    python2-mock \ 
    python34-devel \
    python34-mock \
    rpmdevtools  \
    python2-devel \
    python2-setuptools \
    python34-setuptools
RUN pip install httmock coverage=='4.5.4' unittest2 discover 
RUN scl enable python27 'pip install -U pip setuptools'
RUN scl enable python27 'pip install mock httmock coverage tox requests pytest'
RUN scl enable rh-python36 'pip install -U pip setuptools'
RUN scl enable rh-python36 'pip install mock httmock coverage tox requests pytest'
RUN echo 'jenkins ALL=NOPASSWD:/etc/init.d/mongod' > /etc/sudoers && \
    su - jenkins rpmdev-setuptree