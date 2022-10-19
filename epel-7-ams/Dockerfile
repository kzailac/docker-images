FROM centos:centos7
MAINTAINER dvrcic@srce.hr
#ADD files/etc/yum.conf /etc/
#RUN sed -i.original -e 's/^/#/' /etc/yum.repos.d/*.repo
#ADD files/etc/rpm/macros.drb /etc/rpm/macros.drb
ADD epel-7-ams/files/tmp /tmp
RUN rpm --import /tmp/*.pub
RUN yum clean all
RUN yum -y install openssh-clients
RUN yum -y install \
    epel-release
RUN yum makecache && yum -y install \
    python27 \
    python-pip \
    python-requests \
    python2-mock \
    python34-devel \
    python34-mock \
    rpmdevtools  \
    rpmlint \
    rpm-build \
    python-devel \
    python2-devel \
    python2-setuptools \
    python34-setuptools \
    python36-devel \
    python36-setuptools \
    which \
    perl-devel \
    perl-ExtUtils-MakeMaker
RUN yum -y install \
    gcc \
    zlib zlib-devel lzma xz-devel \
    openssl-devel ncurses-devel bzip2-devel \
    readline-devel libffi-devel sqlite-devel
RUN yum -y group install "Development Tools"
ADD epel-7-ams/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
ADD epel-7-ams/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
ADD epel-7-ams/files/scripts/pyenv.sh /etc/profile.d/
ADD epel-7-ams/files/etc/argo.repo /etc/yum.repos.d
RUN pip install httmock coverage=='4.5.4' unittest2 discover
RUN pip install -U "pip==20.*" "setuptools<45.0.0" && pip install pipenv
RUN pip3 install -U pip setuptools
RUN pip3 install mock httmock tox requests pytest coverage unittest-xml-reporting aiofiles lxml
RUN yum install -y python3-aiohttp python3-bonsai python3-avro
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
USER jenkins
WORKDIR /home/jenkins
RUN curl https://pyenv.run | bash
RUN source /etc/profile.d/pyenv.sh && pyenv install --list | grep ' 3.7' | tail -n1 | xargs pyenv install
RUN source /etc/profile.d/pyenv.sh && pyenv install --list | grep ' 3.8' | tail -n1 | xargs pyenv install
RUN source /etc/profile.d/pyenv.sh && pyenv install --list | grep ' 3.9' | tail -n1 | xargs pyenv install
RUN su - jenkins rpmdev-setuptree
