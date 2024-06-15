import json

with open('llm_serialized.json', 'w') as f:
    serialized_llm = json.dumps({
        'model': "D:\Serverles\model\mistral-7b-instruct-v0.2.Q2_K.gguf",
        'model_type': "llama",
        'config': {'max_new_tokens': 512, 'temperature': 0.5}
    })
    f.write(serialized_llm)
import json
from langchain.llms import CTransformers

def load_llm(serialized_file):
    with open(serialized_file, 'r') as f:
        llm_data = json.load(f)
        return CTransformers(**llm_data)

def main():
    llm = load_llm('llm_serialized.json')
    while True:
        query = input("Enter your query : ")
        if query.lower() == 'quit':
            break
        result = llm(query)
        print(result)

if __name__ == '__main__':
    main()
