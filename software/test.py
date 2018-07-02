from pyrogram import Client
import sys,os
import requests
import json
import time
import random
import string

global phone

def phone_code_callback():


    time.sleep(40)
    url = "http://userapi.izinumber.com/mynumbers/tZlTminKblMSlJW10QBg/check/"+phone
    print(url)
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0e48221e-52da-3f40-b9ae-515023b0f599"
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    try:
        results = json.loads(response.text)

        if str(results[0]['content']).startswith("Telegram code"):
            print (str(results[0]['content']).replace("Telegram code ",""))
            return str(results[0]['content']).replace("Telegram code ","")
    except:
        return "12345"

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def registerUser(phoneNumber:str,groupID:str,message:str,userName:str,lastName:str):
    rnd = random_generator();
    print(rnd)

    client = Client(
        session_name=phoneNumber,
        phone_code=phone_code_callback,
        #phone_number="918093735782",
        phone_number=phoneNumber,
        first_name=userName,
        last_name=lastName  # Can be an empty string
    )

    try:
        client.start()

        # Your Group Invite Link
        resp = client.join_chat(chat_id=groupID)
        resp = client.send_message(chat_id=groupID,text=message)

    except Exception as e: print(e)


# srcipt goes here # Your Number in Params
phone=sys.argv[1]
registerUser(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
os._exit(0)
