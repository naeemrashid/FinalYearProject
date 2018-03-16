FROM node:6.13.1-wheezy
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    git-core \
    git \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists*
RUN git clone https://github.com/eclipse/orion.client.git \
    && cd orion.client/modules/orionode &&  npm install -y \
    && apt-get purge --auto-remove -y git git-core
EXPOSE 8081
WORKDIR orion.client/modules/orionode
CMD [ "server.js" ]
ENTRYPOINT [ "node" ]
