FROM python:3.12-slim

WORKDIR /code

COPY pyproject.toml ./
COPY some_code/ ./some_code/

RUN pip install --no-cache-dir .

ENV PYTHONPATH=/code

CMD ["python", "-m", "some_code.some_script"]
