import xlwt

workboook = xlwt.Workbook(encoding='utf-8')
worksheet = workboook.add_sheet('sheet1')

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d X %d = %d" %(j+1, i+1, (i+1)*(j+1)))
workboook.save('mul.xls')
