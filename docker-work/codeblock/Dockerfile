FROM ubuntu:14.04
RUN apt-get update && apt-get install -y software-properties-common \
    codeblocks --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
ENV HOME /home/codeblocks
RUN useradd --create-home --home-dir $HOME codeblocks \
        && chown -R codeblocks:codeblocks $HOME \
        && mkdir $HOME/workspace
USER codeblocks
WORKDIR workspace
ENTRYPOINT [ "codeblocks" ]