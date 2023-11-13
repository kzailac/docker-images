FROM rockylinux/rockylinux:8
ADD files/tmp /tmp
RUN rpm --import /tmp/*.pub
RUN yum clean all
RUN yum -y install openssh
RUN yum -y install \
    epel-release
RUN yum install -y sudo
RUN yum makecache
RUN yum install -y python3 python3-pip python3-devel
RUN yum -y install \
    python3-pip \
    python3-requests \
    python3-devel \
    which \
    perl-devel \
    perl-ExtUtils-MakeMaker
RUN yum install -y rpmdevtools rpmlint rpm-build
RUN yum install -y git
RUN dnf install -y epel-release
RUN yum -y install \
    gcc \
    zlib zlib-devel xz-devel \
    openssl-devel ncurses-devel bzip2-devel \
    readline-devel libffi-devel sqlite-devel
RUN yum -y group install "Development Tools"
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
ADD files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
ADD files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
ADD files/scripts/pyenv.sh /home/jenkins/
RUN pip3 install -U pip setuptools
RUN pip3 install mock httmock tox-current-env requests pytest coverage unittest-xml-reporting aiofiles lxml unidecode
RUN dnf -y install python38-devel python38-setuptools python38-requests python39-devel python39-setuptools python39-requests python3.11-devel python3.11-setuptools python3.11-requests
RUN dnf -y install mock bc
RUN useradd mockbuild
USER jenkins
WORKDIR /home/jenkins
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV HOME  /home/jenkins
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install 3.7.15 \
    && pyenv install 3.8.15 \
    && pyenv install 3.9.15 \
    && pyenv install 3.10 \
    && pyenv install 3.11
RUN pyenv global 3.7.15
RUN pyenv rehash
RUN pip3 install scons
USER root
WORKDIR /
RUN su - jenkins rpmdev-setuptree
