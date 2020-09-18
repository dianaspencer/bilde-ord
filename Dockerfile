# --
# Credit to:
# https://github.com/anibali/docker-pytorch/blob/master/dockerfiles/1.4.0-cuda9.2-ubuntu16.04/Dockerfile
# --
FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu16.04

# Basic installs
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    git \
    bzip2 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Set work directory which commands will be run by default
WORKDIR /app

# TODO: copy requirements over

ENV PATH=/root/miniconda/bin:$PATH

# Install miniconda and set python to 3.7
RUN curl -sLo ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh \
 && conda install -y python==3.7 \
 && conda clean -ya

# Install python packages
RUN conda install -y -c pytorch \
    cudatoolkit=10.1 \
    torchvision \
    flask \
    pytest \
    typing \
 && conda clean -ya

EXPOSE 5000
# Entry point when the container starts