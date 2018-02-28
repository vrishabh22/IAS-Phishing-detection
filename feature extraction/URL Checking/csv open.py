import csv
def main():
        #process_URL_list('URL.txt','1.csv')
        with open('url_features1.csv', 'rb') as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                print(row[0])

main()
