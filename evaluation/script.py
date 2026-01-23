import os
import json
import matplotlib.pyplot as plt
from pathlib import Path


# ------
# PATHS
# ------
EVALUATION_PATH = Path(__file__).resolve().parent
CHARTS_PATH = EVALUATION_PATH / "charts"
CHARTS_PATH.mkdir(parents=True, exist_ok=True)


# -----------------
# DATA PREPARATION
# -----------------
base_dir = "outputs"

evaluation_data = {
    "nb-violations-total": 0,
    "results-per-api": {},
    "results-per-violation": {}
}

for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    
    if os.path.isdir(folder_path):
        json_path = os.path.join(folder_path, "execution.json")
        
        if os.path.isfile(json_path):
            with open(json_path, "r") as f:
                execution_data = json.load(f)

                name = execution_data["name"]
                nb_routes = execution_data["nb-routes"]
                nb_violations = execution_data["rule-violations"]["total"]

                evaluation_data["nb-violations-total"] += nb_violations
                
                evaluation_data["results-per-api"][name] = {
                    "nb-routes": nb_routes,
                    "nb-violations": nb_violations
                }

                for rule in execution_data["rule-violations"]["by-rule"]:
                    if rule not in evaluation_data["results-per-violation"]:
                        evaluation_data["results-per-violation"][rule] = {
                            "nb-total": 0,
                            "nb-apis": 0,
                            "in": []
                        }

                    evaluation_data["results-per-violation"][rule]["nb-total"] += execution_data["rule-violations"]["by-rule"][rule]

                    if name not in evaluation_data["results-per-violation"][rule]["in"]:
                        evaluation_data["results-per-violation"][rule]["in"].append(name)
                        evaluation_data["results-per-violation"][rule]["nb-apis"] += 1


print(json.dumps(evaluation_data, indent=4))


# --------------------------------------
# CHART FOR VIOLATIONS PER DISTINCT API
# --------------------------------------
chart_data = dict(sorted(evaluation_data["results-per-violation"].items(), key=lambda item: item[1]["nb-apis"], reverse=True))

rule_ids = list(chart_data.keys())
rule_values = [chart_data[rule_id]["nb-apis"] for rule_id in rule_ids]

plt.figure(figsize=(20, 12))
plt.barh(rule_ids, rule_values, color="orange")

plt.xlabel("Amount of REST API Specifications", fontweight="bold", fontsize=16, labelpad=20)
plt.ylabel("Rule Identifier", fontweight="bold", fontsize=16, labelpad=20)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.xticks(range(0, 61, 10))

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.xaxis.grid(True, color="gray", linestyle="--", linewidth=0.5, zorder=0)
ax.set_axisbelow(True)

plt.gca().invert_yaxis()

ax.margins(y=0)

plt.tight_layout()

plt.savefig(CHARTS_PATH / "chart-violations-per-distinct-api.pdf", format="pdf")
plt.close()