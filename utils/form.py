
from  django import forms

from app02.models import *

class BookForm_(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        labels={'title':'书名','price':'价格',}
        widgets={
            'password':forms.widgets.PasswordInput(attrs={"class":'c1'}),
            'publishDate':forms.widgets.DateInput(attrs={'type':'date'}),
        }

class BookForm(forms.Form):
    class Meta:
        model=Book
    title=forms.CharField(max_length=16,label='书名',initial='山海经',
                          widget=forms.widgets.TextInput(attrs={"class":'form-control'},),)

    # sex=forms.ChoiceField(choices=(('1','男'),('2','女'),),required=False,
    #                       label='性别',
    #                       widget=forms.widgets.Select(attrs={'class':'form-control'})
    #                       )
    publish=forms.ModelChoiceField(label='出版社',required=False,
                                   queryset=Publish.objects.all().only('name'),
                                   widget=forms.widgets.Select(attrs={"class":'form-control'}))

    publishDate=forms.DateField(label='出版时间',required=False,
                                 widget=forms.widgets.DateInput(attrs={'class':'for-control','type':'date'},),
                                 )
    publish_id=forms.IntegerField(label='出版社ID',required=False,
                                 widget=forms.widgets.TextInput(attrs={'class':'for-control'},),
                                 )
    price=forms.DecimalField(decimal_places=2,max_digits=6,label='价格',
                             widget=forms.widgets.TextInput(attrs={'class': 'for-control'}, ),
                             )
    authors=forms.ModelMultipleChoiceField(
        queryset=Author.objects.all().only('name',),required=False,
        widget=forms.widgets.SelectMultiple(attrs={"class":'form-control'})
    )
    def __init__(self,*args,**kwargs):
        super(BookForm,self).__init__(*args,**kwargs)
        # self.fields['publish_id'].choices=((1,'上海'),(2,'北京'),(3,'武汉'))
        self.fields['publish_id'].chioces=Publish.objects.all().values_list('nid','name')