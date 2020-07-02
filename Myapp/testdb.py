from django.http import HttpResponse

from Myapp.models import Students
from docx import Document
from Myapp.models import Biao4
from docx.shared import Inches


def testdbadd(request):
    student = Students(name='谢振乾')
    student.save()
    return HttpResponse("<p> 数据添加成功！</p>")


def testdblst(request):
    response1 = ""
    list = Students.objects.all()
    for var in list:
        response1 += var.name + " "
    return HttpResponse("<p>" + response1 + "</p>")


def testdbupd(request):
    stu = Students.objects.get(id=2)
    stu.name = '谢岸马'
    stu.save()
    stu.objects.filter(id=3).update(name='谢多多')
    return HttpResponse("<p>成功修改</p>")


def testdoc(request):
    document = Document()
    document.add_heading('Document Title', 0)
    p = document.add_paragraph('A plain pragraph having some')
    p.add_run('bold').bold = True
    p.add_run('and some')
    p.add_run('italic.').italic = True
    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='Intense Quote')
    document.add_paragraph(
        'first item in unordered list', style='List Bullet'
    )
    document.add_paragraph(
        'first item in ordered list', style='List Number'
    )
    # document.add_picture('monty-truth.png', width=Inches(1.25))
    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam')
    )

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc
    document.add_page_break()
    document.save('testdoc/demo.docx')
    return HttpResponse("<p>doc文件生成成功</p>")


def readword(request):
    document = Document('testdoc/psbg.docx')
    table = document.tables[0]
    for row in table.rows:
        rowcells=row.cells
        biao = Biao4(
            # lyxh=rowcells[0],
            lyname=rowcells[1],
            # lbxh=rowcells[2],
            lb=rowcells[3],
            # dxxh=rowcells[4],
            duixiang=rowcells[5],
            # xmxh=rowcells[6],
            csmc=rowcells[7],
            yjbz=rowcells[8],
            xzfw=rowcells[9],
            sm=rowcells[10],
        )
    biao.save()
    return HttpResponse("<p>doc读取ddddd成功</p>")

