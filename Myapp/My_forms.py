from django import forms
from django.forms import ModelForm

from Myapp.models import Pingshenxxb, Xcpshcb71, Xcpshcb


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
        fields = ['pstzh', 'jcjgmc', 'psslh', 'sqsx', 'psdate', 'psadress', 'user', 'bpsdwxx']

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


class XcpshcbForm(ModelForm):
    class Meta:
        model = Xcpshcb
        fields = ['id','zhangbh', 'zhangmc', 'tkhao', 'psneirong','psjg','psyj','pssm']

        widgets = {
            "pssm":forms.widgets.Textarea(
                attrs={
                    "placeholder":"jjjjjjjjjjj",
                    'style':"height:100px;width:100%",
                }


            ),
            "psneirong": forms.widgets.Textarea(
                attrs={
                    "placeholder": "jjjjjjjjjjj",
                    'style': "height:100px;width:100%",
                },
            ),

            "psjg": forms.widgets.Select(
                choices=[(0,'符合'),(1,'不符合'),(2,'不适用')],


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

