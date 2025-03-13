FROM apache/nifi:1.23.2

USER root
RUN apt-get update

# Install Python3
RUN apt-get install -y python3 python3-pip 

USER root
#To create a folder in nifi for lookup files


RUN mkdir /opt/nifi/py_scripts
COPY ie-python-scripts /opt/nifi/py_scripts
RUN chmod -R 777 /opt/nifi/py_scripts && chown -R nifi:nifi /opt/nifi/py_scripts

RUN mkdir /opt/nifi/Driver
COPY Driver /opt/nifi/Driver
RUN chown -R nifi:nifi /opt/nifi/Driver


USER nifi
