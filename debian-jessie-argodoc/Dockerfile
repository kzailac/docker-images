FROM debian:jessie

RUN apt-get update && apt-get install -y git python-pip make && \
    pip install -U pip && \
    pip install -Iv setuptools==44.0.0 && \
    useradd -m newgrnetci
RUN pip install pytest \
                pytest-cov mock \
                pymongo \
                mkdocs \
                sphinx \
                sphinx_rtd_theme
