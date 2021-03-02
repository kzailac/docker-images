FROM centos:centos7

RUN useradd jenkins

ENV JAVA_HOME=/usr/lib/jvm/jre-openjdk
ENV M2_HOME=/opt/maven
ENV MAVEN_HOME=/opt/maven
ENV PATH=${M2_HOME}/bin:${PATH}

RUN yum --enablerepo=base clean metadata -y
RUN yum update -y
RUN yum install -y java-1.8.0-openjdk-devel \
                   wget \
                   git && \
    wget https://www-us.apache.org/dist/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz -P /tmp && \
    tar xf /tmp/apache-maven-3.6.3-bin.tar.gz -C /opt && \
    ln -s /opt/apache-maven-3.6.3 /opt/maven