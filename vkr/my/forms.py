from django import forms  
from my.models import *  

class AccountForm(forms.ModelForm):  
    class Meta:  
        model = Account  
        fields = "__all__"

class TestForm(forms.ModelForm):  
    class Meta:  
        model = Test  
        fields = "__all__"        