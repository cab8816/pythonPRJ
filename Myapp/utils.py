from django.shortcuts import render
from docx import Document

from Myapp.models import PsyuanDetail


def importpsymd(self, request, obj, change):  # 读入评审员名单

    document = Document(obj.file)
    for t in document.tables:
        table = t
        for row in table.rows:
            rowcells = row.cells
            biao = PsyuanDetail(
                name=rowcells[1].text,
                gender=rowcells[2].text,
                danwei=rowcells[3].text,
                psybh=rowcells[4].text,
            )
            biao.save()
    context = {'msg': '读取word文档成功'}
    return render(request, 'test.html', context)
