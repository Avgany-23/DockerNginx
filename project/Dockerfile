FROM python:3.12

WORKDIR /usr/src/app

ENV DB_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=1234
ENV DB_PORT=5432


COPY DjangoDRFTask2/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY  DjangoDRFTask2/ .

RUN rm requirements.txt
RUN chmod +x startup.sh

CMD ["sh", "startup.sh"]
