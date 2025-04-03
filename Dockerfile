FROM python:3.13.2-bullseye

WORKDIR /app

# preven python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# ensure python output is send directly
# to the terminal without buffering
ENV PYTHONUNBUFFERED=1

# upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Entrypoint
COPY entrypoint.sh entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . .

EXPOSE 8000

# ENTRYPOINT
ENTRYPOINT [ "/app/entrypoint.sh" ]