FROM python:latest
LABEL maintainer="github.com/asabhi6776"


WORKDIR /code
COPY . /code/.
RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
EXPOSE 5000