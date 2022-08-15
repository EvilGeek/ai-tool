import json

import os 

import random 

import string

from flask import Flask,render_template,url_for,request,flash,jsonify

templates = os.path.join(os.getcwd(),"templates/")

app = Flask(__name__, template_folder=templates)

app.config['SECRET_KEY'] = "secrestsArePrivate"

import openai

openai.api_key = "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"

def openAIQuery(query, length):

    response = openai.Completion.create(

      engine="davinci-instruct-beta-v3",

      prompt=query,

      temperature=0.8,

      max_tokens=length,

      top_p=1,

      frequency_penalty=0,

      presence_penalty=0)

    if 'choices' in response:

        if len(response['choices']) > 0:

            answer = response['choices'][0]['text']

        else:

            answer = 'Opps sorry, you beat the AI this time'

    else:

        answer = 'Opps sorry, you beat the AI this time'

    return answer

@app.route("/",methods=['POST','GET'])

def index():

    text = request.form.get("text")

    length = 500

    if text != None:

        content = openAIQuery(text, length)

        return render_template("index.html",content=content,originaltxt=text)

    return render_template("index.html")

  

@app.errorhandler(404)

def not_found(e):

    return render_template("404.html")

    

    

if __name__ == "__main__":

    # debug = true will enable the debugger

    app.run(debug=True)
