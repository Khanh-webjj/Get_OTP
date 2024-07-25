import openpyxl
print('Excel Handler');

def ReadExcel(path):
    print('Reading Excel From Path '+path)
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    row0 = list(sheet.rows)
    n = len(row0)
    details = []
    for row in list(sheet.rows)[1:]:
        j = 0
        map={}
        for cell in row:
            if j >= n:
                break;
            elif row0[j].value != None and cell.value!=None:
                map[row0[j].value] = cell.value
            j+=1;
        if map:
            details.append(map)
    return details

def Write_excel(path, contents):
    columns = list(contents[0].key())
    wb = openpyxl.Workbook()
    sheet = wb.active

    for i in range(1, len(columns)+1):
        sheet.cell(row=1, column=i).value = columns[i-1]
    i=2;
    for entry in contents:
        for j in range(1, len(columns)+1):
            sheet.cell(row=i, column=j).value = entry[columns[j-1]]
        i += 1;
    wb.save(path)

# read from excel
