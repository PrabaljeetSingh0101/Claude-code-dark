import json
import re

with open('themes/claude-dark.json', 'r') as f:
    content = f.read()

# Replace specific hex codes
replacements = {
    # Name and Type
    '"Claude Nine"': '"Claude Nine Light"',
    '"dark"': '"light"',
    
    # Foreground / Text
    '"#FFFFFF"': '"#000000"',
    '"#000000"': '"#FFFFFF"',
    '"#999999"': '"#666666"', # inactive
    '"#505050"': '"#AFAFAF"', # subtle
    
    # Backgrounds
    '"#1F1F1E"': '"#FFFFFF"', # Editor
    '"#1A1A19"': '"#F3F3F3"', # Sidebar/Panel
    '"#181817"': '"#E8E8E8"', # Activity Bar / Status Bar
    '"#383835"': '"#F3F3F3"', # Menus
    
    # Borders
    '"#2a2a29"': '"#D4D4D4"',
    '"#2a2a2980"': '"#D4D4D480"',
    
    # Selections
    '"#264F78"': '"#A8D1FF"',
    '"#264F7880"': '"#A8D1FF80"',
    '"#264F7840"': '"#A8D1FF40"',
    '"#264F7820"': '"#A8D1FF20"',
    
    # Diff Backgrounds
    '"#225C2B40"': '"#C7E1CB40"',
    '"#225C2B20"': '"#C7E1CB20"',
    '"#7A293640"': '"#FDD2D840"',
    '"#7A293620"': '"#FDD2D820"',
    
    # Semantic Colors
    '"#4EBA65"': '"#2C7A39"', # Success
    '"#FF6B80"': '"#AB2B3F"', # Error
    '"#FFC107"': '"#966C1E"', # Warning
    '"#827DBD"': '"#8700FF"', # Purple
    
    # We leave #D77757 (orange), #6A9BCC (blue), #FBBC04 (yellow) as is.
}

# Apply replacements
for old, new in replacements.items():
    content = content.replace(old, new)

# Write to light theme
with open('themes/claude-light.json', 'w') as f:
    f.write(content)

print("Generated claude-light.json")
