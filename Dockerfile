FROM python:3.10.0

# Set working directory
RUN mkdir /project

# rwx permissions for everyone
RUN chmod 777 /project

WORKDIR /project

RUN pip install pdm

COPY . .

RUN pdm install

CMD ["pdm", "run", "python", "src/book_watch/main.py"]