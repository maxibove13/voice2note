import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

# Get the variables from the environment
access_token = os.environ.get("TELEGRAM_ACCESS_TOKEN")
verify = os.environ.get("TELEGRAM_VERIFY")
webhook_url = os.environ.get("TELEGRAM_WEBHOOK_URL")

# Use the variables in your credentials.yml content
credentials_yml = f"""addons.telegram.TelegramInput:
  access_token: "{access_token}"
  verify: "{verify}"
  webhook_url: "{webhook_url}"
"""

# Save the credentials to a file
with open("credentials.yml", "w") as f:
    f.write(credentials_yml)
