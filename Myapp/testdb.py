from django.http import HttpResponse
from django.shortcuts import render
from Myapp.models import Students
from docx import Document
from Myapp.models import Biao4
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage
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
        rowcells = row.cells
        biao = Biao4(
            lyxh=rowcells[0].text,
            lyname=rowcells[1].text,
            lbxh=rowcells[2].text,
            lb=rowcells[3].text,
            dxxh=rowcells[4].text,
            duixiang=rowcells[5].text,
            xmxh=rowcells[6].text,
            csmc=rowcells[7].text,
            yjbz=rowcells[8].text,
            xzfw=rowcells[9].text,
            sm=rowcells[10].text,
        )
        biao.save()
    context = {}
    context['msg'] = '读取word文档成功'
    return render(request, 'test.html', context)


def split_page(object_list, request, per_page=8):
    paginator = Paginator(object_list, per_page)
    # 取出当前需要展示的页码, 默认为1
    page_num = request.GET.get('page', default='1')
    # 根据页码从分页器中取出对应页的数据
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger as e:
        # 不是整数返回第一页数据
        page = paginator.page('1')
        page_num = 1
    except EmptyPage as e:
        # 当参数页码大于或小于页码范围时,会触发该异常
        print('EmptyPage:{}'.format(e))
        if int(page_num) > paginator.num_pages:
            # 大于 获取最后一页数据返回
            page = paginator.page(paginator.num_pages)
        else:
            # 小于 获取第一页
            page = paginator.page(1)

    # 这部分是为了再有大量数据时，仍然保证所显示的页码数量不超过10，
    page_num = int(page_num)
    if page_num < 6:
        if paginator.num_pages <= 10:
            dis_range = range(1, paginator.num_pages + 1)
        else:
            dis_range = range(1, 11)
    elif (page_num >= 6) and (page_num <= paginator.num_pages - 5):
        dis_range = range(page_num - 5, page_num + 5)
    else:
        dis_range = range(paginator.num_pages - 9, paginator.num_pages + 1)

    data = {'page': page, 'paginator': paginator, 'dis_range': dis_range}
    return data


def lstbiao4(request):
    mlstbiao4 = Biao4.objects.all()

    data1 = split_page(mlstbiao4, request, 10)
    return render(request, 'biao4.html', data1)
