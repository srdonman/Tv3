import os
import pandas as pd
import shutil

# Definir les rutes
dades_dir = "Dades"
dades_netes_dir = "Dades_netes"

# Crear la carpeta Dades_netes i les subcarpetes
if not os.path.exists(dades_netes_dir):
    os.mkdir(dades_netes_dir)

for subdir in os.listdir(dades_dir):
    subdir_path = os.path.join(dades_dir, subdir)
    if os.path.isdir(subdir_path):
        subdir_netes_path = os.path.join(dades_netes_dir, subdir)
        if not os.path.exists(subdir_netes_path):
            os.mkdir(subdir_netes_path)

        # Processar cada arxiu dins de la subcarpeta
        for file_name in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file_name)
            if os.path.isfile(file_path):
                # Llegir el fitxer amb el separador especial
                df = pd.read_csv(file_path, sep="\x01", header=None, dtype=str)

                # Crear la ruta de sortida per al fitxer processat
                output_file_path = os.path.join(subdir_netes_path, file_name + "_transformat.csv")

                # Desar el fitxer transformant-lo a CSV
                df.to_csv(output_file_path, index=False, header=False)

                print(f"Fitxer processat: {output_file_path}")

print("Tots els fitxers s'han processat i desat correctament.")
