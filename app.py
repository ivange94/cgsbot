from flask import Flask , request , make_response
from slackclient import SlackClient 
import json
import os

app = Flask(__name__)

slack_token = os.environ['SLACK_API_TOKEN']
sc = SlackClient(slack_token)
general_channel = "C93RP3CSG"
introductions_channel = "CFQV2533L"

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
                    channel=general_channel,
                    text="Hi, I will be your assistant. For now this is all I can do!"
                )
                return make_response("", 200)
            
            if (event_type == "team_join"):
                user = events_data["event"]["user"]
                welcome_text = "Welcome to Cameroon GSoCers Workspace. \nTell us a little bit about yourself, Your Real Names, Location, \nSpecialty/Department, Your Interests, Any specific questions ? \nLearn Netiquette Rules on http://www.albion.com/netiquette/corerules.html \nLearn How To Ask Smart Questions on http://www.catb.org/esr/faqs/smart-questions.html \nRemember to put your Real Names on your profile and a professional profile picture :) \nTake note of the channel topic and ALL pinned posts"
                sc.api_call(
                    "chat.postMessage",
                    channel=general_channel,
                    text="Hi @" + user["profile"]["display_name"] + ", \n" + welcome_template
                )
                return make_response("", 200)

        return make_response("Not implemented.", 404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
