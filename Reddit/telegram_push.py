import requests
import os
import random

def post_message(message):
    
    tele_chatid = ''
    thread_id = ''
    tele_api= ''
    
    payload = {'chat_id' : tele_chatid, "message_thread_id": thread_id,'text' : message, 'parse_mode' : "HTML"}
    response = requests.post(tele_api, json=payload)
    
    if response.status_code == 200:
        print("post sucessful")
    else:
        print(f"error in posting {response}")