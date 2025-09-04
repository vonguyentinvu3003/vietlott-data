import json

file_path = r"C:\Users\OneBim\Desktop\data\vietlott-data\data\power655.jsonl"

results = []
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            obj = json.loads(line)
            results.append(obj["result"][:-1])

# In thử 5 kết quả đầu tiên
# for r in results:
#     print(r)

for r in results[:5]:
    print(r)
