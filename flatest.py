from flask import Flask, request

import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd

host = "chatbot-mysql.cwvbxvvwztug.ap-northeast-2.rds.amazonaws.com"
port = 3306
username = "chatbot"
password = "bitbit123!"
db = "lawbot"

conn = pymysql.connect(host=host, port=port, user=username, password=password, db=db)



sql_state = 'select * from chat where date<"2022-09-17"'
df = pd.read_sql_query(sql_state, conn)


from konlpy.tag import Okt


tokenizer = Okt()
df['tokenized'] = df['message'].apply(tokenizer.nouns)


import numpy as np
print(df)
df = np.hstack(df['tokenized'].values)


app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    print(request.data)
    print(request.json)
    print(request.form)
    print(request.json["message"])
    request.json["message"]
    return {"message":20}

@app.route('/getTest', methods=['GET'])
def test():
    return {"get":3030}

if __name__ == '__main__':
    app.run()
