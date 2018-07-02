from pyrogram import Client
import requests
import json
import time
import random
import string


def phone_code_callback():
    time.sleep(30)
    url = "http://userapi.izinumber.com/mynumbers/tZlTminKblMSlJW10QBg/check/19342227719"
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0e48221e-52da-3f40-b9ae-515023b0f599"
    }

    response = requests.get(url, headers=headers)
    # print(response.text)
    results = json.loads(response.text)
    try:
        if str(results[0]['content']).startswith("Telegram code"):
            return str(results[0]['content'])
    except:
        return "12345"


def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def registerUser(phoneNumber: str):
    rnd = random_generator();
    print(rnd)

    client = Client(
        session_name=rnd,
        phone_code=phone_code_callback,
        # phone_number="918093735782",
        phone_number=phoneNumber,
        first_name="Test",
        last_name="User"  # Can be an empty string
    )

    try:
        client.start()

        # Your Group Invite Link
        resp = client.join_chat(chat_id="t.me/joinchat/HOyD4RH1YuiL61ty4sNNrw")
    except:
        print("Client already registered or Message Not receieved")


# srcipt goes here # Your Number in Params
registerUser("+18383000936")