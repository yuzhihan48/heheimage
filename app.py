#!/usr/bin/env python
# coding: utf-8




# In[ ]:


from flask import Flask, render_template, request
import openai
import json
import requests
import time

openai.api_key = "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"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        body = json.dumps({
            "version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
            "input": {
                "prompt": q
            }
        })
        header = {
            "authorization": "Token b67d8c1f66133b563f269688f742a022bd5134e8",
            "content-type": "application/json"
        }
        output = requests.post('https://api.replicate.com/v1/predictions', data=body, headers=header)
        time.sleep(10)
        get_url = output.json()['urls']['get']
        get_result = requests.post(get_url, headers=header).json()["output"]

        return render_template("index.html", result=get_result[0])
    else:
        return render_template("index.html", result="waiting for your question...")

if __name__ == "__main__":
    app.run(port=8080)


# In[ ]:




