import re

text = "1 cL of lemon juice"
text = text.replace('_', ' ')


numP = r'(\d+(?:_\d+)?)\s*'
cl_pattern = r'\bcLs?\b'
pattern = numP + cl_pattern
match = re.search(pattern, text)

if match:
    print(match.group())
    
    
"""
for match in matches:
    print(match)

import re

s = 'Python 3.10'
pattern = '(\d+)\.(\d+)'

match = re.search(pattern, s)

# show the whole match
print(match.group())

# show the groups
for group in match.groups():
    print(group)
"""