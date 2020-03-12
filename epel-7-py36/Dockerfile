FROM centos:centos7

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum --enablerepo=base clean metadata -y
RUN yum update -y
RUN yum install -y python36u \
        python36u-libs \
        python36u-devel \
        python36u-pip

RUN mkdir /home/jenkins
RUN groupadd -g 1000 jenkins
RUN useradd -r -u 1000 -g jenkins -d /home/jenkins jenkins
RUN chown jenkins:jenkins /home/jenkins
USER jenkins
WORKDIR /home/jenkins
