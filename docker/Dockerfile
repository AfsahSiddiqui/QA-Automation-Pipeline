FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies required for Chrome and Chrome Browser
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    ca-certificates \
    wget \
    libnss3 \
    libxss1 \
    libgtk-3-0 \
    libasound2 \
    libgbm1 \
    fonts-liberation \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

COPY automated-testing/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY automated-testing/ .

CMD ["pytest", "--html=report.html", "--self-contained-html"]