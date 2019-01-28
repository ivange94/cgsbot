from flask import Flask , request , make_response
from slackclient import SlackClient 
import json
import os

app = Flask(__name__)

slack_token = os.environ['SLACK_API_TOKEN']
sc = SlackClient(slack_token)

@app.route('/', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        return make_response("These are not the slackbots you're looking for.", 404)
    else:
        events_data = json.loads(request.data.decode('utf-8'))

        if 'challenge' in events_data:
            return make_response(
                events_data.get('challenge'), 200, {'content_type': 'application/json'}
            )

        if "event" in events_data:
            event_type = events_data["event"]["type"]

            if (event_type == "app_mention"):
                sc.api_call(
                    "chat.postMessage",
                    channel='C93RP3CSG',
                    text="Hi, I'm Nancy. I will be your assistant. For now this is all I can do!"
                )
                return make_response("", 200)
        return make_response("Not implemented.", 404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)