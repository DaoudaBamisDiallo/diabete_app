#-------------------package------------------
# packages necessaires
import streamlit as st
import numpy as np
import pickle as pkl
import pandas as pd

#-------------modelisation et deployement----------------------------
# def main():
# description de l'application
st.image("datasets_bd/images/presnation.webp")
st.title("Welcome to Fast_Finding Diabete")
st.header("Réalisée par : Pro-Data_Consulting")
st.markdown(("FFD est une application est conçcue pour détecter très rapidement le diabete chez les femmes"))

#chagement du modele
def load_model():
    with open("datasets_bd/db/model_diabete.pkl","rb") as file:
        data = pkl.load(file)
    file.close()
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
col3,col4 = st.columns(2)
with col3 : 
    if st.button('Examiner le patient',type='secondary') :
        resultat= inference(Glucose,BMI,Age,DiabetesPedigreeFunction,BloodPressure,Pregnancies)
        if resultat[0] == 1:
            st.warning("Diabetique")
        elif resultat[0] == 0:
            st.success("Non diabetique")
        else :
            st.error("Le résultat de l'examen inconnu merci de bien saisir les information ou de consulter le médecin pour plus de detail")
with col4 :
    url ="https://ettienyann-diabete-diabete-tr9slg.streamlit.app/"
    st.button("[Retour à analyse](%s)" % url,type="primary")
# if __name__=='main':
# #   main()
        