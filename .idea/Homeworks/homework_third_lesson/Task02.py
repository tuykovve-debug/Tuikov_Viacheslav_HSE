import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv("C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\other\\Electronic_sales_Sep2023-Sep2024.csv",
                 delimiter=',', quotechar='"', header=0)

income_for_each_delivery_method = df.groupby ("Shipping Type")['Total Price'].sum().reset_index();
income_for_each_delivery_method.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_four.csv', index=False)
plt.figure(figsize=(10,6))
plt.plot(income_for_each_delivery_method['Shipping Type'], income_for_each_delivery_method['Total Price'], marker='o')
plt.xlabel('Тип доставки (Shipping Type)')
plt.ylabel('Общая сумма (Total Price)')
plt.title('Общая сумма по типам доставки')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%06d'))
plt.tight_layout()
plt.show()

income_for_each_type_of_product = df.groupby ("Product Type")['Total Price'].sum().reset_index();
income_for_each_type_of_product.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_five.csv', index=False)
plt.figure(figsize=(10,6))
plt.plot(income_for_each_type_of_product['Product Type'], income_for_each_type_of_product['Total Price'], marker='o')
plt.xlabel('Тип продукта (Product Type)')
plt.ylabel('Общая сумма (Total Price)')
plt.title('Общая сумма по типам продуктов')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%06d'))
plt.tight_layout()
plt.show()

df['Order Month'] = pd.to_datetime(df["Purchase Date"]).dt.to_period('M')
income_for_each_month = df.groupby('Order Month')["Add-on Total"].sum().reset_index()
income_for_each_month.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_six.csv', index=False)
income_for_each_month['Order Month'] = income_for_each_month['Order Month'].astype(str)
plt.figure(figsize=(10,6))
plt.plot(income_for_each_month['Order Month'], income_for_each_month['Add-on Total'], marker='o')
plt.xlabel('Месяц (Order Month)')
plt.ylabel('Общая сумма за доп. услуги (Add-on Total)')
plt.title('Общая сумма за доп. услуги по месяцам')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%06d'))
plt.tight_layout()
plt.show()

df['Order Quarter'] = pd.to_datetime(df["Purchase Date"]).dt.to_period('Q')
income_for_each_quarter = df.groupby('Order Quarter')["Add-on Total"].sum().reset_index()
income_for_each_quarter.to_csv('C:\\Users\\tujko\\IdeaProjects\\Tuikov_Viacheslav_HSE\\.idea\\Homeworks\\homework_third_lesson\\data_quarter.csv', index=False)
income_for_each_quarter['Order Quarter'] = income_for_each_quarter['Order Quarter'].astype(str)
plt.figure(figsize=(10,6))
plt.plot(income_for_each_quarter['Order Quarter'], income_for_each_quarter['Add-on Total'], marker='o')
plt.xlabel('Квартал (Order Quarter)')
plt.ylabel('Общая сумма за доп. услуги (Add-on Total)')
plt.title('Общая сумма за доп. услуги по кварталам')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%06d'))
plt.tight_layout()
plt.show()