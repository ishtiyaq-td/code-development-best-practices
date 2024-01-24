import requests


def send_notification(key, title, msg):
    api_url = "https://example.com/notification-api"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}",
    }

    payload = {
        "title": title,
        "message": msg,
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to send notification. {str(e)}"}


# Example usage:
my_key = "your_api_key"
title = "New Message"
msg = "You have a new message. Click to read."

result = send_notification(my_key, title, msg)
print(result)
