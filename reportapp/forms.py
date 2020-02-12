from django import forms
from .models import profile,topic1,subtopic1
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'
    

class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')

class regform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profile_pic']

class userupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class upform(forms.ModelForm):
    class Meta:
        model = profile
        exclude = ('user','email','up')
        fields = '__all__'
        
class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32,widget=forms.PasswordInput)

class topicform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = topic1
        exclude = ['user']
        fields = '__all__'
    
class subtopicform(forms.ModelForm):
    # topic = forms.CharField(widget = forms.TextInput)
    subtopic = forms.CharField(widget = forms.Textarea)
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = subtopic1
        exclude = ['user']
        fields = '__all__'


class reportform(forms.Form):
    start_date=forms.DateField(widget=DateInput)
    end_date=forms.DateField(widget=DateInput)
    
class contactform(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)
    