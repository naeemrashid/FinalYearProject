FROM debian:jessie
RUN apt-get update && apt-get install -y \
    kicad-common \
    libc6 \
    libcairo2 \
    libgcc1 \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libgomp1 \
    libpython2.7 \
    libstdc++6 \
    libglib2.0-0 \
    libgtk2.0-0 \
    kicad \
    kicad-doc-en \
    --no-install-recommends \
    && rm -rf rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "kicad" ]
