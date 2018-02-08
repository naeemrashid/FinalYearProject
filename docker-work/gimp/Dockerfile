# Run gimp in a contianer
#
# docker run -d \
#	-v /etc/localtime:/etc/localtime:ro \
#	-v /tmp/.X11-unix:/tmp/.X11-unix \
#	-e DISPLAY=unix$DISPLAY \
#	-v $HOME/Pictures:/root/Pictures \
#	--name gimp \
#	jess/gimp
#
FROM ubuntu:16.04
LABEL maintainer "Jessie Frazelle <jess@linux.com>"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
        software-properties-common \
	gimp --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*
ENV HOME /home/gimp
RUN useradd --create-home --home-dir $HOME gimp \
        && chown -R gimp:gimp $HOME
USER gimp
WORKDIR gimp

ENTRYPOINT [ "gimp" ]
