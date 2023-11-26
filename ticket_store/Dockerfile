FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /ticket_store
WORKDIR /ticket_store
RUN apt-get update && \
    apt-get install -y locales && \
    echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen
COPY requarements.txt ./
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requarements.txt
COPY ./ ./ticket_store/

EXPOSE 80
CMD /usr/local/bin/gunicorn --config /ticket_store/gunicorn.conf