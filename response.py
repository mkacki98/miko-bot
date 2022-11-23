import requests
from configs import app_config


def send_message(recipient_id, text):
    """Send a response to Facebook"""

    message = text + f", your id is {recipient_id}"
    payload = {
        "message": {"text": message},
        "recipient": {"id": recipient_id},
        "notification_type": "regular",
    }

    auth = {"access_token": app_config["PAGE_ACCESS_TOKEN"]}

    response = requests.post(app_config["FB_API_URL"], params=auth, json=payload)

    return response.json()