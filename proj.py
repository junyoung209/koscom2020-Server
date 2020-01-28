
from flask import Flask, request, jsonify

# 플라스크 웹 서버 객체를 생성합니다.
app = Flask(__name__)


@app.route("/process", methods=['GET', 'POST'])
def process():
    if request.method=='POST':
        result=[]
        contents = {'result': True}
        content = request.json
        result.append(contents)
        result.append(content)
        return jsonify(result)
    else:
        result=[]
        for i in range(1,4):
            sub={'id':i,'title':i,'content':i}
            result.append(sub)

        return jsonify(result)

@app.route("/")
def process1():
    return 'jsonify(result)'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)