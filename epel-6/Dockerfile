FROM centos:centos6

#COPY epel-6/files/etc/yum.conf /etc/
#COPY epel-6/files/etc/rpm/macros.drb /etc/rpm/macros.drb
#COPY epel-6/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
#COPY epel-6/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
#COPY epel-6/files/tmp /tmp
#RUN sed -i.original -e 's/^/#/' /etc/yum.repos.d/*.repo  && \
#    rpm --import /tmp/*.pub
RUN yum clean metadata && yum -y update
RUN yum -y install rpmdevtools rpmlint \
    rpm-build \
    openssh-clients \
    yum-utils 
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm && \
    yum -y install gcc \
    tar && \
    useradd -m jenkins
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
RUN su - jenkins rpmdev-setuptree
