FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends git python-pip && \
    pip install -U pip && \
    useradd newgrnetci
RUN pip install pytest pytest-cov mock pymongo mkdocs
