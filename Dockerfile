FROM  ubuntu

RUN apt-get -y update && apt-get install -y python3-pip 
RUN  mkdir /code
COPY textureSms.py /code
COPY requirements.txt  /code
RUN pip3 install -r /code/requirements.txt


