"""
Python Web Service
"""

#!/usr/bin/env python
import web
from requests import Session
File = open('data.txt','r')
s = Session()
for line in File:
    resp = s.get('http://0.0.0.0:8080/classify/', params={'user': str(line)}, stream=True)
    content=resp.content
    print(content)
