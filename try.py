import csv 
    

def read():
    # opening the CSV file 
    with open('data.csv', mode ='r') as file: 
          
      # reading the CSV file 
        csvFile = csv.reader(file) 
        
        line_count = 0
      # displaying the contents of the CSV file 
        for lines in csvFile: 
            if line_count == 0:
                line_count += 1
                print('\n') 
                continue
            else:
                print(lines) 
                line_count += 1

def write():
    print('CSV dosyasina eklemek icin sirayla gelicek bilgileri doldurmalisiniz!')
    new_Id = input('\n Id giriniz')
    new_Name = input('\n Adini giriniz')
    new_Gender = input('\n Cinsiyeti giriniz')
    new_Phone = input('\n Telefon no giriniz')
    new_Lesson = input('\n Dersi giriniz')

    fields = [new_Id, new_Name, new_Gender, new_Phone, new_Lesson]

    # name of csv file
    filename = "data.csv"

    # writing to csv file
    with open(filename, 'a+') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # # writing the data rows
        # csvwriter.writerows(rows)


def search():
    print('ara ulan')

def start():
    print("""
     __________________________________________________
    |                                                  |  
    |    Lutfen Yapmak istediginiz islemi giriniz:     |
    |        1- CSV dosyayini oku                      |
    |        2- CSV dosyasina ekle                     |
    |        3- CSV dosyasinda arama yap               | 
    |        4- Cikis yapmak icin giriniz.             |
    |__________________________________________________|        
            """)
    x = input('=> Yapmak istediginiz islemi giriniz:\n')

    if x == '1':
        read()
    elif x == '2':
        write()
    elif x == '3':
        search()
    elif x == '4':
        exit()
    else:
        print('yanlis secim haci')


while(1<2):
    start()
