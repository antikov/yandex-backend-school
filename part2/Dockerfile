FROM python

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm requirements.txt

CMD ["python","app.py"]
