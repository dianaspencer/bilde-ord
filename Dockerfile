FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu16.04
LABEL maintainer="Diana Spencer"

# Basic installs
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    git \
    bzip2 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Default dir to launch commands
WORKDIR /webapp/code

ENV PATH=/root/miniconda/bin:$PATH

# Install miniconda and set python to 3.8
RUN curl -sLo ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod +x ~/miniconda.sh \
    && ~/miniconda.sh -b -p ~/miniconda \
    && rm ~/miniconda.sh \
    && conda install -y python==3.8 \
    && conda clean -ya

COPY ./requirements.txt /webapp/code/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["gunicorn", "-c", "bildeord:create_app()"]