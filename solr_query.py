from urllib3 import *
from urllib.request import urlopen

connection = urlopen('http://localhost:8983/solr/articles/select?q=articles.description:duke&wt=python')
response = eval(connection.read())

print (response['response']['numFound'], "documents found.")

# Print the name of each document.


print(response['response']['docs'][0]['articles.title'][0])
print(response['response']['docs'][0]['articles.description'][0])
print(response['response']['docs'][0]['articles.url'][0])
# for document in response['response']['docs']:
#   print ("  Name =", document['articles.title'])
