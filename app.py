# app.py

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# # 配置MySQL数据库连接
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://law:123456@49.123.83.191/america'
# db = SQLAlchemy(app)
#
# # 定义数据库模型
# class america_structed_case(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_text = db.Column(db.String(80), unique=True, nullable=False)
#     analysis = db.Column(db.String(120), unique=True, nullable=False)

#加载模型
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("model/checkpoint-14500")
model = AutoModelForSequenceClassification.from_pretrained("model/checkpoint-14500")

#加载标签字典
import json

with open("edit_data/id2text.json", "r", encoding = "utf-8") as jf:
    id2label = json.load(jf)

@app.route('/anyou', methods=['POST'])
def anyou():
    # # 从数据库中获取用户数据
    # users = america_structed_case.query.all()
    # return render_template('index.html', users=users)
    # 读取数据
    data = request.get_json()
    for it in data:



if __name__ == '__main__':
    app.run(debug=True)
