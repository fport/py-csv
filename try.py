import csv 
    

def read():
    with open('data.csv', mode ='r') as file: 
          
        csvFile = csv.reader(file) 
        
        line_count = 0
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

    filename = "data.csv"

    with open(filename, 'a+') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)

def search(gender):
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[2] == gender:
                print(row)

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
        gender = input('lutfen male/female seciniz: \t')
        search(gender)
    elif x == '4':
        exit()
    else:
        print('Hatali secim!')


while(1<2):
    start()
