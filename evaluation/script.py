import os
import json
import matplotlib.pyplot as plt
import numpy as np

base_dir = "outputs"

evaluation_data = {
    "apis": {},
    "nb-total-violations": 0,
    "violations": {}
}

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    if os.path.isdir(folder_path):
        json_path = os.path.join(folder_path, "execution.json")
        
        if os.path.isfile(json_path):
            with open(json_path, "r") as f:
                data = json.load(f)

                name = data["name"]
                nb_routes = data["nb-routes"]
                nb_violations = data["rule-violations"]["total"]
                
                evaluation_data["apis"][name] = {
                    "nb-routes": nb_routes,
                    "nb-violations": nb_violations
                }

                evaluation_data["nb-total-violations"] += nb_violations

                for rule in data["rule-violations"]["by-rule"]:
                    if rule not in evaluation_data["violations"]:
                        evaluation_data["violations"][rule] = 0

                    evaluation_data["violations"][rule] += data["rule-violations"]["by-rule"][rule]


print(evaluation_data["nb-total-violations"])

"""
sorted_data = dict(sorted(evaluation_data["violations"].items(), key=lambda item: item[1], reverse=True))

keys = list(sorted_data.keys())
values = list(sorted_data.values())

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
plt.barh(keys, values, color='skyblue')
plt.xlabel('Values')
plt.title('Counts of HTTP Response Rules')
plt.gca().invert_yaxis()  # Largest values on top
plt.tight_layout()

# Display the chart
plt.show()
"""


"""
api_names = list(apis.keys())
routes = [apis[api]['nb-routes'] for api in apis]
violations = [apis[api]['nb-violations'] for api in apis]

x = np.arange(1, len(api_names) + 1)
width = 0.4

# Create bar chart
plt.figure(figsize=(18, 6))
plt.bar(x - width / 2, routes, width=width, label="Number of Routes")
plt.bar(x + width / 2, violations, width=width, label="Number of Violations")

# Axis labels and ticks
plt.xlabel("API Index")
plt.ylabel("Count")
plt.title("Routes vs Violations per API")
plt.xticks(x, x)  # show indices instead of API names
plt.legend()

plt.tight_layout()
plt.show()
"""