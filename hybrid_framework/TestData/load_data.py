from hybrid_framework.Utilities.xlultilites import *
def fetch_data_from_xl(xl_path, sheet):
    row=GetRow(xl_path, sheet)
    col=GetCol(xl_path, sheet)
    print(row, col)

    xl_data = []
    for r in range(2,row+1):
        row_data=[]
        for c in range(1, col+1):
            row_data.append(ReadCell(xl_path, sheet, r, c))
        xl_data.append(tuple(row_data))
    # print(xl_data)
    return xl_data
