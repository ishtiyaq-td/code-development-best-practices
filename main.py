import os
import logging
import requests


# Create 'logs' folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging to write to a file
logging.basicConfig(
    filename="logs/notification_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def send_notification(api_key, title, message):
    """
    Sends a notification using a hypothetical API.

    Args:
    - api_key (str): The API key for authentication.
    - title (str): The title of the notification.
    - message (str): The message content of the notification.

    Returns:
    - dict: A dictionary containing the API response.
    """
    api_url = "https://example.com/notification-api"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "title": title,
        "message": message,
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        logger.info("Notification sent successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send notification. {str(e)}")
        return {"error": f"Failed to send notification. {str(e)}"}


my_password = "test123"

# Example usage:
api_key = "your_api_key"
notification_title = "New Message"
notification_message = "You have a new message. Click to read."

result = send_notification(api_key, notification_title, notification_message)
print(result)
