import json
import re

with open('themes/claude-dark.json', 'r') as f:
    content = f.read()

replacements = {
    '"Claude Nine"': '"Claude Nine Light"',
    '"dark"': '"light"',
    '"#FFFFFF"': '"#000000"',
    '"#000000"': '"#FFFFFF"',
    '"#999999"': '"#666666"', 
    '"#505050"': '"#AFAFAF"', 
    '"#1F1F1E"': '"#FFFFFF"', 
    '"#1A1A19"': '"#F5F5F5"', 
    '"#181817"': '"#EBEBEB"', 
    '"#383835"': '"#F5F5F5"', 
    '"#2a2a29"': '"#D4D4D4"',
    '"#2a2a2980"': '"#D4D4D480"',
    '"#264F78"': '"#B4D5FF"',
    '"#264F7880"': '"#B4D5FF80"',
    '"#264F7840"': '"#B4D5FF40"',
    '"#264F7820"': '"#B4D5FF20"',
    '"#225C2B40"': '"#C7E1CB40"',
    '"#225C2B20"': '"#C7E1CB20"',
    '"#7A293640"': '"#FDD2D840"',
    '"#7A293620"': '"#FDD2D820"',
    '"#4EBA65"': '"#2C7A39"', 
    '"#FF6B80"': '"#AB2B3F"', 
    '"#FFC107"': '"#966C1E"', 
    '"#827DBD"': '"#8700FF"', 
}

# Use a regex to replace simultaneously and prevent the overlap bug
pattern = re.compile('|'.join(re.escape(k) for k in replacements.keys()))

def replace_match(match):
    return replacements[match.group(0)]

content = pattern.sub(replace_match, content)

with open('themes/claude-light.json', 'w') as f:
    f.write(content)
