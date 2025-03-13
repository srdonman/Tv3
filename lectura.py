import pandas as pd

# Definir el fitxer de dades
file_path = "Dades/HIVE_UNION_SUBDIR_1/000006_0"

# Definir les columnes segons el .txt
columnes = [
    "st_usuari_id", "st_player_id", "max_sn", "n_sn", "max_an", "st_agrupador_live",
    "st_agrupador_contingut_id", "st_agrupador_arafem_start_time", "st_agrupador_canal_nom",
    "st_agrupador_REPRODUCCIO", "bo_es_diferit", "bo_canal_sense_arafem", "bo_en_reproduccio",
    "min_data", "max_data", "min_data_timestamp", "max_data_timestamp",
    "min_counter", "max_counter", "min_time_code", "max_time_code",
    "min_id_raw", "max_id_raw", "min_id_bloc", "max_id_bloc",
    "id_bloc_consolidacio", "bi_segons_consum", "bi_marques",
    "n_blocs", "de_55_consum", "de_ratio_consum_marques",
    "SUMA_DIFERENCIES", "COLUMNES_AMB_DIFERENCIES", "RESUM_DIFERENCIES_AMB_VALORS",
    "bi_id_setting", "usuari_id", "player_id", "live", "difftime",
    "sn", "an", "ui", "ri", "versio_app", "versio_player", "casting",
    "font", "media_tipus", "producte_id", "format", "qualitat",
    "contingut_id", "contingut_variant", "reproduccio_id", "sbt", "sbtd",
    "debug", "debug_message", "debug_request", "debug_type", "debug_data",
    "ref", "loc", "ip", "geoip_ciutat", "geoip_codi_postal",
    "geoip_coordenades_x", "geoip_coordenades_y", "geoip_pais",
    "geoip_regio", "provincia_id", "provincia_nom", "canal_codi",
    "canal_codi_norma", "canal_nom", "programa_id", "durada",
    "programa_nom", "programa_capitol", "media_titol", "tematica",
    "arafem_tipus", "arafem_codi_canal", "arafem_codi_programa",
    "arafem_titol_programa", "arafem_capitol", "arafem_titol_capitol",
    "arafem_codi_op", "arafem_titol_tdt", "arafem_start_time",
    "arafem_end_time", "arafem_durada", "arafem_graella",
    "arafem_subtitulat_catala", "arafem_subtitulat_vo",
    "arafem_audio_descripcio", "arafem_classificacio_grup",
    "arafem_classificacio_grup_id", "arafem_classificacio_subgrup",
    "arafem_classificacio_subgrup_id", "arafem_tematica",
    "arafem_classificacio_tematica_dvb", "arafem_target",
    "arafem_target_id", "arafem_codi_etic", "arafem_drets_cat",
    "arafem_drets_esp", "arafem_drets_mon", "arafem_contribucio",
    "arafem_destacat", "arafem_destacat_imatge", "arafem_logo",
    "arafem_reemissio", "arafem_codi_hashtag", "arafem_hashtag",
    "mrec_id", "mrec_modul", "mrec_posicio", "mrec_default",
    "mrec_tipus_test", "spm_id", "spm_tipus", "spm_modul",
    "spm_posicio", "dispositiu_dia", "dispositiu_hora",
    "dispositiu_ip", "dispositiu_geo", "dispositiu_profile_aplicacio",
    "dispositiu_engine_versio", "dispositiu_accepta_cookies",
    "dispositiu_software_versio", "dispositiu_model",
    "dispositiu_vendor", "dispositiu_norma", "dispositiu_cpu",
    "dispositiu_browser_versio", "dispositiu_browser_nom",
    "dispositiu_tipus", "dispositiu_engine_nom",
    "dispositiu_hardware_versio", "dispositiu_useragent",
    "dispositiu_regio"
]

# Carregar el fitxer en un DataFrame, assignant les columnes correctes
df = pd.read_csv(file_path, sep="\x01", names=columnes, dtype=str)

# Mostrar les primeres files per validar
print(df.head())
