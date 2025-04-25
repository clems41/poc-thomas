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
        result = self._run_query("SELECT nom FROM base_culture;")
        return ','.join([e[0] for e in result])

    def get_activites(self):
        result = self._run_query("SELECT nom FROM base_activite;")
        return ','.join([e[0] for e in result])

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
