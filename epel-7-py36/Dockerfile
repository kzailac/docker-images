FROM centos:centos7

COPY epel-7-mgo/files/etc/yum.conf /etc/
COPY epel-7-mgo/files/etc/rpm/macros.drb /etc/rpm/macros.drb
COPY epel-7-mgo/files/etc/argo.repo /etc/yum.repos.d/argo.repo
COPY epel-7-mgo/files/tmp /tmp
COPY epel-7-mgo/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
COPY epel-7-mgo/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh

RUN sed -i.original -e 's/^/#/' /etc/yum.repos.d/*.repo
RUN rpm --import /tmp/*.pub && \
    useradd jenkins

COPY utils/checksec/checksec.py /home/checksec.py

RUN yum clean metadata && yum update
RUN yum install -y python3 \
        python3-devel \
        openssl \
        checksec \
        git

RUN  pip3 install --upgrade pip --ignore-installed six pyparsing && \
     pip3 install pytest mock pytest-cov
