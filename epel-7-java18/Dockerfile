FROM centos:centos7

RUN useradd jenkins

RUN yum --enablerepo=base clean metadata -y
RUN yum update -y
RUN yum install -y java-1.8.0-openjdk-devel \
                   maven \
                   git
