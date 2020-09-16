# --
# Credit to:
# https://github.com/anibali/docker-pytorch/blob/master/dockerfiles/1.4.0-cuda9.2-ubuntu16.04/Dockerfile
# --
FROM nvidia/cuda:9.2-base-ubuntu16.04

# Basic installs
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    git \
    bzip2 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and switch to it.
# TODO: consider a work-around for this
RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /app
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

# Working directory
WORKDIR /app

ENV HOME=/home/user
ENV PATH=/home/user/miniconda/bin:$PATH

# Conda install
RUN curl -sLo ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh \
 && conda install -y python==3.6.9 \
 && conda clean -ya

# CUDA 9.2-specific steps
RUN conda install -y -c pytorch \
    cudatoolkit=9.2 \
    "pytorch=1.4.0=py3.6_cuda9.2.148_cudnn7.6.3_0" \
    "torchvision=0.5.0=py36_cu92" \
 && conda clean -ya

RUN pip install --upgrade \
    pytest \
    flask \
    pillow \
