import pandas as pd

df = pd.read_csv("C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\other\\Electronic_sales_Sep2023-Sep2024.csv",
                 delimiter=',', quotechar='"', header=0)

income_for_each_delivery_method = df.groupby ("Shipping Type")['Total Price'].sum().reset_index();
income_for_each_delivery_method.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_four.csv', index=False)

income_for_each_type_of_product = df.groupby ("Product Type")['Total Price'].sum().reset_index();
income_for_each_type_of_product.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_five.csv', index=False)

df['Order Month'] = pd.to_datetime(df["Purchase Date"]).dt.to_period('M')
income_for_each_month = df.groupby ('Order Month')["Add-on Total"].sum().reset_index()
income_for_each_month.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_six.csv', index=False)

df['Order Quarter'] = pd.to_datetime(df["Purchase Date"]).dt.to_period('Q')
income_for_each_quarter = df.groupby ('Order Quarter')["Add-on Total"].sum().reset_index()
income_for_each_quarter.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_seven.csv', index=False)