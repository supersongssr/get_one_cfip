# 
from fastapi import FastAPI, Form
import json 
import os 
import requests 
import config 
current_file_path = os.path.dirname(os.path.abspath(__file__))
CFIPS_PATH = os.path.join(current_file_path, 'cfips.json')
app = FastAPI()

# 发送消息到 telegram
def send_telegram_message(message : str ) -> dict:
    url : str  = config.TELEGRAM_URL
    data : dict  = {
        'chat_id': config.TELEGRAM_CHATID,
        'text': 'get-cf-ip.py:'+message,
        # 'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=data)
    return response.json()

# Read JSON from file
def read_json_from_file(file_path : str ) -> list :
    with open(file_path, "r") as f:
        return json.load(f)

# Save JSON to file
def save_json_to_file(data : list, file_path : str) -> None :
    with open(file_path, "w") as f:
        json.dump(data, f)

@app.get("/")
def read_root() -> dict :
    return {"Hello": "World"}


@app.get("/get-one-cfip")
def get_one_cfip() -> dict :
    cfips : list  = read_json_from_file(CFIPS_PATH)
    if not cfips :
        send_telegram_message('cfips.json is empty')
        return {} 
    cfip : str = cfips.pop() 
    save_json_to_file(cfips, CFIPS_PATH)
    return {'cfip':cfip} 

# 通知 api 通知 telegram; 请求体是 json. 见 docs
@app.post("/notify")
def notify(token : str, message : str) -> dict :
    # 获取 参数 token 和 message
    if token != config.NOTIFY_TOKEN :
        send_telegram_message('notify: token is not correct')
        return {'err':'token-correct'}
    send_telegram_message(message)
    return {'notify':'done'}
