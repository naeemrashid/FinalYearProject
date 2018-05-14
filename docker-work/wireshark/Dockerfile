
FROM ubuntu:16.04


ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
	software-properties-common \
	--no-install-recommends && \
	add-apt-repository ppa:wireshark-dev/stable && \
	apt-get update && \
	apt-get install -y \
	wireshark \
	&& rm -rf /var/lib/apt/lists/*

ENV HOME /home/wireshark
RUN useradd --create-home --home-dir $HOME wireshark \
	&& chown -R wireshark:wireshark $HOME

ENV HOME /home/wireshark
RUN mkdir -p ${HOME} && useradd -m -d ${HOME}  wireshark
USER wireshark
WORKDIR wireshark

ENTRYPOINT	[ "wireshark" ]
