FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /pdf_summary
WORKDIR /pdf_summary
COPY . /pdf_summary/
RUN pip install -r requirements.txt
