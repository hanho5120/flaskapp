from flask import Flask, render_template , request,redirect,jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather/<int:city>')
def weather(city):
    return city

@app.route('/movemenu',methods=('POST','GET'))
def movemenu():

    req = request.get_json(force=True)
    print(req)
    action = req['queryResult']['intent']['displayName']  # 1
    if action == 'weather':
          print(action)

    response_json = jsonify(
        fulfillment_text='영화정보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [[
                        {
                             "type": "image",
                             "rawUrl": "http://img.cgv.co.kr/Movie/Thumbnail/Poster/000082/82120/82120_1000.jpg"
                        },
                        {
                            "type": "info",
                            "title": '탑건',
                            "actionLink": 'https://moviestory.cgv.co.kr/fanpage/mainView;jsessionid=9A2A4DA75143D960B95E007DAEDAA124.STORY_node?movieIdx=82120',
                            "subtitle": '탑건'
                        }
                    ]]
                }
            }
        ]
    )

    return response_json


if __name__=="__main__":
    app.run('0.0.0.0', port=5001, debug=True)  #host = '127.0.0.1' port='5000'