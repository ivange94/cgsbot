from flask import Flask , request , make_response
import json

app = Flask(__name__)

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
        return make_response("Not implemented.", 404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)