FROM python:3

RUN groupadd -g 1000 jenkins && \
    useradd -m jenkins -u 1000 -g 1000 && pip install pipenv
COPY utils/rpm_version /home/jenkins/rpm_version