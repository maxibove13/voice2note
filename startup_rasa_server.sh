python3 utils/create_credentials.py && echo "credentials.yml created out of .env vars" && \
rasa run -m models --enable-api --cors "*" --port 5005
