"""
Python Web Service
"""
#!/usr/bin/env python
import web
from requests import Session

url = "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers/f5b42fx173-nlc-1507/classify"

urls = (
    '/classify/(.*)', 'clasify_string'
)

app = web.application(urls, globals())

class clasify_string:
    def GET(self, user):
        print(self)
        s = Session()
        s.verify = False
        s.auth = ('e214758a-a5f4-4571-9a07-cb233ddfbc96', 'DVKxopmo6FH7')
        resp = s.get(url, params={'text': str(user)}, stream=True)
        content=resp.content
        return str(content.split('\n')[4].split('"')[3])

if __name__ == "__main__":
    app.run()
