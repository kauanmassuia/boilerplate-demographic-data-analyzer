import pandas as pd

def calculate_demographic_data(print_data=True):
    # Lê os dados do arquivo CSV
    df = pd.read_csv('adult.data.csv')

    # Quantas pessoas de cada raça estão representadas no dataset?
    # Aqui vai ser uma série do Pandas com o nome da raça como índice.
    race_count = df['race'].value_counts()

    # Qual é a idade média dos homens?
    # Filtra pelo sexo 'Male' e tira a média das idades.
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # Qual a porcentagem de pessoas que têm um diploma de Bacharelado?
    # Conta quantos têm 'Bachelors' e divide pelo total, multiplicando por 100 pra virar porcentagem.
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 1)

    # Qual a porcentagem de pessoas com educação avançada (Bachelors, Masters ou Doctorate) que ganham mais de 50K?
    # E qual a porcentagem de pessoas sem educação avançada que ganham mais de 50K?
    
    # Filtra quem tem e quem não tem educação avançada
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Calcula a porcentagem de pessoas com educação avançada e salário >50K
    higher_education_rich = round(len(higher_education[higher_education.salary == '>50K']) / len(higher_education) * 100, 1)
    lower_education_rich = round(len(lower_education[lower_education.salary == '>50K']) / len(lower_education) * 100, 1)

    # Qual o menor número de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()

    # Qual a porcentagem das pessoas que trabalham o mínimo de horas por semana e ganham mais de 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers[num_min_workers.salary == '>50K']) / len(num_min_workers) * 100, 1)

    # Qual país tem a maior porcentagem de pessoas que ganham mais de 50K?

    # Conta as pessoas por país
    countries = df['native-country'].value_counts()
    # Conta os ricos por país
    rich_countries = df[df['salary'] == '>50K']['native-country'].value_counts()

    # Calcula a porcentagem e encontra o país com maior porcentagem de ricos
    highest_earning_country = (rich_countries / countries * 100).idxmax()
    highest_earning_country_percentage = round(rich_countries / countries * 100, 1).max()

    # Qual é a ocupação mais comum entre os que ganham mais de 50K na Índia?
    rich_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = (rich_indians['occupation'].value_counts()).idxmax()

    # Não mexer na parte de baixo

    if print_data:
        print("Número de cada raça:\n", race_count) 
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem com diploma de Bacharelado: {percentage_bachelors}%")
        print(f"Porcentagem de pessoas com educação avançada que ganham >50K: {higher_education_rich}%")
        print(f"Porcentagem de pessoas sem educação avançada que ganham >50K: {lower_education_rich}%")
        print(f"Menor número de horas trabalhadas: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre os que trabalham menos horas: {rich_percentage}%")
        print("País com maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de ricos em um país: {highest_earning_country_percentage}%")
        print("Ocupação mais comum entre os ricos na Índia:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
