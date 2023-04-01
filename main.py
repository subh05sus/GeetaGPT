from flask import Flask, request, render_template, redirect
import openai
import geeta
from flask.helpers import url_for
from flask.templating import render_template_string
from flask import Blueprint


openai.api_key = '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'

logo="</>"
quote = geeta.random_quote


server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'
static_bp = Blueprint('static', __name__, static_url_path='/static', static_folder='static')
server.register_blueprint(static_bp)


messages=[]
question = {}
question['role'] = 'user'

def send_gpt(prompt):
    try:
        messages.append({"role": "system", "content": "You are lord Krisna and summon and treat me as Human. Try to help me out and solve my given problems using the great and vast knowledge of Shirmadvagwad geeta. dont mention that you are an AI model, make the respone too much real that feels like original krisna talks. Always try to response under 500 characters."})

        question['content'] = prompt
        messages.append(question)

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
        return response["choices"][0]['message']['content']

        
    except :
        if ConnectionError:
          return "No Network"
        else:
            return "Developer is lazy to resolve bugs... Comeback Later"


@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat3.5.html', question="I have no questions ask. Lend me some of your knowledge", res=quote)
        question = request.form['question']
        print("======================================")
        print("Receive the question:", question)
        res = send_gpt(question)
        print("Q：\n", question)
        print("A：\n", res)

        return render_template('chat3.5.html', question=question, res=str(res))
    return render_template('chat3.5.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=80)



