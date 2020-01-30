# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import csv
import json
import sql as sql_db
import data as d
# 플라스크 웹 서버 객체를 생성합니다.
app = Flask(__name__,static_folder='./outputs')
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def main_data():
    data=d.getdata('1')
    return json.dumps(data,ensure_ascii=False)

@app.route("/outputs",methods=['GET','POST'])
def output():
    stock_code=request.args.get('stock_code')
    return app.send_static_file(stock_code + '.png')

@app.route("/outputs_logo",methods=['GET','POST'])
def output_logo():
    stock_name=request.args.get('stock_name')
    return app.send_static_file('./outputs_logo/'+stock_name + '.png')

@app.route("/outputs_pop",methods=['GET','POST'])
def output_pop():
    stock_code = request.args.get('stock_code')
    return app.send_static_file('./outputs_pop/'+stock_code + '_pop.png')

@app.route("/sectors",methods=['GET','POST'])
def sectors():
    data = d.getdata('1')
    sector_list=[]
    for i in range(len(data)):
        sector_list.append(data[i]['stock_sector'])
    sector_list=list(set(sector_list))
    return json.dumps(sector_list, ensure_ascii=False)


@app.route("/favorite",methods=['GET','POST'])
def favorite():
    data = d.getdata('1')
    temp=[]
    for i in range(len(data)):
        if data[i]['favorite']=='1':
            temp.append(data[i])
    return json.dumps(temp, ensure_ascii=False)


@app.route("/validate",methods=['GET','POST'])
def validate():
    text_id=request.args.get('textID')
    path='./outputs/{0}.png'.format(text_id)
    result={}
    if os.path.isfile(path):
        result['result']=True
    else:
        result['result']=False
    return jsonify(result)

@app.route("/favorite_id",methods=['GET','POST'])
def favorite_id():
    stock_code=request.args.get('stock_code')
    result=sql_db.sql_select2('favorite','1',stock_code)

    if len(result)==0:
        sql_db.sql_insert('1',stock_code)
        result_id='insert'
    else:
        sql_db.sql_delete('1',stock_code)
        result_id='delete'
    return result_id

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)