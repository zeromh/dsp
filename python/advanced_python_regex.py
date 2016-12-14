import re

pattern_email = '([\w.-]+)@([\w+.-]+)'
match = re.search(pattern, emaillllls)
match.group(2) #will return domains
