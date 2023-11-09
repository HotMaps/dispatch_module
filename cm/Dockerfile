# Use base image
FROM hotmaps/base_cm:latest

# Install CBC solver
RUN apt-get update && apt-get install -y coinor-cbc

# Define environment variables for CBC
ENV CBC_HOME /usr
ENV PATH $PATH:$CBC_HOME

# Install python and the required packages
RUN apt-get install -y python3 python3-pip
COPY ./requirements.txt /cm/
RUN pip3 install -r /cm/requirements.txt

# Copy files of application
COPY . /cm
WORKDIR /cm

RUN chmod u+x /cm/wait-for-it.sh

# Remove unused Gurobi files if they still exist
RUN rm -rf /opt/gurobi* || true
RUN rm -f /cm/gurobi_install/gurobi.lic || true


EXPOSE 80

# Create journal folder
RUN mkdir -p /var/log/supervisor

# Copy the Supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start process
CMD ["/cm/wait-for-it.sh", "rabbit:5672", "--strict", "--timeout=360", "--", "/usr/bin/supervisord"]
