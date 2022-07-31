import argparse
from flask import Flask, request
from flask_cors import CORS
from args import predict_argparser
from config_reader import process_configs
from spert import input_reader
from spert.spert_trainer import SpERTTrainer
import json
import spacy

api = Flask(__name__)
CORS(api)

def _predict():
    arg_parser = predict_argparser()
    process_configs(target=__predict, arg_parser=arg_parser)


def __predict(run_args):
    trainer = SpERTTrainer(run_args)
    trainer.predict(dataset_path=run_args.dataset_path, types_path=run_args.types_path,
                    input_reader_cls=input_reader.JsonPredictionInputReader)

@api.route('/')
def health_check():
    return 'OK'

@api.route('/fs-predict', methods=['POST', 'GET'])
def predict():
    text = request.args.get('text', type=str)
    print(text)
    spcy = spacy.load("de_dep_news_trf")
    doc = spcy(text)
    with open("data/datasets/financial_statements/financial_statements_prediction_example.json", 'w', encoding='utf-8') as f:
        if len(list(doc.sents)) > 1:
            json.dump([sentence.text for sentence in doc.sents], f, ensure_ascii=False)
        else:
            json.dump([text], f, ensure_ascii=False)
    _predict()
    with open("data/predictions.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('mode', type=str, help="Mode: 'train' or 'eval'")
    args, _ = arg_parser.parse_known_args()

    if args.mode == 'predict':
        _predict()
    elif args.mode == 'api':
        api.run(debug=True, host='0.0.0.0', port=5000)
    else:
        raise Exception("Mode not in ['train', 'eval', 'predict'], e.g. 'python spert.py train ...'")