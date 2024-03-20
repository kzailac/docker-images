FROM centos:centos7
COPY epel-7-perl/files/tmp /tmp
COPY epel-7-perl/files/etc/rpm-repo.conf /root/scripts/rpm-repo.conf
COPY epel-7-perl/files/scripts/scp-upload.sh /root/scripts/scp-upload.sh
RUN rpm --import /tmp/*.pub
RUN yum update; yum clean all
RUN yum -y install openssh-clients openssl
RUN yum -y install \
    centos-release-scl \
    epel-release
RUN yum makecache && yum -y install \
    rpmdevtools  \
    rpmlint \
    rpm-build \
    tar \
    perl \
    perl-devel \
    perl-CPAN \
    perl-Config-General \
    perl-Crypt-OpenSSL-RSA \
    perl-Crypt-OpenSSL-X509 \
    perl-Crypt-SMIME \
    perl-DBI \
    perl-IO-Socket-SSL \
    perl-Messaging-Message \
    perl-Nagios-Plugin \
    perl-No-Worries \
    perl-Test-Exception \
    perl-Test-Pod \
    perl-Test-Pod-Coverage \
    perl-Test-Simple \
    perl-TimeDate \
    perl-YAML \
    perl-Business-ISBN \
    perl-Business-ISBN-Data \
    perl-Class-Accessor \
    perl-Compress-Raw-Bzip2 \
    perl-Compress-Raw-Zlib \
    perl-Config-Tiny \
    perl-Crypt-OpenSSL-Bignum \
    perl-Crypt-OpenSSL-Random \
    perl-Devel-Symdump \
    perl-Digest \
    perl-Digest-MD5 \
    perl-HTTP-Date \
    perl-IO-Compress \
    perl-IO-Socket-IP \
    perl-JSON \
    perl-Math-Calc-Units \
    perl-Module-Implementation \
    perl-Module-Runtime \
    perl-Mozilla-CA \
    perl-Net-Daemon \
    perl-Net-LibIDN \
    perl-Net-SSLeay \
    perl-Params-Validate \
    perl-PlRPC \
    perl-Pod-Coverage \
    perl-Monitoring-Plugin \
    perl-Pod-Parser \
    perl-Sub-Uplevel \
    perl-Sys-Syslog \
    perl-Try-Tiny \
    perl-URI \
    wget
RUN wget http://repo.openfusion.net/centos7-x86_64/perl-IPC-DirQueue-1.0-1.of.el7.noarch.rpm && \
    rpm -Uvh perl-IPC*.rpm && \
    yum -y install perl-IPC-DirQueue
RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000
COPY utils/build-rpm.sh /home/jenkins/build-rpm.sh
RUN su - jenkins rpmdev-setuptree
