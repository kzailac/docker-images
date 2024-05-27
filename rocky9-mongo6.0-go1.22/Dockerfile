FROM rockylinux:9

RUN yum update -y && \
    yum install -y wget tar gcc-c++ make git sudo && \
    yum clean all

RUN useradd -ms /bin/bash jenkins \
    && echo 'jenkins ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV GO_SRC=go1.22.3.linux-amd64.tar.gz
ENV GO_URL=https://golang.org/dl/$GO_SRC

RUN mkdir -p /home/jenkins/go
RUN mkdir -p /data/db

RUN wget $GO_URL && \
    tar -C /usr/local -xzf $GO_SRC && \
    rm $GO_SRC

RUN tee /etc/yum.repos.d/mongodb-org-6.0.repo <<EOF
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
EOF

RUN yum install -y mongodb-org && \
    yum clean all

ENV GOPATH=/home/jenkins/go
ENV PATH=$GOPATH/bin:/usr/local/go/bin:$PATH

RUN echo GOPATH=/home/jenkins/go >> /home/jenkins/.bashrc
RUN echo PATH=$GOPATH/bin:/usr/local/go/bin:$PATH >> /home/jenkins/.bashrc

RUN go version

RUN go install github.com/axw/gocov/gocov@latest
RUN go install github.com/AlekSi/gocov-xml@latest
RUN go install github.com/jstemmer/go-junit-report/v2@latest

RUN chown -R jenkins:jenkins /data/db
RUN chown -R jenkins:jenkins /home/jenkins/go
