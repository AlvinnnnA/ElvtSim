import xlwt
import xlrd
import io
import pandas
import numpy

fileaddresstlog = "Log/LOG/log.py"
fileaddress = 'Log/xls/log.xls'


def read_log():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('log')
    log = open(fileaddresstlog, 'r')
    r = 1
    for logline in log:
        logline = logline.split(':')
        write_excel(r, logline, sheet1)
        r = r + 1
    f.save(fileaddress)


def write_excel(r, table, sheet1):
    print(r)
    # f = xlwt.Workbook()
    #   sheet1=f.add_sheet('log')
    if table == 0:
        row0 = ['key', 'value']
    else:
        row0 = table
    for i in range(0, len(row0)):
        sheet1.write(r, i, row0[i])


if __name__ == '__main__':
    read_log()
    print('end')
