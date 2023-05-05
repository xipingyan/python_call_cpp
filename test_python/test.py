import sys
sys.path.append("../build/")
import mylib
# VS code pylance add parsing config
# File: .vscode/settings.json
# Context:
# {
#     "python.analysis.extraPaths": ["./sources"]
# }

print("mylib.add(1, 2) =", mylib.add(1, 2))
print("mylib.minus(10, 2) =", mylib.minus(10, 2))