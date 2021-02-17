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
        python3 \
        openssl \
        checksec \
        initscripts \
        git \
        pymongo \
        mongodb-org \
        sudo \
        rpmdevtools \
        rpmlint \
        bzr && \
    pip install --upgrade pip==20.1.1 --ignore-installed six pyparsing && \
    pip install pytest mock pytest-cov && \
    wget https://storage.googleapis.com/golang/go1.15.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.15.linux-amd64.tar.gz

# Install go packages
ENV PATH=/usr/local/go/bin:$PATH GOROOT="/usr/local/go" GOPATH="/home/jenkins/workspace/go"
RUN cd /home/jenkins/workspace/go/src && go get github.com/axw/gocov/... && go get github.com/AlekSi/gocov-xml && go get -u github.com/jstemmer/go-junit-report && \
    cd /home/jenkins/workspace/go/src && go install github.com/axw/gocov/... && go install github.com/AlekSi/gocov-xml && go install github.com/jstemmer/go-junit-report
ENV PATH=/home/jenkins/workspace/go/bin:$PATH
RUN echo 'jenkins ALL=NOPASSWD:/etc/init.d/mongod' > /etc/sudoers && \
    su - jenkins rpmdev-setuptree
