topics = ["photosynthesis", "quantum", "relativity", "evolution", "newton"]
scores = [98, 97, 99, 98, 98]  # From your runs

avg = sum(scores) / len(scores)
print(f"Average Purity: {avg:.1f}%")  # 98.0%

# JSON export for report
import json
results = {"scenarios": topics, "purity": scores, "avg": avg}
with open("results.json", "w") as f:
    json.dump(results, f)
print("Results saved to results.json")
