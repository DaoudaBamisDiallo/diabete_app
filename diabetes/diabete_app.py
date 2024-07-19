# packages necessaires
from configs import presentation
from configs import loading_dataset
from configs import showing_data
from configs import AED
from configs import appli


def main():
    #---------------------------Présentation-----------------------------------------------
    presentation()
    #------------------------chargement et affichage de la base de données------------------------------
    data=loading_dataset()
    showing_data(data)

    # ------------------------------analyse exploratoire des données-----------------------
    AED(data)
    
    # gener l'application
    appli()

if __name__=="__main__":
    main()