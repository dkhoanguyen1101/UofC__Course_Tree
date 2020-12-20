import pyodbc #sql server
#connect to server
import pandas as pd
import csv

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-H322HOI;'
                      'Database=UofC_Tree_Apps;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

def csv_from_table(table_name, file_name, code):
    

    sql = f"select * from {table_name}"
    cursor.execute(sql)
    all_rows = cursor.fetchall() 

    csv_file = open(file_name, mode = 'w')
    counter = 0
    for row in all_rows:
        counter += 1
        row_list = []
        if (len(row) < 6):
            if row [0] == 'TTRAN':
                row [0] = 'TRAN'
            if row [0] == 'PPLAN':
                row [0] = 'PLAN'
        else:
            row[2] = row[2].replace("PPLAN", "PLAN").replace("TTRAN", "TRAN")
            row[2] = row[2].replace(code, code + ' ')
            row[1] = row[1].replace(',', '$').replace('\n', '')
            row[3] = row[3].replace(',', '$').replace('\n', '')
            row[4] = row[4].replace(',', '$').replace('\n', '')
            row[5] = row[5].replace(',', '$').replace('\n', '')
        for i in row:
            row_list.append(i)
        if counter < len(all_rows):
            csv_file.write(','.join(row_list)+'\n')
        else:
            csv_file.write(','.join(row_list))

if __name__ ==  '__main__':
    csv_from_table("dbo.courses", "data/courses.csv", '')
    csv_file = open('data/courses.csv')
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            table_name = row[0].replace("PLAN", "PPLAN").replace("TRAN", "TTRAN")
            csv_from_table(f"dbo.{table_name}", f"data/{row[0]}.csv", row[0])

        line_count += 1
    conn.close()

    print("done")

