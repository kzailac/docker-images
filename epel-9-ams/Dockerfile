FROM rockylinux/rockylinux:9
ADD epel-9-ams/files/tmp /tmp
RUN yum clean all
RUN yum -y install \
    epel-release
RUN yum -y install openssh
RUN yum makecache
RUN yum install -y rpmdevtools rpmlint rpm-build
RUN yum -y install \
    python-pip \
    python-requests \
    python-devel \
    which \
    perl-devel \
    perl-ExtUtils-MakeMaker
RUN yum install -y sudo
RUN yum install -y git
RUN dnf install -y epel-release
RUN yum -y install \
    gcc \
    zlib zlib-devel lzma xz-devel \
    openssl-devel ncurses-devel bzip2-devel \
    readline-devel libffi-devel sqlite-devel
RUN yum -y group install "Development Tools"
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
ADD epel-9-ams/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
ADD epel-9-ams/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
ADD epel-9-ams/files/scripts/pyenv.sh /home/jenkins/
RUN pip3 install -U pip setuptools
RUN pip3 install mock httmock tox-current-env requests pytest coverage unittest-xml-reporting aiofiles lxml unidecode
RUN dnf -y install python3-devel python3-setuptools python3-requests python3.11-devel python3.11-setuptools python3.11-requests
RUN dnf -y install mock bc
RUN useradd mockbuild
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
USER jenkins
WORKDIR /home/jenkins
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV HOME /home/jenkins
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install 3.7.15 \
    && pyenv install 3.8.15 \
    && pyenv install 3.9.15 \
    && pyenv install 3.10 \
    && pyenv install 3.11
RUN pyenv rehash
RUN pip3 install scons
USER root
WORKDIR /
RUN su - jenkins rpmdev-setuptree
