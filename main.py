# 
from fastapi import FastAPI
import json 
import os 
import requests 
import config 
current_file_path = os.path.dirname(os.path.abspath(__file__))
CFIPS_PATH = os.path.join(current_file_path, 'cfips.json')
app = FastAPI()



# 发送消息到 telegram
def send_telegram_message(message):
    url = config.TELEGRAM_URL
    data = {
        'chat_id': config.TELEGRAM_CHATID,
        'text': 'get-cf-ip.py:'+message,
        # 'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=data)
    return response.json()

# Read JSON from file
def read_json_from_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Save JSON to file
def save_json_to_file(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get-one-cfip")
def get_one_cfip():
    cfips = read_json_from_file(CFIPS_PATH)
    if not cfip :
        send_telegram_message('cfips.json is empty')
        return None 
    cfip = cfips.pop() 
    save_json_to_file(cfips, CFIPS_PATH)
    return {'cfip':cfip} 
