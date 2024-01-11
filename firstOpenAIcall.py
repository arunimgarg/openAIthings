import requests
import json

url = "https://api.openai.com/v1/images/generations"

payload = json.dumps({
  "model": "dall-e-3",
  "prompt": "A cute penguin on a jetski",
  "n": 1,
  "size": "1024x1024"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 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',
  'Cookie': '__cf_bm=5CTD748YJoiEWpZwFbjesA3_LrzH4no6i5tbNmpyTCM-1704939028-1-AY8nZFDruJO6LxdX6KE4NegQwj6tOHzDwT5nqGH4gSlkSOLzNkUrB5ZuX/HBCKG/xTiD3AKBBKozRk3cwTR9cDk=; _cfuvid=mdMLip3O.QhUYAjAXISYFVmZYhOx2SlISiRHytcfwZ4-1704939028703-0-604800000'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)