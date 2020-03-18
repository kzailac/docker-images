FROM centos:centos6

COPY epel-6/files/etc/yum.conf /etc/
COPY epel-6/files/etc/rpm/macros.drb /etc/rpm/macros.drb
COPY epel-6/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
COPY epel-6/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
COPY epel-6/files/tmp /tmp
RUN sed -i.original -e 's/^/#/' /etc/yum.repos.d/*.repo && \
    rpm --import /tmp/*.pub && \
    useradd -m jenkins
RUN yum clean metadata && yum update && \
    yum -y install rpmdevtools \
    rpm-build \
    epel-release \
    openssh-clients \
    yum-utils \
    gcc
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
RUN su - jenkins rpmdev-setuptree
