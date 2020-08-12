from django.shortcuts import render
from docx import Document

from Myapp.models import PsyuanDetail, Biao4, Pstz, Biao5, Biao72, Pingshenxxb


def importpsymd(self, request, obj, change):  #

    document = Document(obj.file)
    if obj.importtype == '0':  # (0, "评审通知"),
        biao = Pingshenxxb(
            pstzh = document.paragraphs[2].text,
        )
        biao.save()

    for t in document.tables:
        table = t
        if obj.importtype == '1':  # (1, "认证现场评审报告"),

            if len(t.columns) == 11:  # 评审报告  表4 建议批准的检验检测能力表
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


            elif len(t.columns) == 6:  # 建议批准的授权签字人
                for row in table.rows:
                    rowcells = row.cells
                    biao = Biao5(
                        xuhao=rowcells[0].text,
                        name=rowcells[1].text,
                        ziwuzicheng=rowcells[3].text,
                        sqqzly=rowcells[4].text,
                        beizu=rowcells[5].text,
                    )
                    biao.save()

            elif len(t.columns) == 16:  # 表7.2 现场评审能力确认方式及确认结果一览表
                for row in table.rows:
                    rowcells = row.cells
                    biao = Biao72(
                        xuhao=rowcells[0].text,
                        xmmc=rowcells[1].text,
                        yjbz=rowcells[2].text,
                        xmxh=rowcells[3].text,
                        csmc=rowcells[4].text,
                        # yjbztk = rowcells[0].text,
                        # xcsy = rowcells[0].text,
                        # nlyz = rowcells[0].text,
                        # clsh = rowcells[0].text,
                        # bdjg = rowcells[0].text,
                        # xcys = rowcells[0].text,
                        # xctw = rowcells[0].text,
                        # cyjlbg = rowcells[0].text,
                        # hcyq = rowcells[0].text,
                        # sfqr = rowcells[0].text,
                        # beizu = rowcells[0].text,
                    )
                    biao.save()
        if obj.importtype == '0':  # (0, "评审通知"),

            if len(t.columns) == 5:  # 评审通知
                for row in table.rows:
                    rowcells = row.cells
                    biao = Pstz(
                        psyzc=rowcells[0].text,
                        psname=rowcells[1].text,
                        ziwuzicheng=rowcells[2].text,
                        gzdw=rowcells[3].text,
                        lxfs=rowcells[4].text,
                    )
                    biao.save()
        if obj.importtype == '2':  # (2, "资质认定评审员名单"),
            if len(t.columns) == 5:  # 评审员名单
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
