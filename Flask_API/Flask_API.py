from flask import Flask, render_template
from flask import request, jsonify
import json

@app.route('/index',methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return jsonify({'status':'failure','msg':'Only POST request served'})
    elif request.method == 'POST':
        req_Json = request.json
        CliRaw = req_Json['CliRaw'] #This is the User Payload
        TempName= req_Json['TempName']
    return jsonify({
            'status': CliRaw,
            'msg': 'Successfully applied TextFSM template on device log',
            'body': output})
