import os

dossier = '/chemin/vers/votre/dossier'  

def rename(dossier):
    for fichier in os.listdir(dossier):
        if os.path.isfile(os.path.join(dossier, fichier)):
            nouveau_nom = fichier.replace('-', '_').replace(' ', '_')
            ancien_chemin = os.path.join(dossier, fichier)
            nouveau_chemin = os.path.join(dossier, nouveau_nom)
            os.rename(ancien_chemin, nouveau_chemin)
            print(f"Renommé : {fichier} -> {nouveau_nom}")

rename(dossier)
