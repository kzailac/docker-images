FROM centos:centos7

RUN useradd jenkins

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum --enablerepo=base clean metadata -y
RUN yum update -y
RUN yum install -y python36u \
        python36u-libs \
        python36u-devel \
        python36u-pip \
        git

RUN  pip3 install --upgrade pip --ignore-installed six pyparsing && \
     pip3 install pytest mock pytest-cov
