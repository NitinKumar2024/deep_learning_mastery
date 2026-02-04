import re

resume_text = "I am an expert in C++, Node.js, and AI/ML! I built smart edu ai."

tech_terms = ["C++", "Node.js", "AI/ML", "v1.0", "smart edu ai"]

tech_terms.sort(key=len, reverse=True) 

print(tech_terms)

escaped_terms = [re.escape(t) for t in tech_terms]
print(escaped_terms)

tech_pattern = "|".join(escaped_terms)
print(tech_pattern)

combine_pattern = f"({tech_pattern})|(\w+|[^\w\s])"
print(combine_pattern)

tokens = []

for match in re.findall(combine_pattern, resume_text):
    if match[0]:
        tokens.append(match[0])
    else:
        tokens.append(match[1])

print(tokens)