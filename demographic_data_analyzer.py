#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

def calculate_demographic_data(print_data=True):
    # Column names
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]

    
    df = pd.read_csv(
        r'c:/users/srinivas/downloads/dataset/adult/adult.data',
        header=None,
        names=column_names,
        skipinitialspace=True
    )

    
    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)


    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    higher_education_rich = round((df[higher_edu & (df['salary'] == '>50K')].shape[0] / df[higher_edu].shape[0]) * 100, 1)
    lower_education_rich = round((df[lower_edu & (df['salary'] == '>50K')].shape[0] / df[lower_edu].shape[0]) * 100, 1)

    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_earnings.idxmax()
    highest_earning_country_percentage = round(country_earnings.max() * 100, 1)

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


# In[3]:





# In[5]:





# In[ ]:




