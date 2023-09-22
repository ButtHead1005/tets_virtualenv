import csv

with open('orders.csv','r') as csvinput:
    with open('orders_two.csv', 'w') as csvoutput:
        f_writer = csv.writer(csvoutput, lineterminator='\n')
        f_reader = csv.reader(csvinput)
        all_data = []
        f_header = next(f_reader)
        f_header.append('is_checked')
        all_data.append(f_header)
        
        for row in f_reader:
            row.append('checked')
            all_data.append(row)
        
        f_writer.writerows(all_data)