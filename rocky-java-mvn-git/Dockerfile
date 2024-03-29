FROM rockylinux:9

# Install necessary tools
RUN yum install -y git \
    && yum clean all

# Install Java 11
RUN yum install -y java-11-openjdk-devel \
    && yum clean all

# Install Maven 3.9.6
ENV MAVEN_VERSION 3.9.6
ENV MAVEN_HOME /opt/maven
ENV MAVEN_URL https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz

RUN mkdir -p ${MAVEN_HOME} \
    && curl -fsSL -o /tmp/apache-maven.tar.gz ${MAVEN_URL} \
    && tar -xzf /tmp/apache-maven.tar.gz -C ${MAVEN_HOME} --strip-components=1 \
    && rm /tmp/apache-maven.tar.gz \
    && ln -s ${MAVEN_HOME}/bin/mvn /usr/bin/mvn

# Verify installation
RUN java -version
RUN mvn --version

# Set environment variables
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk
ENV PATH $JAVA_HOME/bin:$MAVEN_HOME/bin:$PATH

# Set default working directory
WORKDIR /app

# Start a bash shell by default
CMD ["/bin/bash"]
