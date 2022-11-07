from django import forms
from .models import Formone,Education,UploadingDocument
from django_countries.fields import CountryField




CHOICES = [('Male','M'),('Female','F')]


class FormoneForm(forms.ModelForm):
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    country= CountryField(blank_label='Country',).formfield()
    def __init__(self, *args, **kwargs):
        #remove any labels here if desired
        super(FormoneForm, self).__init__(*args, **kwargs)
        # remove the label of a non-linked/calculated field (txt01 added at top of form)
        self.fields['country'].label = ''

    class Meta:
        model=Formone
        fields="__all__"
        labels={'lastname':" ",'father_name':"Father's name",'fathernamelast':" ",'mother_name':"Mother's name",'mothernamelast':" ",'city':"",
        'country':"",'telephone_home':"Telephone - Home",'telephone_mobile':"Telephone - Mobile"}
        widgets={'name':forms.TextInput(attrs={'placeholder':"First"}),
        'lastname':forms.TextInput(attrs={'placeholder':"Last"}),
        'date_of_birth':forms.DateInput(attrs={'type':'date','placeholder':"DD/MM/YYYY"}),
        'father_name':forms.TextInput(attrs={'placeholder':"First"}),
        'fathernamelast':forms.TextInput(attrs={'placeholder':"Last"}),
        'mother_name':forms.TextInput(attrs={'placeholder':"First"}),
        'mothernamelast':forms.TextInput(attrs={'placeholder':"Last"}),
        'home_Address':forms.TextInput(attrs={'placeholder':"Street Address"}),
        'city':forms.TextInput(attrs={'placeholder':"City"}),
        'telephone_home':forms.TextInput(attrs={'placeholder':"### ### ####"}),
        'telephone_mobile':forms.TextInput(attrs={'placeholder':"### ### ####"}),}


BOARD_CHOICE=[('CBSC','CBSC'),('ICSC','ICSC'),('State board','State board')]
class EducationForm(forms.ModelForm):
    HSC_Board=forms.CharField(label='HSC Board', widget=forms.Select(choices=BOARD_CHOICE))
    SSC_board=forms.CharField(label='SSC Board', widget=forms.Select(choices=BOARD_CHOICE))
    class Meta:
        model=Education
        fields="__all__"


class UploadingDocumentForm(forms.ModelForm):
    class Meta:
        model=UploadingDocument
        fields="__all__"