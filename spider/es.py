from elasticsearch import Elasticsearch


def es():

    es = Elasticsearch([{'host':'10.40.2.100','port':9200}])
    es.indices.create(index='my_index',body='my_test',params=[{'a':'b','c':'d'}])
    a=es.get('my_index')
    print(a)
es()