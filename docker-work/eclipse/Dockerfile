FROM ubuntu:14.04
RUN apt-get update && apt-get install -y software-properties-common \
    eclipse --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
#RUN useradd --create-home --home-dir $HOME eclipse \
#        && chown -R eclipse:eclipse $HOME \
#        && mkdir $HOME/workspace
ENV HOME /home/eclipse
RUN mkdir -p ${HOME} && useradd -m -d ${HOME}  eclipse
USER eclipse
WORKDIR eclipse
ENTRYPOINT [ "eclipse","-data","/home/eclipse/workspace" ]
