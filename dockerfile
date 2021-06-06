FROM python:3.6
RUN mkdir -p /work
WORKDIR /work
COPY ./requirements.txt /work
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
RUN pip install -r requirements.txt
COPY main.py /work
CMD ["python", "main.py"]
