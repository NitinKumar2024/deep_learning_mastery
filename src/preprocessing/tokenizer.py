import re

def rigorous_tokenize(text: str, custom_terms: list = []) -> list:
    # 1. Handle Empty Custom Terms (Safety Check)
    if not custom_terms:
        # If no custom terms, just split by words and punctuation
        return re.findall(r"\w+|[^\w\s]", text)

    # 2. Prepare the Regex
    custom_terms.sort(key=len, reverse=True) 
    escaped_terms = [re.escape(t) for t in custom_terms]
    tech_pattern = "|".join(escaped_terms)
    
    # 3. Combine Logic
    combine_pattern = f"({tech_pattern})|(\w+|[^\w\s])"

    tokens = []
    for match in re.findall(combine_pattern, text):
        if match[0]:
            tokens.append(match[0])
        else:
            tokens.append(match[1])

    return tokens