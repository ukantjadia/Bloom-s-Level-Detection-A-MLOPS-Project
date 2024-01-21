# FROM python:3.11-slim

# WORKDIR /app
# COPY . ./
# EXPOSE 8501

# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# ENTRYPOINT ["streamlit", "run"]
# CMD [ "app.py"]

FROM python:3.11-slim

WORKDIR /app

# COPY requirements.txt ./requirements.txt
COPY . ./

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        netbase \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8501


ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]