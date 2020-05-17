import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

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
num=input('Enter mobile number: ')
msg=input('Enter message: ')
# get response
response = sendPostRequest(URL, 'CYQCG29KDVD7BO6BMXA8ZTR5H405386G', 'FHYKK6I8D564QF29', 'stage', num , 'l3xi3', msg )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)
