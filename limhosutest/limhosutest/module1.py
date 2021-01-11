import xlsxwriter
# 엑셀파일과 워크시트를 만든다.
workbook = xlsxwriter.Workbook('d:\파이썬\Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# 워크시트에 쓸 튜블데이터
expenses = (['Rent', 1000],
            ['Gas', 100],
            ['Food', 300],
            ['Gym', 50],)

# 첫번째 열과 행을 초기화
row = 0
col = 0

# 반복문을 돌며 튜플에 있는 값을 워크시트에 값을 쓴다.
for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

# 마지막 행에 합계와 값을 넣은다.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()
