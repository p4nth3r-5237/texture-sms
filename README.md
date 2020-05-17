# message-sender
pull repository in your local
```
git clone https://github.com/anoopyadavan/message-sender.git
cd message-sender
```
Now you have to install requirement in this project you have to install two library that is json and requests. <br>
to install requirements
```
pip install -r requirements.txt
```
Now you have need to make account on https://www.sms4india.com/ and register it then loging with that account and enter it 
at there on top API is there click on that you will get like in image.<br>
![Alt text](sms-sender.png?raw=true "API")  <br>
copy api key and replace api-key with your api key  and then copy secret key from that website and replace secret-key with your secret key.
```
response = sendPostRequest(URL, 'api-key', 'secret-key', 'stage', num , 'l3xi3', msg )
```
Now run your program 
```
python3 sms.py
```
Now you have to enter number on which you want to send and message.
