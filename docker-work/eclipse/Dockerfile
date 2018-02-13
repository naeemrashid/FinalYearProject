FROM ubuntu:14.04
RUN apt-get update && apt-get install -y software-properties-common \
    eclipse --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
ENV HOME /home/eclipse
RUN useradd --create-home --home-dir $HOME eclipse \
        && chown -R eclipse:eclipse $HOME
USER eclipse
WORKDIR eclipse
ENTRYPOINT [ "eclipse","-data","/home/eclipse" ]