FROM python:3.11.7

RUN useradd -ms /bin/bash streamlity

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

USER streamlity
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
