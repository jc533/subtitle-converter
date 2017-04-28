import easygui,os

input_path = easygui.tk_FileDialog.askopenfilename(title='選擇文字檔案') #path of the file


f = open(input_path,'r',encoding="ASCII")
text = f.readlines()

page = []

for row in text:
    for char in row:
        if ord(char) >= 48 and ord(char)<= 57: #remove all digits
            break
        else:
            page.append(row)
            break
f.close()

text = "".join(page)

text = text.replace('\n',' ') # replace \n with space
text = text.replace('  ',' ') # remove double spaces  


file_name = os.path.basename(input_path)# get the old file name
result_file = open(file_name,'w')# creat a new file if the file doesn't exist and open the file
result_file.write(text)# write the new file 
result_file.close()# close the file
