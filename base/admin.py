from django.contrib import admin
from .models import User,Post,Comment_Post,Question,Answer,Note,Message,Room,Topic,Choice, Poll, Resume


admin.site.register(Post)
admin.site.register(Comment_Post)

@admin.register(User)
class Admin(admin.ModelAdmin):
    list_display = ['username' , 'is_teacher']
    
@admin.register(Question)
class Admin(admin.ModelAdmin):
    list_display = ['user' , 'body']
    
@admin.register(Answer)
class Admin(admin.ModelAdmin):
    list_display = ['user']
    
    
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['user' , 'title']
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['host']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Resume)
class Admin(admin.ModelAdmin):
    pass


    

    

    

    

    



    

    
    
