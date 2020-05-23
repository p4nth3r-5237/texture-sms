FROM  centos

RUN /bin/sh -c yum install python-pip -y
RUN  mkdir /code
COPY sms.py /code/
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt 
