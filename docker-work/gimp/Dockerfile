
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
        software-properties-common \
	gimp --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*
ENV HOME /home/gimp
RUN mkdir -p ${HOME} && useradd -m -d ${HOME}  gimp
USER gimp
WORKDIR gimp

ENTRYPOINT [ "gimp" ]
