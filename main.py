import time
import requests
import json

def main():
    with open("queries.txt", "r") as f:
        queries = f.read().splitlines()
    
    all_prompts = []
    for query in queries:
        query = "https://lexica.art/api/v1/search" + query[len("https://lexica.art/"):]
        print(query)
        try:
            response = requests.get(query)
        except:
            continue
        # print(response.content)
        result = json.loads(response.content)
        prompts = []
        for item in result["images"]:
            prompts.append(item["prompt"])
        time.sleep(1)
        all_prompts.extend(prompts)
    return all_prompts


if __name__ == "__main__":
    all_prompts = main()
    with open("all_prompts.txt", "w") as f:
        for line in all_prompts:
            f.write(line + "\n")