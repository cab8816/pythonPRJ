from django import forms
from django.forms import ModelForm
from django.utils import timezone

from Myapp.models import Pingshenxxb, Xcpshcb71, Xcpshcb, Bfhxiang, Bpsdwxx, Biao72


class PsdwxxForm(forms.Form):
    jyjcjgmc = forms.CharField(label="检测机构名称", required="True", error_messages={"required": "该字段不能为空"})
    zcdz = forms.CharField(label="注册地址", error_messages={"required": "该字段不dd能为空"})
    jydz = forms.CharField(label="检验地址")
    yzbm = forms.CharField(label="邮编")
    chuanz = forms.CharField(label="传真")
    email = forms.CharField(label="email")


class PingshenxxbForm(ModelForm):
    class Meta:
        model = Pingshenxxb
        fields = ['id', 'pstzh', 'jcjgmc', 'psslh', 'sqsx', 'psdate', 'psadress', 'user', 'bpsdwxx', 'userinfo']

        labels = {

            'pstzh': '评审通知号1',
            'jcjgmc': '检测机构名称',
        }
        help_texts = {
            'pstzh': '这个是评审通知号',
        }
        error_messages = {
            'pstzh': {
                'max_length': "评审通知号",
            },
        }

        # widgets = {'id': forms.HiddenInput()}


class XcpshcbForm(ModelForm):
    class Meta:
        model = Xcpshcb
        fields = ['zhangbh', 'zhangmc', 'tkhao', 'psneirong']

        widgets = {
            "pssm": forms.widgets.Textarea(
                attrs={
                    "placeholder": "jjjjjjjjjjj",
                    'style': "height:100px;width:100%",
                }

            ),
            "psneirong": forms.widgets.Textarea(
                attrs={
                    "placeholder": "jjjjjjjjjjj",
                    'style': "height:100px;width:100%",
                },
            ),

            "psjg": forms.widgets.Select(
                choices=[(0, '符合'), (1, '不符合'), (2, '不适用')],

            ),

            "psyj": forms.widgets.Textarea(
                attrs={
                    "placeholder": "jjjjjjjjjjj",
                    'style': "height:100px;width:100%",
                },
            ),
        }
        labels = {
            'zhangbh': '序号',
            'psneirong': '评审内容',
        }


class BFHXForm(ModelForm):
    class Meta:
        model = Xcpshcb71
        fields = ['psxxb', 'pshcxx', 'psjd', 'psjg', 'psyj', 'pssm', 'jzfs', 'bsfyj', 'pszzyj']

        widgets = {
            "pssm": forms.widgets.Textarea(
                attrs={
                    "placeholder": "jjjjjjjjjjj",
                    'style': "height:100px;width:100%",
                }

            ),
            "psneirong": forms.widgets.Textarea(
                attrs={
                    "placeholder": "jjjjjjjjjjj",
                    'style': "height:100px;width:100%",
                },
            ),

            "psjg": forms.widgets.Select(
                choices=[(0, '符合'), (1, '不符合'), (2, '不适用')],

            ),

            "psyj": forms.widgets.Textarea(
                attrs={
                    "placeholder": "jjjjjjjjjjj",
                    'style': "height:100px;width:100%",
                },
            ),
        }
        labels = {
            'zhangbh': '序号',
            'psneirong': '评审内容',
        }


class Bfhxiangform(ModelForm):
    # 不符合项编辑表
    class Meta:
        model = Bfhxiang
        fields = ['psxxb', 'bfhxwc', 'bfhxwcdate', 'bpsbm', 'ptren', 'yiju', 'bfhms', 'jielun', 'tkhao', 'qrfs',
                  'psyname', 'bfsqueren', 'zzqueren']

        widgets = {
            "yiju": forms.widgets.Textarea(
                attrs={
                    " template_name": "django/forms/widgets/textarea.html",
                    'style': "height:75px;width:100%;margin:1px;",
                    "placeholder": "依据",
                    'class': 'form-control',
                },
            ),
            #
            "bfhms": forms.widgets.Textarea(
                attrs={
                    "placeholder": "不符合项事实描述",
                    'style': "height:75px;width:100%;margin:1px",
                    'class': 'form-control',
                },
            ),

            "jielun": forms.widgets.Select(
                choices=[(0, '符11合'), (1, '不符合'), (2, '不适用')],
            ),

            "bfhxwcdate": forms.widgets.SelectDateWidget(
                attrs={
                    "input_type": 'text',
                    "template_name": 'django/forms/widgets/SelectDateWidget.html',
                },

            ),
        }

class Bpsdwxxform(ModelForm):
    # 被评审单位信息编辑表
    class Meta:
        model = Bpsdwxx
        fields = ['jyjcjgmc', 'zcdz', 'jydz', 'yzbm', 'chuanz', 'email', 'fzr', 'fzrzw', 'fzrgddh', 'fzryddh',
                  'llr', 'llrzw', 'llrgddh', 'llryddh', 'sfrdw', 'sfrdwdz']

class Biao72form(ModelForm):
    # 被评审单位信息编辑表
    class Meta:
        model = Biao72
        fields = ['psxxb', 'xuhao', 'xmmc', 'yjbz', 'xmxh', 'csmc', 'yjbztk', 'xcsy', 'nlyz', 'clsh',
                  'bdjg', 'xcys', 'xctw', 'cyjlbg', 'hcyq', 'sfqr', 'beizu']

        # widgets = {
        #     "nlyz": forms.widgets.Select(
        #
        #         attrs={
        #             'class': 'form-control btn-label glyphicon glyphicon-ok',
        #             "template_name": 'django/forms/widgets/select.html',
        #             'option_template_name': 'django/forms/widgets/select_option.html',
        #
        #         },
        #
        #
        #     ),
        #
        #
        #
        #
        # },
        # labels = {
        #      'nlyz': '序号',
        #          },