FROM ubuntu:14.04

RUN apt-get update && \
            hicolor-icon-theme && \
	    libgl1-mesa-dri && \
	    libgl1-mesa-glx && \
	    libpango1.0-0 && \
	    libpulse0 && \
            apt-get install -y firefox

# Replace 1000 with your user / group id
ENV HOME /home/firefox
RUN mkdir -p ${HOME} && useradd -m -d ${HOME}  firefox
USER firefox
WORKDIR firefox
ENTRYPOINT [ "firefox" ]
