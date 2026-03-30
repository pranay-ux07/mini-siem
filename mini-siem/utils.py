import re

def extract_ip(line):
    match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
    return match.group() if match else None