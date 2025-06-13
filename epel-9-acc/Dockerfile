FROM rockylinux/rockylinux:9
ADD epel-9-ams/files/tmp /tmp
RUN dnf clean all
RUN dnf -y install \
    epel-release
RUN dnf -y install openssh
RUN dnf makecache
RUN dnf install -y rpmdevtools rpmlint rpm-build
RUN dnf -y install \
    python-pip \
    python-requests \
    python-devel \
    which \
    perl-devel \
    perl-ExtUtils-MakeMaker
RUN dnf install -y sudo
RUN dnf install -y git
RUN dnf install -y epel-release
RUN dnf -y install \
    gcc \
    zlib zlib-devel lzma xz-devel \
    openssl-devel ncurses-devel bzip2-devel \
    openldap-devel readline-devel libffi-devel sqlite-devel
RUN dnf -y group install "Development Tools"
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
ADD epel-9-ams/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
ADD epel-9-ams/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
ADD epel-9-ams/files/scripts/pyenv.sh /home/jenkins/
RUN pip3 install -U pip setuptools==69.2.0
RUN pip3 install mock httmock tox-current-env requests pytest coverage unittest-xml-reporting aiofiles lxml unidecode freezegun pyOpenSSL
RUN dnf -y install python3-devel python3-setuptools python3-requests python3.11-devel python3.11-setuptools python3.11-requests python3.12-devel python3.12-setuptools python3.12-requests
RUN dnf -y install mock bc
RUN dnf config-manager --set-enabled crb && dnf install -y \
    perl-generators \
    perl-Config-General \
    perl-Crypt-OpenSSL-RSA \
    perl-Crypt-OpenSSL-X509 \
    perl-Crypt-SMIME \
    perl-DBI \
    perl-ExtUtils-MakeMaker \
    perl-Monitoring-Plugin \
    perl-Monitoring-Plugin \
    perl-No-Worries \
    perl-Test \
    perl-Test-Exception \
    perl-Test-Pod \
    perl-Test-Pod-Coverage \
    perl-TimeDate
RUN python3.9 -m venv /opt/poetry-tool/
RUN sh -c '\
  . /opt/poetry-tool/bin/activate \
  && pip install -U pip \
  && pip install setuptools==69.2.0 \
  && pip install -U poetry'
RUN ln -s /opt/poetry-tool/bin/poetry /usr/local/bin/
RUN useradd mockbuild
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
USER jenkins
WORKDIR /home/jenkins
RUN curl https://pyenv.run | bash
RUN mv $HOME/.pyenv $HOME/pyenv
RUN source $HOME/pyenv.sh && pyenv install --list | grep ' 3.7' | tail -n1 | xargs pyenv install
RUN source $HOME/pyenv.sh && pyenv install --list | grep ' 3.8' | tail -n1 | xargs pyenv install
RUN source $HOME/pyenv.sh && pyenv install --list | grep ' 3.9' | tail -n1 | xargs pyenv install
RUN source $HOME/pyenv.sh && pyenv install --list | grep ' 3.10' | tail -n1 | xargs pyenv install
RUN source $HOME/pyenv.sh && pyenv install --list | grep ' 3.11' | tail -n1 | xargs pyenv install
RUN source $HOME/pyenv.sh && pyenv install --list | grep ' 3.12' | tail -n1 | xargs pyenv install
RUN source $HOME/pyenv.sh && pyenv local system
RUN rm $HOME/.python-version
USER root
WORKDIR /
RUN su - jenkins rpmdev-setuptree
