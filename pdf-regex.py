'''
Author: Viktor Vlasov
'''

import re
import csv
import os


pdf_folder = 'D:\Anaconda2\projects\pdf-src\\' #откуда берем PDF
txt_folder = 'D:\Anaconda2\projects\pdf2txt\\' #куда сохраняем ТХТ
pdf2txt_py_folder = 'D:\Anaconda2\Scripts\pdf2txt.py' #где хранится скрипт pdf2txt.py

for filename in os.listdir('./pdf-src/'):
    fn_no_spaces = filename.replace(" ", "")
    #Формируем строку скрипта
    py_script = 'python ' + pdf2txt_py_folder + ' -o ' + txt_folder + fn_no_spaces + '.txt ' + pdf_folder + filename
    
    print py_script + '\n'
    print 'Converting ' + filename + ' to TXT-file. Please wait...\n'
    os.system(py_script)

    #Читаем ТХТ-файл и парсим
    pdf_file = open(txt_folder + fn_no_spaces + '.txt')
    final = []
    for line in pdf_file:
        match = re.search('([\w.-]+)@([\w.-]+)', line)
        if match and not([match.group()] in final): #Удаляем дубликаты
            final.append([match.group()])
    print final
    
    #Запись Email-ов из ТХТ в CSV-файл
    with open('emails.csv', 'a') as fp:
        a = csv.writer(fp, delimiter=' ', lineterminator='\n')
        a.writerows(final)
       

''' 
    #EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
df_folder = 'D:\Anaconda2\projects\pdfs'
for filename in os.listdir('./pdfs/'):
    os.system('D:\Anaconda2\Scripts\pdf2txt.py -o ' + filename + '.txt ' + pdf_folderfilename + '.pdf')
    pdf_file = open('./pdfs/'+filename)
    final = []
    for line in pdf_file:
        
        print line
        match = re.search('([\w.-]+)@([\w.-]+)', line)
        if match:
            final.append([match.group()])
    print final
    '''