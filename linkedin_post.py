import os
import requests
from dotenv import load_dotenv

load_dotenv()  # To load LINKEDIN_ACCESS_TOKEN from .env

ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")
USER_URN = os.getenv("LINKEDIN_USER_URN")  # e.g. "urn:li:person:ABC123"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

post_body = {
    "author": USER_URN,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": "Hello LinkedIn from Python!"},
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}

response = requests.post(
    "https://api.linkedin.com/v2/ugcPosts",
    headers=headers,
    json=post_body
)

if response.status_code == 201:
    print("✅ Post successful!")
else:
    print("❌ Error:", response.status_code, response.text)

