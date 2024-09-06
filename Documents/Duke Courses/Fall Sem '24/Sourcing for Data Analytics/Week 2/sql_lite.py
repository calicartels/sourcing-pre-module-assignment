import sqlite3
import pandas as pd

## connecting to the database : 

initialization = sqlite3.connect("tips.db") # name of the database


# reading the tips database using the pandas library:

df = pd.read_csv("aipi510-fall24/data/tips.csv")
df.head()


# Loading the data file to the SQL database :

df.to_sql("tips", initialization, if_exists = "replace")  ## name of the db table(new), connection variable, command to work out what happens when the data/ table exits already.


# Everytime you want to send in a query, you have to create a cursor object:

cursor = initialization.cursor() # its essentially a pointer


# printing all the values in as a table before working on them:

cursor.execute("SELECT * FROM tips")
items = cursor.fetchone()

for item in items:
    print(item)

print("-------------------")
cursor.execute("SELECT rowid, * FROM tips")
items = cursor.fetchmany()

for item in items:
    print(item)

print("-------------------")

# 1. Retrieve the average tip percentage for each day of the week

query = """
SELECT 
    day,
    AVG((tip / total_bill) * 100) AS average_tip_percentage
FROM 
    tips
GROUP BY 
    day
ORDER BY 
    CASE day
        WHEN 'Sun' THEN 1
        WHEN 'Mon' THEN 2
        WHEN 'Tue' THEN 3
        WHEN 'Wed' THEN 4
        WHEN 'Thu' THEN 5
        WHEN 'Fri' THEN 6
        WHEN 'Sat' THEN 7
    END;
"""
cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(f"{row[0]}: {row[1]:.2f}% average tip")


print("-----------")

# 2. Find the maximum and minimum total bull amounts

query = """
SELECT MAX(total_bill),
MIN(total_bill)
FROM tips

"""

cursor.execute(query)
results = cursor.fetchall()

print(f"maximum = {results[0][0]} and minimum = {results[0][1]}")
print("-----------")

# 3. Count the number of parties for each size

query = """
SELECT 
    size, 
    COUNT(*) AS party_count
FROM 
    tips
GROUP BY 
    size;
"""

cursor.execute(query)
results = cursor.fetchall()


for size,count in results:
    print(f"size = {size} and count = {count}")
print("-----------")

# 4. Retrieve the total bill and tip for parties of size 4 or more, where the tip percentage is greater than 15%

query = """
SELECT 
    total_bill, 
    tip 
FROM
    tips
WHERE 
size > 4 
AND 
(tip / total_bill) * 100 > 15;

"""

cursor.execute(query)
results = cursor.fetchall()

for i in results:
    print(f"total bill = {i[0]} and tips = {i[1]}")
print("-----------")


# 5. Retrieve the total bill, tip amount, and tip percentage for each combination of day and time, sorted by tip percentage in descending order

query = """
SELECT 
    total_bill,
    tip,
    (tip / total_bill) * 100 as tip_percentage,
    day,
    time
FROM 
    tips
ORDER BY 
    tip_percentage DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

for i in results:
    print(f"Day: {i[3]}, Time: {i[4]}, Total Bill: {i[0]}, Tip: {i[1]}, Tip Percentage: {i[2]:.2f}%")
print("-----------")


# 6. Find the average tip percentage for each combination of day, time, and smoker status
query = """
SELECT 
    AVG((tip / total_bill) * 100) as avg_tip_percentage,
    day,
    time,
    smoker
FROM 
    tips
GROUP BY
    day,
    time,
    smoker;
"""
cursor.execute(query)
results = cursor.fetchall()

for i in results:
    print(f"Average tip percentage = {i[0]} day = {i[1]}, time = {i[2]}, smoker = {i[3]}")
print("_______")


# 7. Retrieve the total bill, tip amount, 
# and tip percentage for each sex, sorted by total bill in descending order, and limit the results to the top 5 records

query = """
SELECT 
    total_bill,
    tip,
    (tip / total_bill) * 100 as tip_percentage,
    sex
FROM 
    tips
GROUP BY
    sex
ORDER BY
    total_bill;
"""
cursor.execute(query)
results = cursor.fetchall()

for i in results:
    print(f"sex = {i[3]}, total bill = {i[0]} , tip = {i[1]}, tip_percentage = {i[2]}")
print("_______")