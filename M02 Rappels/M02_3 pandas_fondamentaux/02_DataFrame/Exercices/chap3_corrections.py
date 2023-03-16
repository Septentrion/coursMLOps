# Bitcoins

import pandas as pd
bitcoins = pd.read_csv('../data/Cours_BTC2FEUR_-_Feuille_1.csv')

bitcoins

bitcoins['Date'] = pd.to_datetime(bitcoins['Date'])
bitcoins['Prix'] = bitcoins['Prix'].replace(
    to_replace=r'^1 BTC =(.*)€$', value='\\1', regex=True)
bitcoins['Prix'] = bitcoins['Prix'].astype(float)

bitcoins.plot(x='Date', y='Prix')

# todo


dataset = {
    'name': ['john', 'mary', 'peter', 'jeff', 'bill', 'lisa', 'jose'],
    'age': [23, 78, 22, 19, 45, 33, 20],
    'gender': ['M', 'F', 'M', 'M', 'M', 'F', 'M'],
    'state': ['Paris', 'Lille', 'Paris', 'Lille', 'Paris', 'Bordeaux', 'Bordeaux'],
    'num_children': [3, 0, 2, 4, 3, 1, 5],
    'num_pet': [5, 1, 0, 5, 2, 2, 3]
}

df = pd.DataFrame(dataset)
dfG = df.groupby(['state'])['state', 'num_children'].sum()
dfG.head()

# Ecart des ages par ville

df.groupby(['city'])['age'].apply(lambda x: x.max() - x.min())

# Boston
boston = pd.read_csv('data/boston.csv')

boston['TOTAL EARNINGS'] = boston['TOTAL EARNINGS'].str.replace(',', '')

boston = boston[boston['TOTAL EARNINGS'].str.contains('\d')]
boston['TOTAL EARNINGS'] = boston['TOTAL EARNINGS'].astype(float)
bostonGp = boston.groupby('DEPARTMENT_NAME')[
    'TOTAL EARNINGS'].agg(lambda x: x.max() - x.min())

bostonGp.sort_values(ascending=False)

##
dataset = {
    'name': ['john', 'mary', 'peter', 'jeff', 'bill', 'lisa', 'jose'],
    'married': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'yes'],
    'age': [23, 78, 22, 19, 45, 33, 20],
    'genre': ['M', 'F', 'M', 'M', 'M', 'F', 'M'],
    'state': ['Paris', 'Lille', 'Paris', 'Lille', 'Paris', 'Bordeaux', 'Bordeaux'],
    'num_children': [3, 0, 2, 4, 3, 1, 5],
    'num_pet': [5, 1, 0, 5, 2, 2, 3]
}
# Question 1
df = pd.DataFrame(dataset)
nb_child_state = df.groupby('state')['num_children']
print(nb_child_state.sum(), "\n")
# Question 2
nb_child_state_married = df[df.married == 'yes'].groupby('married')[
    'num_children']
print(nb_child_state_married.sum(), "\n")
# Question 3
nb_child_state_notmarried = df[df.married == 'no'].groupby('married')[
    'num_children']
print(nb_child_state_notmarried.sum(), "\n")
if nb_child_state_married.sum().sum() > nb_child_state_notmarried.sum().sum():
    print("Oui", "\n")
else:
    print("Non")
​
# Question 4
nb_pet_married = df.groupby('married')['num_pet']
print(nb_pet_married.sum(), "\n")
m_no, m_yes = nb_pet_married.sum()
if m_yes > m_no:
    print("Oui", "\n")
else:
    print("Non")
# Question 5
print(df[df['married'] == 'no']['num_children'].mean())
