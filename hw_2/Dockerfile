FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-base texlive-fonts-recommended texlive-latex-extra \
    texlive-xetex texlive-lang-cyrillic ghostscript \
    python3-pip python3-venv pipx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./app/main.py"]
