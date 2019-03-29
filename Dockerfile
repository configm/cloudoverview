FROM python:3.7
ENTRYPOINT ["python"]
COPY . /app
WORKDIR /app
ENV flask_secret_key _5#y2Lxc;lkcv;xlF4Q8zdssdec]fdd
RUN pip install -r requirements.txt
CMD ["loader.py"]
