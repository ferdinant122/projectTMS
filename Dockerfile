FROM python:3.8
LABEL maintainer="dimakorp@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app/app.py"]
