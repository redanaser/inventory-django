from typing import Any
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ["ti","co"]
    
    def clean(self):
        data=self.cleaned_data
        title=data.get('ti')
        qs=Article.objects.filter(ti__icontains=title)
        if qs.exists() :
            self.add_error('ti',f'{title} is already used')

        return data



