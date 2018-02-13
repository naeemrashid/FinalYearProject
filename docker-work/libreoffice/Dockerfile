FROM ubuntu:14.04
LABEL maintainer "Naeem Rashid <naeemb7070@gmail.com>"

RUN apt-get update && \
apt-get install -y libreoffice-java-common \
libreoffice-base \
libreoffice \
--no-install-recommends \
&& rm -rf /var/lib/apt/lists/* 
ENV HOME /home/libreoffice
RUN useradd --create-home --home-dir $HOME libreoffice \
        && chown -R libreoffice:libreoffice $HOME
USER libreoffice
WORKDIR libreoffice


ENTRYPOINT [ "libreoffice" ]
