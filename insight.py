### Setting up environment
# python -m virtualenv myenv
# source myenv/bin/activate
# pip freeze > requirements.txt
### Running after cloning 
# python -m virtualenv myenv
# python -m pip install -r requirements.txt
# python -m idlelib.idle
### Extract dataset from
# soccer-spi: https://data.fivethirtyeight.com/

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sys

"""
### QUEBEC COVID 19 DEATHS BY CATEGORIES (AGE, REGION)

Reference: https://www.donneesquebec.ca/recherche/dataset/covid-19-portrait-quotidien-des-cas-confirmes

Details: Quebec provides data that categorizes cumulative cases, deaths by region & age 

"""

myfile1 = './dataset/COVID19_Qc_RapportINSPQ_VigieCategories.csv'
df1 = pd.read_csv(myfile1, index_col=0)



dfDecesCum = df1[["Categorie","Nb_Deces_Cumulatif_Total"]] 

fig = dfDecesCum.plot(x='Categorie',y='Nb_Deces_Cumulatif_Total', kind='bar')
plt.title("Cumulative Covid-19 deaths in Quebec as of TBD by groups")

#Setup xtick to be more readable
ax = plt.gca()
ax.tick_params(axis='x',direction='in',pad=-300)

"""
ax=plt.gca()
rects = ax.patches

labels = dfDecesCum["Categorie"]

for rect,label in zip(rects,labels):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center",va="bottom",rotation=90
    )
"""

plt.show(block=False)

dfCasesCum = df1[["Categorie","Nb_Cas_Cumulatif"]]

fig2 = dfCasesCum.plot(x='Categorie',y='Nb_Cas_Cumulatif', kind='bar')
plt.title("Cumulative Covid-19 cases in Quebec as of TBD by groups")

#Setup xtick to be more readable
ax = plt.gca()
ax.tick_params(axis='x',direction='in',pad=-300)

plt.show(block=False)


"""
### QUEBEC HOSPITALIZATION BY AGE AND VACCINE STATUS

Reference: https://www.donneesquebec.ca/recherche/dataset/covid-19-portrait-quotidien-des-hospitalisations#

Details: Read the PDF to determine (snapshot? cumulative?) 

"""


myfile2 = './dataset/COVID19_Qc_RapportINSPQ_HospitalisationsSelonStatutVaccinalEtAge.csv'
df2 = pd.read_csv(myfile2, index_col=0)


"""
Data is organized as...
Date         GrAge_Admission  Status_Vaccinal      Nb_Nvelles_Hosp
2021-07-18    0-9 ans          Non-vaccine         0 
                               Vaccine 1 dose
                               Vaccine 2 doses
"""


# Overview of hospitalization by Status & Age
HospByStatus    = df2.groupby('Statut_Vaccinal')['Nb_Nvelles_Hosp'].sum()
HospByAge       = df2.groupby('GrAge_Admission')['Nb_Nvelles_Hosp'].sum() 

"""
figA = HospByStatus.plot(kind='bar')
plt.title('Using GroupBy to find sum of Hospitalized by Vaccine Status')
plt.show()

figB = HospByAge.plot(kind='bar')
plt.title('Using GroupBy to find sum of Hospitalized by Age')
plt.show()
"""

# Experiment: Split the Age distribution by vaccination status
dfA         = df2[(df2["Statut_Vaccinal"]=="Non-vacciné")]
HospByAgeA  = dfA.groupby('GrAge_Admission')['Nb_Nvelles_Hosp'].sum() 

dfB         = df2[(df2["Statut_Vaccinal"]=="Vacciné 1 dose")]
HospByAgeB  = dfB.groupby('GrAge_Admission')['Nb_Nvelles_Hosp'].sum() 

dfC         = df2[(df2["Statut_Vaccinal"]=="Vacciné 2 doses")]
HospByAgeC  = dfC.groupby('GrAge_Admission')['Nb_Nvelles_Hosp'].sum() 

# Subplots
fig,axes = plt.subplots(nrows=2,ncols=1,sharex=True)
fig.suptitle("Comparing Hospitalization Vaxx vs. Non-Vaxx")
plt.subplot(2,1,1)
HospByAgeA.plot(kind='bar')
plt.ylabel("Non-vacciné")
plt.grid(visible=True)

### Excluding the 1 dose cases because they are so few
#plt.subplot(3,1,2)
#HospByAgeB.plot(kind='bar')
#plt.ylabel("Vacciné 1 dose")
#plt.grid(visible=True)

plt.subplot(2,1,2)
HospByAgeC.plot(kind='bar')
plt.ylabel("Vacciné 2 doses")
plt.grid(visible=True)

#Fixing xticks to be visible
ax = plt.gca()
ax.tick_params(axis='x',direction='in',pad=0,rotation=45)
plt.show(block=False)

"""
### APPENDIX
"""
"""
1. Useful for plotting tick_params neater

ax=plt.gca()
rects = ax2.patches

labels = dfDecesCum["Categorie"]

for rect,label in zip(rects,labels):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center",va="bottom",rotation=90
    )

2. Useful for noting time that data was parsed

import datetime
x = datetime.datetime.now()
x.strftime("%x")

3. Useful to potentially query data with variables Age, Status 

# ENTER QUERY CRITERIA
Age     = "20-29 ans"
Status  = "Vacciné 2 doses"

# Experiment #1: Visualizing data that matches our query criteria
dfSub = df2[(df2["GrAge_Admission"] == Age ) & (df2["Statut_Vaccinal"] == Status )]
dfAgeVacc = pd.concat([dfSub.Nb_Nvelles_Hosp.value_counts()],axis=1).fillna(0).sum(axis=1)

fig3 = dfAgeVacc.plot(kind='bar')
plt.title("Age: " + Age + " Vaccine Status: " + Status)
plt.xlabel("# of Hospitalisations")
plt.show(block=False)


"""
