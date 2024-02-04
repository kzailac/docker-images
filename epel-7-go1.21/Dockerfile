FROM centos:centos7

# Copy files to docker image
COPY epel-7-mgo/files/etc/yum.conf /etc/
COPY epel-7-mgo/files/etc/rpm/macros.drb /etc/rpm/macros.drb
COPY epel-7-mgo/files/etc/argo.repo /etc/yum.repos.d/argo.repo
COPY epel-7-mgo/files/tmp /tmp
COPY epel-7-mgo/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
COPY epel-7-mgo/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh

# Init yum and go
RUN sed -i.original -e 's/^/#/' /etc/yum.repos.d/*.repo
RUN rpm --import /tmp/*.pub && \
    useradd jenkins && \
    mkdir -p /home/jenkins/workspace/go/src

COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
COPY utils/checksec/checksec.py /home/jenkins/checksec.py

# Install Packages
RUN yum clean metadata && yum update && \
    yum install -y gcc \
        tar \
        rpm-build \
        yum-utils \
        wget \
        openssh-clients \
        python3 \
        openssl \
        checksec \
        initscripts \
        git \
        sudo \
        rpmdevtools \
        rpmlint \
        bzr && \
    wget https://go.dev/dl/go1.21.6.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.21.6.linux-amd64.tar.gz

# Install go packages
ENV PATH=/usr/local/go/bin:$PATH GOROOT="/usr/local/go" GOPATH="/home/jenkins/workspace/go"
WORKDIR /home/jenkins/workspace/go/src
RUN go install github.com/axw/gocov/gocov@v1.1.0 && go install github.com/AlekSi/gocov-xml@v1.1.0 && go install github.com/jstemmer/go-junit-report@v1.0.0
ENV PATH=/home/jenkins/workspace/go/bin:$PATH
RUN su - jenkins rpmdev-setuptree
