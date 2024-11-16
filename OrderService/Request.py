import requests

url = "http://localhost:5000/orders"
payload = {"product_id": "123", "quantity": 2}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
