from django import forms


class PsdwxxForm(forms.Form):
    jyjcjgmc = forms.CharField(label="检验检测机构名称",required="True",error_messages={"required":"该字段不能为空"})
    zcdz = forms.CharField(label="注册地址",error_messages={"required":"该字段不dd能为空"})