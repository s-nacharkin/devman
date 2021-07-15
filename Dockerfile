FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /django-orm-watching-storage
COPY django-orm-watching-storage/ /django-orm-watching-storage/
RUN pip install -r requirements.txt