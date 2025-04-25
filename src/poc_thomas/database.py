import psycopg2

class DatabaseManager:
    # Configuration de la connexion
    config = {
        'dbname': 'sebania',
        'user': 'sebania',
        'password': 'sebania',
        'host': 'localhost',
        'port': 5432
    }

    def __init__(self):
        try:
            # Connexion à la base
            conn = psycopg2.connect(**self.config)
            cursor = conn.cursor()
            # Fermeture de la connexion
            cursor.close()
            conn.close()

        except Exception as e:
            print("Erreur lors de la connexion ou de la requête :", e)

    def get_cultures(self):
        return self._run_query("SELECT id,nom FROM base_culture;")

    def get_activites(self):
        return self._run_query("SELECT id,nom,mots_cles FROM base_activite;")

    def _run_query(self, query):
        # Connexion à la base
        conn = psycopg2.connect(**self.config)
        cursor = conn.cursor()

        # Exécution de la requête SQL
        cursor.execute(query)

        # Récupération des résultats
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return results
