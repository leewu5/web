from flask import Flask, request, jsonify
import transformers
from transformers import AutoModelForMaskedLM, BertTokenizer, pipeline
from transformers import BertTokenizer, BertConfig

app = Flask(__name__)

# 加载微调好的模型和标记器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', cache_dir='cache_dir') # MosaicBERT uses the standard BERT tokenizer

config = transformers.BertConfig.from_pretrained('mosaicml/mosaic-bert-base', cache_dir='cache_dir') # the config needs to be passed in
mosaicbert = AutoModelForMaskedLM.from_pretrained('mosaicml/mosaic-bert-base', config=config, trust_remote_code=True, cache_dir='cache_dir')

# To use this model directly for masked language modeling
mosaicbert_classifier = pipeline('fill-mask', model=mosaicbert, tokenizer=tokenizer, device="cpu")
# mosaicbert_classifier("I [MASK] to the store yesterday.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        text = data['text']

        # 处理输入文本
        inputs = tokenizer(text, return_tensors="pt")

        # 进行预测
        outputs = mosaicbert_classifier(**inputs)

        return jsonify({'outputs': outputs})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
