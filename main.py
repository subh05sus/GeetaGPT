from flask import Flask, request, render_template, redirect,  send_from_directory
import geeta
from flask.helpers import url_for
from flask.templating import render_template_string
from flask import Blueprint
from dotenv import load_dotenv
import openaimodel as open
import Geminimodel as gena


# Load environment variables from .env file
load_dotenv()
quote = geeta.random_quote


server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'
static_bp = Blueprint('static',
                      __name__,
                      static_url_path='/static',
                      static_folder='static')
server.register_blueprint(static_bp)

messages = []
gemini_send_gpt = gena.send_gpt
openai_send_gpt = open.send_gpt

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        try:
            if len(request.form['question']) < 1:
                return render_template(
                    'chat3.5.html',
                    question="I have no questions ask. Lend me some of your knowledge",
                    res=quote
                )
            question = request.form['question']
            print("======================================")
            print("Receive the question:", question)
            resp_gemini = gemini_send_gpt(question)
            resp_openai = openai_send_gpt(question)
            try:
                res = resp_openai
            except:
                res = resp_gemini
                print("Gemini model used")
            # tokens = resp["usage"]["total_tokens"]
            print("Q：\n", question)
            print("A：\n", res)
            # print("tokens used: ", tokens)
            return render_template('chat3.5.html', question=question, res=str(res))
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            print(error_message)
            return render_template('chat3.5.html', question=question, res=error_message)
    return render_template('chat3.5.html', question=0)

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=80)

 
