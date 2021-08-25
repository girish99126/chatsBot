from flask import Flask
from flask import json
from flask import request
from json import dumps

from httplib2 import Http






app = Flask(__name__)

@app.route("/")
def api_root():
    return "welcome bro"

@app.route('/github',methods=["POST"])
def api_git_message():
    
    if(request.headers['Content-Type']=="application/json"):
        return json.dumps(request.json)
    else:
        
        print(request.json)
        main(request.json)
        return json.dumps(request.json)
        

def main(msg):
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/wXJtHwAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=50JN8p7qiTGIHcVrmexTvvn6nMEW-_4svfqyHo5s-AI%3D'
    
    bot_message = {
        'text' : str(msg.get("name")+" is "+msg.get("build").get("phase"))}

    if(msg.get("build").get("status")== "SUCCESS"):
        bot_message={
    "cards": [
        {
        "sections": [
            {
            "widgets": [
                {
                "textParagraph": {
                    "text":"<b>"+msg.get("name")+"is "+msg.get("build").get("phase")+"</b> <br/> <font color=\"#008000\">Success</font>"
                }
                }
            ]
            }
        ]
        }
    ]
    }
   

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)


if __name__ == "__main__":
    app.run(debug=True)
   
