import os
import json

base_dir = "outputs"

total_docs = 0
total_violations = 0
total_rules = {}

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    if os.path.isdir(folder_path):
        json_path = os.path.join(folder_path, "execution.json")
        
        if os.path.isfile(json_path):
            with open(json_path, "r") as f:
                data = json.load(f)
                
                total_docs += 1
                total_violations += data["rule-violations"]["total"]

                for rule in data["rule-violations"]["by-rule"]:
                    if rule not in total_rules:
                        total_rules[rule] = 0

                    total_rules[rule] += data["rule-violations"]["by-rule"][rule]

print(total_docs, total_violations, total_rules)