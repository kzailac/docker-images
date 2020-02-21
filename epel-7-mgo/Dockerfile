FROM centos:centos7
MAINTAINER Themis Zamani themiszamani@gmail.com

# Copy files to docker image
COPY files/etc/yum.conf /etc/
COPY files/etc/rpm/macros.drb /etc/rpm/macros.drb
COPY files/etc/argo.repo /etc/yum.repos.d/argo.repo
COPY files/tmp /tmp
COPY files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
COPY files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
ADD https://raw.githubusercontent.com/kevangel79/jenkins-docker-rpm-builder/feature/DEVOPS-54-packaging-script/pipeline/build-rpm.sh /root/scripts/build-rpm.sh

# Init yum and go
RUN sed -i.original -e 's/^/#/' /etc/yum.repos.d/*.repo
RUN rpm --import /tmp/*.pub && \
    chmod 755 /root/scripts/build-rpm.sh && \
    useradd jenkins && \
    mkdir -p /home/jenkins/workspace/go/src && \
    cp /root/scripts/build-rpm.sh /home/jenkins

# Install Packages
RUN yum clean metadata && yum update && \
    yum install -y gcc \
        perl-ExtUtils-MakeMaker \
        perl-devel \
        perl-IPC-DirQueue \
        tar \
        rpm-build \
        yum-utils \
        apache-maven \
        wget \
        openssh-clients \
        python-pip \
        python-coverage \
        initscripts \
        git \
        pymongo \
        mongodb-org \
        sudo \
        rpmdevtools \
        rpmlint \
        bzr \
        golang && \
    pip install --upgrade pip --ignore-installed six pyparsing && \
    pip install pytest mock pytest-cov && \
    wget https://storage.googleapis.com/golang/go1.10.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.10.linux-amd64.tar.gz

# Install go packages
ENV PATH=/usr/local/go/bin:$PATH GOROOT="/usr/local/go" GOPATH="/home/jenkins/workspace/go"
RUN cd /home/jenkins/workspace/go/src && go get github.com/axw/gocov/... && go get github.com/AlekSi/gocov-xml && go get -u github.com/jstemmer/go-junit-report && \
    cd /home/jenkins/workspace/go/src && go install github.com/axw/gocov/... && go install github.com/AlekSi/gocov-xml && go install github.com/jstemmer/go-junit-report
ENV PATH=/home/jenkins/workspace/go/bin:$PATH
RUN echo 'jenkins ALL=NOPASSWD:/etc/init.d/mongod' > /etc/sudoers && \
    su - jenkins rpmdev-setuptree
