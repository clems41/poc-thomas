import os
from datetime import datetime
from os.path import isfile

from poc_thomas.short_version.crew import ShortVersionCrew
from poc_thomas.transcriptor import Transcriptor

def run_crew(filename: str, filepath: str, output_directory: str):
    print("----------------------------   {}    ----------------------------".format(filename))
    filename_without_extension = filename.replace(".mp3", "")
    crew = ShortVersionCrew(filename=filename_without_extension, output_directory=output_directory)
    # CONFIG
    cultures = "Ail,Artichaut,Asperge,Aubergine,Betterave,Blette,Brocoli,Butternut,Carotte,Chou chinois,Chou frisé,Chou kale,Chou rouge,Chou-fleur,Concombre,Courge musquée,Courge spaghetti,Courgette,Céleri branche,Céleri-rave,Endive,Fenouil,Haricot vert,Laitue,Manioc,Melon,Mâche,Navet,Oignon,Panais,Pastèque,Patate douce,Patidou,Piment,Poireau,Poivron,Pomme de terre,Potimarron,Potiron,Pâtisson,Radis,Roquette,Tomate,Épinard,Engrais verts,Fleurs,Radis noir,Chou-rave"
    activites = "Production de plant,Travail du sol,Apport de MO (Amender),Fertilisation,Paillage,Bâchage,Semis direct,Plantation,Gestion climatique,Gestion des bioagresseurs,Irrigation,Désherbage,Taille,Palissage,Destruction de culture,Suivi de culture,Récolte,Nettoyage,Livrer,Stockage,Charger / Décharger,Communication / Marketing,Marché,Vente directe,Panier AMAP,Gestion des stocks,Préparation de commande,Comptabilité,Administratif,Planifier,Veille,Achat / Commande,Ranger,Accueil du public,Réparer,Construire,Aménager,Entretenir,Formation,Accompagnement,Production de compost,Gestion des intrants,Réunions,Volailles,Floriculture,Brassiculture,Apiculture,Champignons,Boissons,Conserves,Boulangerie,Verger,Semences,Atelier pédagogique,Auxiliaires de culture,Transformation,Activités syndicales"
    unites = "kg,pièces,bottes,plants,caisses,m²,mètres,hectares,pots,terrines,plaques,paniers,godets,litres,lignes"

    # TRANSCRIPTION
    transcriptor = Transcriptor(model_path=output_directory)
    transcription = transcriptor.transcribe(filepath)
    with open(os.path.join(output_directory, "1_" + filename_without_extension + "_transcription.txt"), "w") as text_file:
        text_file.write(transcription)

    # INPUT
    inputs = {
        'transcription': transcription,
        'cultures': str(cultures),
        'activites': str(activites),
        'unites': str(unites)
    }

    # EXECUTION
    start_time = datetime.now()
    crew.crew().kickoff(inputs=inputs)
    end_time = datetime.now()
    duration = end_time - start_time
    print("Durée de l'exécution : {} minutes {} secondes".format(duration.seconds // 60, duration.seconds % 60))
    print("--------------------------------------------------------")

    # CLEANUP OUTPUT
    # Read in the file
    with open(crew.final_file_path, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('```json', '')
    filedata = filedata.replace('```', '')

    # Write the file out again
    with open(crew.final_file_path, 'w') as file:
        file.write(filedata)

def main():
    """
    Run the crew.
    """
    input_directory = os.path.abspath(os.path.join(os.getcwd(), "../../input/"))
    output_directory = os.path.abspath(os.path.join(os.getcwd(), "../../output/"))
    # loop over all files in 'input' directory
    for file in os.listdir(input_directory):
        if isfile(os.path.join(input_directory, file)):
            run_crew(file, os.path.join(input_directory, file), output_directory)

if __name__ == '__main__':
    main()
