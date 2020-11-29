from django import forms
from django.forms import ModelForm, Textarea, CheckboxInput
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from Myapp.models import Pingshenxxb, Xcpshcb71, Xcpshcb, Bfhxiang, Bpsdwxx, Biao72

#
# {{ field.label }}	字段对应的label信息
# {{ field.label_tag }}	自动生成字段的label标签，注意与{{ field.label }}的区别。
# {{ field.id_for_label }}	自定义字段标签的id
# {{ field.value }}	当前字段的值，比如一个Email字段的值someone@example.com
# {{ field.html_name }}	指定字段生成的input标签中name属性的值
# {{ field.help_text }}	字段的帮助信息
# {{ field.errors }}	包含错误信息的元素
# {{ field.is_hidden }}	用于判断当前字段是否为隐藏的字段，如果是，返回True
# {{ field.field }}	返回字段的参数列表。例如{{ char_field.field.max_length }}



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
    # def __init__(self, *args, **kwargs):
    #     super(Biao72form, self).__init__(*args, **kwargs)
    #     super().__init__()
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['psxxb'].widget.attrs['readonly'] = True

    class Meta:
        model = Biao72
        # exclude = ['xmmc','xmxh']
        fields = "__all__"
        # fields = ['psxxb', 'xuhao', 'xmmc', 'yjbz', 'xmxh', 'csmc', 'yjbztk', 'xcsy', 'nlyz', 'clsh',
        #           'bdjg', 'xcys', 'xctw', 'cyjlbg', 'hcyq', 'sfqr', 'beizu']

        widgets = {
            "xmmc": Textarea(
                attrs={'cols':30,'rows':12}
            ),



            "xcsy": CheckboxInput(
                attrs={
                    "checked": "False",
                },

            ),
        }

        error_messages = {

            'csmc': {'required': _("This writer's name is too long."), }  # 每个字段的错误都可以写
        },

        # def __init__(self, *args, **kwargs):  # 批量操作
        #     super().__init__(*args, **kwargs)
        #     for field in self.fields:
        #         field.error_messages = {'required':'不能为空'} #批量添加错误信息,这是都一样的错误，不一样的还是要单独写。
        #         # self.fields[field].widget.attrs.update({'class': 'form-control'})