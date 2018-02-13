# Run inkscape in a container
#
# docker run -v /tmp/.X11-unix:/tmp/.X11-unix \
#	-v /inkscape/:/workspace \
#	-e DISPLAY=unix$DISPLAY \
#	infoslack/inkscape
#
FROM ubuntu:16.04
LABEL maintainer "Daniel Romero <infoslack@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
	python-software-properties \
	software-properties-common

RUN add-apt-repository ppa:inkscape.dev/stable && \
	apt-get update && apt-get install -y \
        libgl1-mesa-dri \
	    libgl1-mesa-glx \
		inkscape \
		--no-install-recommends \
        && mkdir -p /workspace \
		&& rm -rf /var/lib/apt/lists/*

ENV HOME /home/inkspace
RUN useradd --create-home --home-dir $HOME inkspace \
	&& chown -R inkspace:inkspace $HOME

USER inkspace
WORKDIR inkspace

ENTRYPOINT [ "inkscape" ]
