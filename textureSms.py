import requests
import json
import os
from time import sleep
import sys
from termcolor import colored

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# titlebar
def title_bar():
    os.system("clear")
    print("\t\t\t ---------------------------------------------------")
    print("\t\t\t|   W E L C O M E   T O   T E X T U R E    S M S    |")
    print("\t\t\t ---------------------------------------------------\n")
# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

title_bar()
try:
    while True:
        num=input('[+] Enter mobile number: ')
        if not num.isdigit():
            print(colored("[!!] Only numbers are accepted\n", 'red'))
            continue
        elif len(num)!=10:
            print(colored("[!!] 10 Digit number is accepted\n", 'red'))
            continue
        else:
            break
    msg=input('[+] Enter message: ')
    # get response
    response = sendPostRequest(URL, '96RN5RK6G8NVG6Z47FRSNPVH6DGT86C2', 'ZZ8YUDJQAIZV6LBO', 'stage', num , 'l3xi3', msg )
    """
    Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
    """
    # print response if you want
    json_obj=json.loads(response.text)
    print(json_obj["message"])
except KeyboardInterrupt as error:
    print("\nQuiting...")
    sleep(0.5)
