from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User,Post,Question,Answer,Note,Room, Resume

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("name","email", "avatar", "bio", "bca_class", 'username' , 'password1', 'password2')

class TeacherUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("name","email", "avatar", "bio", 'username' , 'password1', 'password2')

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ('image' , 'caption')
        
class QuestionForm(ModelForm):
    
    class Meta:
        model = Question
        fields = ("body","image")
        
class AnswerForm(ModelForm):
    
    class Meta:
        model = Answer
        fields = ("body" ,"image")
        
class NoteForm(ModelForm):
    
    class Meta:
        model = Note
        fields = ('title' ,'topic','description','bca_class','image','files')
        
class RoomForm(ModelForm):
    
    class Meta:
        model = Room
        fields = ("title",'topic')


SEX = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others', 'Others'),
)

PROG_LANG = (
    ('Python', 'Python'),
    ('C++', 'C++'),
    ('C', 'C'), 
    ('Java', 'Java'),
    ('Javascript', 'Javascript'),
    ('Kotlin', 'Kotlin'),
)


class ResumeForm(ModelForm):
    sex = forms.ChoiceField(choices =SEX, widget=forms.RadioSelect)
    
    programming_languages = forms.MultipleChoiceField(choices=PROG_LANG, widget=forms.CheckboxSelectMultiple)
    
    class Meta:
         model = Resume
         fields = '__all__'
         exclude = ('user', )
   




