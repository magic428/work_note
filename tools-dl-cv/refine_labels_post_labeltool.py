import os
import glob

'''
    复制静态的护帮板标注信息，主要更改 .txt 标注文件中的信息。
'''

#提取检测文本中的Face_sprag数据
f=open('E:\dl-datasets\\1\yjl_sw_081128.txt',"r")
line = f.readline()
str1 = ''
for i in f:
    if int(i.strip().split(',')[4]) == 1:
        str1 += i
#判断并重新写入文本
for filename in glob.glob(r'E:\dl-datasets\\1\*.txt'):
    f=open(filename,"r")
    line = f.readline()
    count2 = int(line.split(',')[0])                 #每个文本中数据个数
    count3=0                                         #计数，检测每个文本中存在Face_sprag数据个数
    str2 = ''                                        #保存文本中除去Face_sprag数据的其他数据
    str3 = ''                                        #保存文本中第一条数据
    for i in f:
        if int(i.strip().split(',')[4]) == 1:
            count3 = count3 + 1
        if int(i.strip().split(',')[4]) != 1:       
            str2 += i     
    if   count3 < 1:                                  
        count2=count2 + 1 
        str3 = str(count2)+','+str(line.split(',')[1])
        str3=str3+str2+str1
        print(str3)
        with open(filename,'w') as f:    
            f.write(str3)


'''
for filename in glob.glob(r'E:\dl-datasets\\1\*.txt'):
    f=open(filename,"r")
    line = f.readline()
    count2 = int(line.split(',')[0])                 #每个文本中数据个数
    str2 = ''                                        #保存文本中除去Face_sprag数据的其他数据
    str3 = ''                                        #保存文本中第一条数据
    for i in f:
        if int(i.strip().split(',')[4]) == 3:
            count2=count2 -  1
        else:
            str2 += i        

    str3 = str(count2)+','+str(line.split(',')[1])
    str3=str3+str2
    print(str3)
    with open(filename,'w') as f:    
        f.write(str3)
'''
'''
#提取检测文本中的Face_sprag数据
f=open('E:\dl-datasets\\1\yjl_sw_080679.txt',"r")
line = f.readline()
count1 = int(line.split(',')[0])                     #计数文本中Face_sprag数据的条数
str1 = ''
for i in f:
    if int(i.strip().split(',')[4]) != 3:
        count1=count1-1
    
    if int(i.strip().split(',')[4]) == 3:
        str1 += i
#判断并重新写入文本
for filename in glob.glob(r'E:\dl-datasets\\1\*.txt'):
    f=open(filename,"r")
    line = f.readline()
    count2 = int(line.split(',')[0])                 #每个文本中数据个数
    count3=0                                         #计数，检测每个文本中存在Face_sprag数据个数
    str2 = ''                                        #保存文本中除去Face_sprag数据的其他数据
    str3 = ''                                        #保存文本中第一条数据
    for i in f:
        if int(i.strip().split(',')[4]) == 3:
            count3 = count3 + 1
        if int(i.strip().split(',')[4]) != 3:        #去除文本中原有的Face_sprag数据
            str2 += i        
    if count3 < 4:                                   #去除文本中小于4条的Face_sprag数据
        count2=count2 + count1 - count3
        str3 = str(count2)+','+str(line.split(',')[1])
        str3=str3+str2+str1
        print(str3)
        with open(filename,'w') as f:    
            f.write(str3)
'''