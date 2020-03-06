FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends git python-pip make && \
    pip install -U pip setuptools && \
    useradd newgrnetci
RUN pip install pytest \
                pytest-cov mock \
                pymongo \
                mkdocs \
                sphinx \
                sphinx_rtd_theme
