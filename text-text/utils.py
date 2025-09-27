import os
import json
def load_json(filepath: str):
        path=os.path.join((os.path.dirname(__file__)),"..","assets",filepath)
        path = os.path.abspath(path) 
        with open(path, "r",encoding='utf-8') as f:
             raw_text=json.load(f)
        return raw_text