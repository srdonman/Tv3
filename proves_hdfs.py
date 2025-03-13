from hdfs import InsecureClient

# Connexió al servidor HDFS
client = InsecureClient('http://NamenodeHA:50070')  # Canvia el port si és necessari

# Llegir un fitxer des d'HDFS
with client.read('/enterprise/matr/hbbtv_ip_audiencia_cons.csv', encoding='utf-8') as reader:
    data = reader.read()
    print(data[:500])  # Mostra les primeres 500 lletres del fitxer
