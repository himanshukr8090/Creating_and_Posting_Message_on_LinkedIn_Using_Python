import requests

UNIPILE_KEY = "your-unipile-api-key"
USER_ACCOUNT_ID = "your-linkedin-account-id"  # Provided by Unipile

headers = {
    "accept": "application/json",
    "X-API-KEY": UNIPILE_KEY,
    "Content-Type": "application/json"
}

post_url = f"https://api1.unipile.com:13111/api/v1/accounts/{USER_ACCOUNT_ID}/posts"
payload = {"text": "Hello LinkedIn from Python via Unipile!"}

response = requests.post(post_url, headers=headers, json=payload)

print("Status:", response.status_code, response.json())

