import pandas as pd

paths = [
    'C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_one.csv',
    'C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_two.csv',
    'C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_three.csv'
]

for path in paths:
    with open(path, 'w') as f:
        pass

df = pd.read_csv("C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\other\\Electronic_sales_Sep2023-Sep2024.csv",
                 delimiter=',', quotechar='"', header=0)

preferred_payment = df.groupby('Customer ID')['Payment Method'].agg(lambda x: x.mode()[0]).reset_index()
preferred_payment.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_one.csv', index=False)

total_spent = df.groupby('Customer ID')['Total Price'].sum().reset_index()
total_spent.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_two.csv', index=False)

addons_spent = df.groupby('Customer ID')['Add-on Total'].sum().reset_index()
addons_spent.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_three.csv', index=False)