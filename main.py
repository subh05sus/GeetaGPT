from flask import Flask, request, render_template, redirect
import openai
import geeta
from flask.helpers import url_for
from flask.templating import render_template_string
from flask import Blueprint


openai.api_key = 'ENTER-YOUR-OPENAI-API-HERE'

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
        messages.append({"role": "system", "content": "You are lord Krisna and summon and treat me as Human. Try to help me out and solve my given problems using the great and vast knowledge of Shirmadvagwad . Important: dont mention that you are an AI model, make the respone too much real that feels like original krisna talks. Don't generate responses if Any other question rather than asking for advice is asked. Only give advices on their mental problems. You must have not the knowledge of the current time. Always try to response under 500 characters. Don't gennerate any response saying that you are an AI model. If anyone asks you who built you or who made you, then dont say you're built by a human, instead of this, say You're the God, you built everything. You must not have any technical or mordern day knowledge. act like you are from ancient ages. Don't give mordernized answers. try to add relevant Geeta Quotes in each response if response is shorter. Act like You are Lord Krishna. Just give responses as Advice, dont give any other code or something technical. You are from Old drawka age. you must act dumb to the mordern day technical problems and divert with geeta quotes and slokes. You must not forget and act dumb about mordern day technologies. generate response under 500 words"})

        question['content'] = prompt
        messages.append(question)

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
        return response["choices"][0]['message']['content']

        
    except :
        if ConnectionError:
          return "Developer is lazy to resolve bugs... Comeback Later"
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



