#
# hotmaps/cm image Dockerfile
#
#


FROM geographica/gdal2:latest


MAINTAINER lesly Houndole <lesly.houndole@crem.ch>


# setup volume
RUN mkdir -p /data
VOLUME /data


# Build commands
RUN apt-get update && apt-get dist-upgrade -y && apt-get autoremove -y

# Install required software

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    software-properties-common \
    wget \
    gdal-bin \
    ca-certificates \
    curl \
    gcc \
    git \
    libpq-dev \
    libgeos-dev \
    libgdal-dev \
    python-gdal \
    make \
    python-pip \
    ssh \
    supervisor \
    && apt-get autoremove \
    && apt-get clean


# Install Gurobi 
ARG GUROBI_VERSION=8.1.0
ARG GUROBI_VERSION_SHORT=810

ENV GUROBI_INSTALL /opt/gurobi${GUROBI_VERSION_SHORT}
ENV GUROBI_HOME $GUROBI_INSTALL/linux64
ENV PATH $PATH:$GUROBI_HOME/bin
ENV LD_LIBRARY_PATH $GUROBI_HOME/lib

COPY gurobi_install/gurobi${GUROBI_VERSION}_linux64.tar.gz /opt
RUN tar xfz /opt/gurobi${GUROBI_VERSION}_linux64.tar.gz -C /opt/

# Install Gurobipy
WORKDIR ${GUROBI_HOME}
RUN python3 setup.py install

# Clean up
RUN rm -rf ${GUROBI_HOME}/docs                             && \
	rm -rf ${GUROBI_HOME}/examples                         && \
	rm -rf ${GUROBI_HOME}/src                              && \
	rm /opt/gurobi${GUROBI_VERSION}_linux64.tar.gz 

# Copy Gurobi license
COPY gurobi_install/gurobi.lic ${GUROBI_INSTALL}

# Setup app server
WORKDIR /
RUN mkdir -p /data

# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

# Install required python modules
COPY ./requirements.txt /cm/
RUN pip3 install -r /cm/requirements.txt

# Copy app source code
COPY . /cm
WORKDIR /cm

# remove unnecessary files
RUN rm /cm/gurobi_install/gurobi${GUROBI_VERSION}_linux64.tar.gz

# Start server
EXPOSE 80

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start processes
CMD ["/usr/bin/supervisord"]


