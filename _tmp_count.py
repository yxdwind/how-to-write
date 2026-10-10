import re

s = open("evals/runs/baseline-a2b.md", encoding="utf-8").read()
a = s.split("## 任务A成稿", 1)[1].split("## 任务B成稿", 1)[0]
b = s.split("## 任务B成稿", 1)[1]

def count(t):
    lines = [
        ln for ln in t.splitlines()
        if not ln.lstrip().startswith("（字数说明")
        and not ln.lstrip().startswith("（全文约")
    ]
    txt = "".join(lines)
    return len(re.sub(r"\s", "", txt))

print("A:", count(a))
print("B:", count(b))
