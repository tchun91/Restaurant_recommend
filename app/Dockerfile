FROM ubuntu:22.04
WORKDIR /app

#No user interaction set
ENV DEBIAN_FRONTEND noninteractive

RUN apt -y update && apt install --no-install-recommends -y \
    build-essential \
#    curl \
    freetds-bin \
    freetds-dev \
    tdsodbc \
    unixodbc \
    unixodbc-dev \
    libsasl2-modules-gssapi-mit \
    libpython3.10-dev \
    python3.10 \
    python3-pip \
    python3.10-dev \
#    unzip \
#    lsof \
#    net-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python development headers
RUN apt-get update && apt-get install -y python3.10-dev

#teletype
ENV DEBIAN_FRONTEND teletype

COPY ./app/src/requirements.txt .

# Upgrade pip and install Python packages
RUN pip3 install --no-cache-dir --upgrade pip && \
    C_INCLUDE_PATH=/usr/include/python3.10 pip install --no-cache-dir -r requirements.txt


RUN pip3 install --no-cache-dir --upgrade pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip install --no-cache-dir -r requirements.txt
#    pip install --no-cache-dir -r requirements.txt && \
#    pip install --no-cache-dir optimum[onnxruntime-gpu]==1.7.0 && \
#    pip install --upgrade protobuf==3.20.2

#ADD https://databricks-bi-artifacts.s3.us-east-2.amazonaws.com/simbaspark-drivers/odbc/2.6.25/SimbaSparkODBC-2.6.25.1043-Debian-64bit.zip /tmp/
#RUN unzip /tmp/SimbaSparkODBC-2.6.25.1043-Debian-64bit.zip -d /tmp/SimbaSparkODBC && \
#    dpkg -i /tmp/SimbaSparkODBC/simbaspark_2.6.25.1043-2_amd64.deb && \
#    rm -rf /tmp/SimbaSparkODBC*

RUN useradd -ms /bin/bash ubuntu
USER ubuntu
WORKDIR /home/ubuntu/

#COPY ./app/src/app01.py ./app/src/app01.pid ./app/src/__init__.py ./app/src/class_loader.py \
#     ./app/src/data_initiation.py ./app/src/gunicorn_config.py ./app/src/init_instance.py \
#     ./app/src/model_loader.py ./app/src/search_class_loader.py ./app/src/words_combiner.py \
#     ./app/src/wsgi.py ./app/newrelic.ini /home/ubuntu/
#COPY ./app/dbxinst.ini ./app/marketing-database-276519-db585df02f3a.json /etc/
COPY ./app \
     /home/ubuntu/app
WORKDIR /home/ubuntu/app/src
EXPOSE 5001

CMD ["newrelic-admin", "run-program", "gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]