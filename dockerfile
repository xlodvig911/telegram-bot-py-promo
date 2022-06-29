FROM python:3.10

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/src


COPY . /usr/src/app/
RUN pip install --no-cache-dir -r ../requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
