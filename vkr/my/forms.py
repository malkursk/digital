from django import forms  
from my.models import *  

class AccountForm(forms.ModelForm):  
    class Meta:  
        model = Account  
        fields = ['fio','org','region']

class TestForm(forms.ModelForm):  
    class Meta:  
        model = Test  
        fields = ['info','enable']
        # fields = "__all__"        