FROM python:3.10.0

# Set working directory
RUN mkdir /project

# rwx permissions for everyone
RUN chmod 777 /project

WORKDIR /project

RUN pip install pdm

COPY pyproject.toml ./
COPY pdm.lock ./

RUN pdm install

COPY . .

CMD ["pdm", "run", "python", "src/book/main.py"]