import json
with open('text_7.txt', "r", encoding="UTF-8") as reader:
    lines = reader.readlines()
    d = {line.split()[0]: float(line.split()[2]) - float(line.split()[3]) for line in lines}
    avg = {"average_profit:": round(sum([s for s in d.values() if s > 0]) / len(lines))}
    print([d, avg])
with open('js_7.json', "w", encoding="utf-8") as js_writer:
    json.dump([d, avg],js_writer)