import os

file_path = "Dades/HIVE_UNION_SUBDIR_1/000006_0"

# Intentar llegir-lo com a ORC
try:
    import pyorc
    with open(file_path, "rb") as file:
        reader = pyorc.Reader(file)
        print("És un fitxer ORC. Primeres files:")
        for i, row in enumerate(reader):
            print(row)
            if i == 5:  # Mostrem només les primeres 5 línies
                break
except Exception:
    print("No és un fitxer ORC.")

# Intentar llegir-lo com a Avro
try:
    import fastavro
    with open(file_path, "rb") as file:
        reader = fastavro.reader(file)
        print("És un fitxer Avro. Primeres files:")
        for i, record in enumerate(reader):
            print(record)
            if i == 5:
                break
except Exception:
    print("No és un fitxer Avro.")

# Intentar llegir-lo com a text
try:
    with open(file_path, "r", encoding="utf-8") as file:
        print("Primeres línies (si és text):")
        for i in range(5):
            print(file.readline().strip())
except Exception:
    print("No és un fitxer de text llegible.")
