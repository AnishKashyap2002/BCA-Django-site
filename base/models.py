from django.db import models
from django.contrib.auth.models import AbstractUser
class_list = (
    ('1st Sem', '1st Sem'),
    ('2nd Sem', '2nd Sem'),
    ('3rd Sem', '3rd Sem'),
    ('4th Sem', '4th Sem'),
    ('5th Sem', '5th Sem'),
    ('6th Sem', '6th Sem'),
)

class User(AbstractUser):
    name = models.CharField(max_length=50, null = False)
    email = models.CharField( max_length=50 ,null = True)
    avatar = models.ImageField( upload_to='Avaters',  default = 'default-profile-pic.png')
    bio = models.TextField(null = True)
    bca_class = models.CharField( max_length=50 ,choices=class_list ,default= ('1st Sem', '1st Sem'), null = True)
    is_teacher = models.BooleanField(default = False)
    followers = models.ManyToManyField('User', related_name='follower')
    followings = models.ManyToManyField('User',related_name= 'following')
    def __str__(self):
        return self.username
    
    def follower_count(self):
        return self.followers.count()
    
    def following_count(self):
        return self.followings.count()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    caption = models.CharField(max_length=200 , null = True)
    image = models.ImageField(upload_to='Post_Images')
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_by')
    
    def __str__(self):
        return self.user.username
    
    def num_of_likes(self):
        return self.likes.count()
    
 
class Comment_Post(models.Model):
   post = models.ForeignKey(Post,  on_delete=models.CASCADE, related_name='comments')
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   body = models.TextField()
   date = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.post.caption
   
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    date = models.DateTimeField( auto_now_add=True)
    image = models.ImageField(upload_to='Questions' , null = True, blank = True)
    
    def __str__(self):
        return self.body
    
class Answer(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question ,on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    image = models.ImageField(upload_to='answers', null = True, blank = True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.question.body
    

class Note(models.Model):
    
    user = models.ForeignKey( User ,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    topic = models.CharField(max_length=250 , null=True, blank=True)
    description = models.TextField(null = True , blank= True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Notes_Images', null =True , blank = True)
    files =  models.FileField( upload_to='Notes_Files' ,max_length=100 , null = True, blank = True)
    bca_class = models.CharField(max_length=50 ,choices=class_list, default='1st Sem')
    
    def __str__(self):
        return self.title
    
    
    
class Topic (models.Model):
    body = models.TextField(null=True, max_length=250)
    
    
    def __str__(self):
        return self.body
    

    
    
class Room(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='host',null=True, blank=True)
    title = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.host.username
    
class Message(models.Model):
    body = models.TextField(null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='Room- Messages', null = True,blank = True)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username
    

EDUCATION = (
    ("10th", '10th'),
    ('12th', '12th'),
    ('Graduation', 'Graduation'),
)
STATE = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField( max_length=255)
    lastname = models.CharField( max_length=255)
    date = models.DateField( auto_now_add=True)
    fathername = models.CharField( max_length=255)
    sex = models.CharField( max_length=50,default= 'Male')
    education = models.CharField(choices=EDUCATION,max_length=100, default='10th')
    tenth_percentage = models.FloatField(null = True ,blank=True)
    twelth_percentage = models.FloatField(null = True ,blank=True)
    state = models.CharField(choices = STATE, max_length=50, default='Delhi')
    phone = models.IntegerField(null = True ,blank=True)
    email = models.EmailField( max_length=254,null = True ,blank=True)
    languages = models.CharField(max_length=250, null=True)
    programming_languages = models.CharField(max_length=250, null=True)
    hobbies = models.TextField(null = True)
    about = models.TextField(null = True)
    image = models.ImageField( upload_to='resume_images',default = 'default-profile-pic')
    
    def __str__(self):
        return self.firstname
    
class Choice(models.Model):
    body = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.body
    
    
class Poll(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls')
    voters = models.ManyToManyField(User)
    choices = models.ManyToManyField(Choice)
    title = models.TextField(null = True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    


    
   
   
    
    
    