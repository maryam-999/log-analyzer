from collections import Counter

with open('log.txt') as f:
    lines = f.readlines()

stats = Counter()
for line in lines:
    if 'ERROR' in line:
        stats['ERROR'] += 1
    elif 'WARNING' in line:
        stats['WARNING'] += 1
    elif 'INFO' in line:
        stats['INFO'] += 1

with open('rapport.txt', 'w') as report:
    for k, v in stats.items():
        report.write(f"{k}: {v}\n")

print("Analyse terminée.")
