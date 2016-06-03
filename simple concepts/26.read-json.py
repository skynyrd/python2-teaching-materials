import json

json_data=open('json-sample.json').read()

data = json.loads(json_data)
print(data)

print "********"
print data['glossary']
print "********"
print data['glossary']['title']
print "********"
print data['glossary']['GlossDiv']
print "********"
print data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm']
