#-------------------package------------------
# packages necessaires
import streamlit as st
import numpy as np
import  joblib
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact


#---------------------------Présentation-----------------------------------------------
def presentation():
    st.sidebar.markdown("Présentation du projet")
    if st.sidebar.checkbox("Problematique",False):
        st.image("datasets_bd\images\problematique.jpeg")
        url ="https://ettienyann-diabete-diabete-tr9slg.streamlit.app/"
        st.button("[Aller au laboratoire](%s)" % url,type="primary")


#------------------------chargement et affichage de la base de données------------------------------

#fonction de chagement de la base de données
@st.cache_data(persist=True)
def loading_dataset ():
    file="datasets_bd/db/diabetes.csv"
    data = pd.read_csv(file)
    return data

#affichage des 100 premiere observation
def showing_data(data):  
    # affichage des  100 premiere observation
    st.sidebar.markdown("Analyse Exploratoire des données")
    df_sample = data.sample(100)
    if st.sidebar.checkbox("Afficher les données brut",False):
        st.subheader("Jeu de données de diabete : Echantillons de 100 observations")
        st.write(df_sample)


# ------------------------------analyse exploratoire des données-----------------------
def AED(data):
    
        # Analyse Univariée
    cols=data.columns.tolist()
    #-------fonction d'analyse univariée-----------
    def hist_plot(var):
        fig,ax=plt.subplots(figsize=(10,5))
        ax = sns.histplot(x=data[var], kde=True).set_title("Histogramme de "+str(var))
        st.pyplot(fig)

    #---------fonction d'analyse bivariée-----------

    def cat_plot(a):
        fig,ax=plt.subplots()
        ax = sns.boxplot(y=data[a],x=data['Outcome'])
        st.pyplot(fig)

    #---------fonction d'analyse multivariée-----------

    def rel_plot(a,b,c):

        if c=="scatter":
            fig,ax=plt.subplots()
            ax = sns.scatterplot(x=a, y=b, hue='Outcome',data=data)
            st.pyplot(fig)

        if c=="line":
            fig,ax=plt.subplots()
            ax = sns.lineplot(x=a, y=b, hue='Outcome',data=data)
            st.pyplot(fig)

    # menu
        
    
    if st.sidebar.checkbox("Analyse Univariée",False):
        st.title("Distribution des variables")
        # Analyse Univariée
        col = st.selectbox("Choisir la variables a visualiser",cols,key="univare")
        hist_plot(col)
        
    
    if st.sidebar.checkbox("Analyse Bivariée",False):
        st.title("Distrution des variables en fonction de la variable cible")
        # Analyse biivariée
        col =st.selectbox("Choisir la variables a visualiser",cols,key="bivare")
        cat_plot(col)
        
    
    if st.sidebar.checkbox("Analyse Multivariée",False):
        st.title("Reletion entre les variables")
        col1,col2,col3 = st.columns(3)
        with col1:
            x =st.selectbox("Variable en abscisse",cols,key="x")
        with col2:
            y =st.selectbox("Variables en ordonnée",cols,key="y")
        with col3:
            c =st.selectbox("Graphique",["scatter","line"],key="c")
        # Analyse multiiivariée
        rel_plot(x,y,c)

#-------------modelisation et deployement----------------------------
def modeling():

        #chagement du modele
        def load_model():
            data = joblib.load("datasets_bd/db/model_diabete.joblib")
            return data

        model_diabete = load_model()
        # fonction d'inference
        def inference(Glucose,BMI,Age,DiabetesPedigreeFunction,BloodPressure,Pregnancies):
            df = np.array([Glucose,BMI,Age,DiabetesPedigreeFunction,BloodPressure,Pregnancies])
            diabetique = model_diabete.predict(df.reshape(1,-1))
            return diabetique
        # saisie des iinformations du patience
                
        st.header("Informations de la patiente")
        col1,col2 = st.columns(2)
        with col1 : 
            Glucose = st.number_input(label="Taus du glucose",min_value=0.0,max_value=1.0,value=0.621212)
            Age = st.number_input(label="L'age ",min_value=0.0,max_value=1.0,value=0.166667)
            BloodPressure = st.number_input(label="Tension arterielle diastolique",min_value=0.0,max_value=1.0, value=0.631579)
           
        with col2 :
            BMI = st.number_input(label="Indice du masse corporelle",min_value=0.0,max_value=1.0,value=0.570681)
            DiabetesPedigreeFunction = st.number_input(label="Fonction généalogie du diabète",min_value=0.0,max_value=1.0,value=0.137939)
            Pregnancies = st.number_input(label="Nombre de grossse",min_value=0.0,max_value=1.0,value=0.205882)
    
            # axamianation du patient
        if st.button('Examiner le patient') :
            resultat= inference(Glucose,BMI,Age,DiabetesPedigreeFunction,BloodPressure,Pregnancies)
            if resultat[0] == 1:
                st.warning("Diabetique")
            elif resultat[0] == 0:
                st.success("Non diabetique")
            else :
                st.error("Le résultat de l'examen inconnu merci de bien saisir les information ou de consulter le médecin pour plus de detail")
def appli():
    st.sidebar.markdown("Utilisation de l'application")
    if st.sidebar.checkbox("Application",False):
        # description de l'application
        st.subheader("*"*58)
        st.image("datasets_bd\images\presnation.webp")
        st.title("Welcome to Fast_Finding Diabete")
        st.header("Réalisée par : Pro-Data_Consulting")
        st.markdown(("FFD est une application est conçcue pour détecter très rapidement le diabete chez les femmes"))
        
        if st.sidebar.radio("Visiter le patience",["Aprés","Maintenant"])=="Maintenant":
            modeling()
        