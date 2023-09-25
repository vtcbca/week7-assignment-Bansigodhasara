import csv
import pandas as pd
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
with open("C:\\sqlite3\\csv\\selling.csv","w",newline='') as csvfile:
    data=csv.writer(csvfile)
    data.writerow(header)

    l = []
with open("c:\\sqlite3\\csv\\selling.csv", 'a', newline="") as file:
    insert = csv.writer(file)
    for i in range(12):
        prod_no = input("Enter Product Number: ")
        prod_name = input("Enter Product Name: ")
        jan = int(input("Enter January Sales: "))
        feb = int(input("Enter February Sales: "))
        mar = int(input("Enter March Sales: "))
        apr = int(input("Enter April Sales: "))
        may = int(input("Enter May Sales: "))
        jun = int(input("Enter June Sales: "))
        data = [prod_no, prod_name, jan, feb, mar, apr, may, jun]
        l.append(data)
    insert.writerows(l)

df = pd.read_csv("c:\\sqlite3\\csv\\selling.csv")
df.columns = ['Product_No', 'Product_Name', 'January', 'February', 'March', 'April', 'May', 'June']
print(df)

df['Total_Sell'] = df[['January', 'February', 'March', 'April', 'May', 'June']].sum(axis=1)
df['Average_Sell'] = df[['January', 'February', 'March', 'April', 'May', 'June']].mean(axis=1)

print(df['Total_Sell'])

print(df['Average_Sell'])

for i in range(2):
    new_data = {}
    for column in header:
        new_data[column] = input(f"Enter value for {column}: ")
    df = df.append(new_data, ignore_index=True)

new_rows = [
    [15, 'Cable', 1290, 7128, 7456, 4325, 3874, 2002],
    [16, 'Projector', 1140, 1148, 2260, 2245, 2256, 2221]
]
df = pd.concat([df.iloc[:3], pd.DataFrame(new_rows, columns=header), df.iloc[3:]]).reset_index(drop=True)

print(new_rows)

print("FIRST FIVE ROWS")
print(df.head())

print("LAST 5 ROWS")
print(df.tail())

print("ROWS BETWEEN 6 TO 10")
print(df.iloc[6:11])

print("Product Names:")
print(df["Product_Name"])

print("January Sales:")
print(df[["Product_No", "Product_Name", "January"]])

print("Records based on condition:")
filtered_df = df[(df["January"] > 5000) & (df["February"] > 8000)]
print(filtered_df[["Product_No", "Product_Name"]])

print("Sorted by Product Name:")
print(df.sort_values(by="Product_Name"))

print("Odd Rows:")
print(df.iloc[1::2])

print("Alternate Rows:")
print(df.iloc[::2])

