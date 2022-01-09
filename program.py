# Muhammet Furkan Portakal
# 18360859046

# CSV DOSYASI => data.csv olmak zorundadir.
# Id,Name,Gender,Phone,Lesson
# 1010,Ramiz Portakal,Male,553-841-47-89,Math
# 1020,Selma Sakarya,Female,505-782-22-44,Music
# 1030,John Doe,Male,512-224-55-75,Physics

import csv 

# read function
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

# write function
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

# search function
def search(gender):
    sayac = 0
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[2].lower() == gender.lower():
                print('Sonuca uygun olan id =>',row[0])
                sayac += 1

    if sayac == 0:
        print('\nAranan bulunamadi...')

# start function
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
        gender = input('Aranan kelimeyi giriniz: \t')
        search(gender)
    elif x == '4':
        exit()
    else:
        print('Hatali secim!')


while(1<2):
    start()
