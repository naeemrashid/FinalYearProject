# DESCRIPTION:	  Create the atom editor in a container
# AUTHOR:		  Jessie Frazelle <jess@linux.com>
# COMMENTS:
#	This file describes how to build the atom editor
#	in a container with all dependencies installed.
#	Note: atom is not a node-webkit app,
#	found this out a little too late into this example
#	it uses electron(https://github.com/atom/electron)
#	Tested on Debian Jessie.
# USAGE:
#	# Download atom Dockerfile
#	wget https://raw.githubusercontent.com/jessfraz/dockerfiles/master/atom/Dockerfile
#
#	# Build atom image
#	docker build -t atom .
#
#	docker run -v /tmp/.X11-unix:/tmp/.X11-unix \
#		-e DISPLAY=unix$DISPLAY atom
#

# Base docker image
FROM debian:buster
LABEL maintainer "Jessie Frazelle <jess@linux.com>"

# Install dependencies
RUN apt-get update && apt-get install -y \
	git \
	gconf2 \
	gconf-service \
	gvfs-bin \
	libasound2 \
	libcap2 \
	libgconf-2-4 \
	libgnome-keyring-dev \
	libgtk2.0-0 \
	libnotify4 \
	libnss3 \
	libxkbfile1 \
	libxss1 \
	libxtst6 \
	libx11-xcb-dev \
	xdg-utils \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

ENV ATOM_VERSION 1.23.3
RUN buildDeps=' \
		ca-certificates \
		curl \
	' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& curl -L https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom-amd64.deb > /tmp/atom.deb \
	&& rm -rf /var/lib/apt/lists/* \
	&& dpkg -i /tmp/atom-amd64.deb \
	&& rm -rf /tmp/*.deb \
	&& apt-get purge -y --auto-remove $buildDeps

ENV HOME /home/atom
RUN mkdir -p ${HOME} && useradd -m -d ${HOME}  atom
USER atom
WORKDIR atom

# Autorun atom
ENTRYPOINT [ "atom", "--foreground" ]
