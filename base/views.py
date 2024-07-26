from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import FormView
from .forms import UserForm, PostForm,TeacherUserForm,QuestionForm,AnswerForm,NoteForm,RoomForm,ResumeForm
from .models import Post,User, Comment_Post,Question,Answer,Note,Room, Topic,Message, Resume,Poll,Choice

from django.http import HttpResponse
from django.http import JsonResponse


from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def register_teacher(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']
        # avatar = request.FILES.get('avatar')
        # name = request.POST['name']
        # email = request.POST['email']
        # bio = request.POST['bio']
        
        # if password1 != password2:
        #     messages.info(request, 'Password Do Not Match')
        # elif User.objects.filter(username = username).first():
        #     messages.info(request, 'Username Already Taken')
        # else:
        #     user = User()
        #     user.username = username
        #     user.password = password1
        #     user.name = name
        #     user.avatar = avatar
        #     user.bio  = bio 
        #     user.email = email
        #     user.save()
        #     login(request, user)
        #     return redirect('home')
        form = TeacherUserForm(request.POST, request.FILES)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        avatar = request.FILES.get('avatar')
        
        if password1 != password2:
            messages.info(request, 'Password Do Not Match')
            
        elif User.objects.filter(username = username).first():
            messages.info(request, 'Username Already Taken')
            
            
        elif form.is_valid():
            user = form.save(commit= False)
            user.is_teacher = True
            user.avatar = request.FILES.get('avatar')
            user.save()
            login(request, user)
            return redirect('home')
        
        
    form = TeacherUserForm()
    context = {
        'form' : form
    }
    return render(request, 'register.html' ,context )


def register_student(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        
        if password1 != password2:
            messages.info(request, 'Password Do Not Match')
            
        elif User.objects.filter(username = username).first():
            messages.info(request, 'Username Already Taken')
            
            
        elif form.is_valid():
            user = form.save(commit=False)
            user.avatar = request.FILES.get('avatar')
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Data')
    form = UserForm()
    context = {
        'form' : form
    }
    return render(request, 'register.html' ,context )

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password Incorrect')
            
    return render(request, 'login.html')
        
@login_required(login_url='login')   
def logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    posts = Post.objects.all().order_by('-date')
   
    context = {
        'posts' : posts
    }
    
    return render(request, 'home.html', context)

@login_required(login_url='login')
def add_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
        
        
    form = PostForm()
    context = {
        'form' : form
    }
    
    return render(request, 'add-post.html', context)

@login_required(login_url='login')
def like_post(request):
    id = request.GET.get('id')
    post = Post.objects.filter(id=id).first()
    if post.likes.filter(id = request.user.id).first():
        post.likes.remove(request.user)
        data = {
            'likes' : post.likes.count(),
            'liked' : True,
        }
        
        return JsonResponse(data)
    else:
        post.likes.add(request.user)
        data = {
            'likes' : post.likes.count(),
            'liked' : False,
        }
        return JsonResponse(data ,safe=False)
    # return redirect(f'/#{id}')
    

@login_required(login_url='login')
def post_comments(request,id):
    post = Post.objects.get(id= id)
    comments = Comment_Post.objects.filter(post__id=id).order_by('-date')
    context = {
        'post' : post,
        'comments' : comments,
    }
    return render(request, 'post-comments.html', context)

@login_required(login_url='login')
def add_post_comment(request ,id):
    post = Post.objects.get(id = id)
    if request.method == 'POST':
        body = request.POST['body']
        comment = Comment_Post()
        comment.user = request.user
        comment.post = post
        comment.body = body
        comment.save()
        return redirect(f'/post-comments/{id}')
    context = {
        'post' : post
    }
    return render(request, 'add-post-comment.html', context)

@login_required(login_url='login')
def delete_comment(request, id):
    comment = get_object_or_404(Comment_Post, id = id)
    comment.delete()
    return redirect(f'/post-comments/{comment.post.id}')

@login_required()
def delete_post(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('home')

@login_required(login_url='login')
def show_profile(request,id):
    user = get_object_or_404(User, id= id)
    notes = Note.objects.filter(user=user).count()
    questions = Question.objects.filter(user=user).count()
    polls = Poll.objects.filter(host=user).count()
    rooms = Room.objects.filter(host=user).count()
    
    followed = False
    if user != request.user and request.user in user.followers.all():
        followed = True
     
    context = {
         'user' : user,
         'notes' : notes,
         'questions' : questions,
         'polls' : polls,
         'rooms' : rooms,
         'followed' : followed,
    }
    return render(request,'show-profile.html', context)
     
@login_required(login_url=  '/login')    
def edit_profile(request):
    band = get_object_or_404(User,id = request.user.id)
    
    teacher = request.user.is_teacher
    
    if request.method == 'POST': 
        if teacher:
            form = TeacherUserForm(request.POST, request.FILES ,instance =band)
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            username = request.POST['username']
            avatar = request.FILES.get('avatar')
        
            if password1 != password2:
                messages.info(request, 'Password Do Not Match')
            
            elif User.objects.filter(username = username).first() and username != request.user.username:
                messages.info(request, 'Username Already Taken')
            
            elif form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = UserForm(request.POST, request.FILES, instance = band)
        
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            username = request.POST['username']
        
            if password1 != password2:
                messages.info(request, 'Password Do Not Match')
            
            elif User.objects.filter(username = username).first() and username != request.user.username:
                messages.info(request, 'Username Already Taken')
            
            
            elif form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Invalid Data')
        
                
    form = UserForm(instance = band)
    if teacher : 
        form = TeacherUserForm(instance = band)
        
    context = {
        'form' : form
    }
        
    return render(request, 'edit-profile.html', context)


@login_required(login_url='login')
def ask_question(request):
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        
        if form.is_valid():
            question = form.save(commit = False)
            img = request.FILES.get('image')
            if img:
                question.image = img
            question.user = request.user
            question.save()
            return redirect('questions')
        else:
            messages.info(request, 'Question form is Not Valid!!!')
    
    form = QuestionForm()
    context = {
        "form" : form
    }
    return render(request, 'ask-question.html',context )

@login_required(login_url='login')
def questions(request):
    questions = Question.objects.all().order_by('-date')
    
    context = {
        'questions' : questions
    }
    
    return render(request, 'questions.html' , context)

@login_required(login_url='login')
def answers(request, id):
    question = get_object_or_404(Question, id = id)
     
    
    answers = Answer.objects.filter(question= question).order_by('-date')
    context = {
        'answers' : answers,
        'question' : question,
    }
    return render(request, 'answers.html', context)

@login_required(login_url='login')
def answer(request, id):
    question = get_object_or_404(Question, id = id)
    
    
    if request.method == 'POST':
        form = AnswerForm(request.POST,request.FILES)
        if form.is_valid():
            answer = form.save(commit = False)
            img = request.FILES.get('image')
            if img:
                answer.image = img
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect(f'/answers/{id}')
        else:
            messages.info(request, 'Answer form is Not Valid!!!') 
        
        
    form = AnswerForm()
    context = {
        'question' : question,
        'form' : form,
        'id' : id,
    }
    return render(request, 'answer.html', context)


@login_required(login_url='login')
def notes(request):
    notes = Note.objects.all().order_by('-date')
    
    context = {
        'notes' : notes
    }
    return render(request, 'notes.html', context)

@login_required(login_url='login')
def add_note(request):
    
    if request.method == 'POST':
        
        form = NoteForm(request.POST , request.FILES)
        
        if form.is_valid():
            note = form.save(commit = False)
            note.user = request.user
            img = request.FILES.get('image')
            files = request.FILES.get('files')
            
            if img:
                note.image = img
            if files:
                note.files = files
            form.save()
            return redirect('notes')
    
    form = NoteForm()
    
    context = {
        'form' : form,
    }
    
    return render(request, 'add-note.html', context)

@login_required(login_url='login')
def follow(request, id):
    person  = User.objects.get(id = id)
    all_followers = person.followers.all()
    user = User.objects.get(id = request.user.id)
    
    check = False
    if user in all_followers:
        check = True
        
    if check:
        person.followers.remove(user)
        user.followings.remove(person)
    else:
        person.followers.add(user)
        user.followings.add(person)
    person.save()
    user.save()
        
    return redirect(f'/show-profile/{id}')

@login_required(login_url='login')
def followers(request, id):
    followers = User.objects.get(id = id).followers.all()
    context = {
        'users' : followers,
    }
    return render(request, 'followers.html',context)


@login_required(login_url='login')
def following(request, id):
    followings = User.objects.get(id= id).followings.all()
    
    context = {
        'users' : followings
    }
    return render(request, 'following.html',context)


def user_search(request):
        if request.method == 'POST':
            search_text = request.POST['search']
            
            users = User.objects.filter(
                Q(username__icontains = search_text),
                Q(name__icontains = search_text),
                
            )
            
            context = {
                'users' : users,
            }
            
            return render(request, 'user-search.html', context)
        
login_required(login_url='login')        
def rooms(request):
    if request.method == 'POST':
        text = request.POST['search_text']
        rooms = Room.objects.filter(Q(title__icontains = text))
        context = {
            'rooms' : rooms,
        } 
        return render(request, 'rooms.html', context)
    
    print('OUTSIDE')
    rooms = Room.objects.all()
    context = {
        'rooms' : rooms
    }
    return render(request, 'rooms.html', context)

@login_required(login_url='login')
def add_room(request):
    
    topics = Topic.objects.all()
    
    if request.method == 'POST' :
         
        form = RoomForm(request.POST)
        
        topic = request.POST['topic']
        title = request.POST['title']
        
        topic_obj = Topic(body = topic)
        topic_obj.save()
        
        room = Room(host=request.user, title=title, topic=topic_obj)
        room.save()
        return redirect('rooms')
    
    form = RoomForm()
    
    context = {
        'form' : form,
        'topics' : topics
    }
    
    return render(request, 'add-room.html', context)

@login_required(login_url='login')
def room(request, id):
    room = Room.objects.get(id = id)
    if request.method == 'POST':
        body = request.POST.get('body')
        image = request.FILES.get('image')
        
        if image:
            message = Message(body=body, image = image, user=request.user, room=room )
            message.save()
        else:
            message = Message(body=body, user=request.user, room=room )
            message.save()
        return redirect(f'/room/{room.id}')
    messages = Message.objects.filter(room=room).order_by('-date')
    context = {
        'room' : room,
        'messages' : messages
    }
    
    return render(request, 'room.html', context)

@login_required(login_url='login')
def get_messages(request, id):
    messages = Message.objects.filter(room__id=id).order_by('-date').values()
    
    data = {
        'messages' : list(messages),
    }
    
    return JsonResponse(data)
    

@login_required(login_url='login')
def resumes(request):
    resumes = Resume.objects.filter(user = request.user).order_by('-date')
    context = {
        'resumes' : resumes,
    }
    
    return render(request, 'resumes.html', context)

@login_required(login_url='login')
def resume(request, id):
    resume = Resume.objects.get(id = id)
    lst = resume.programming_languages.split(',')
    context = {
        'resume': resume,
        'lst' :lst,
    }
    
    return render(request, 'resume.html', context)

@login_required(login_url='login')
def add_resume(request):
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            lang = ','.join(form.cleaned_data['programming_languages'])
            resume.programming_languages = lang
            img = request.FILES.get('image')
            if img:
                resume.image = img
            resume.user = request.user
            resume.save()
            return redirect(f'resume/{resume.id}')
        else:
            messages.info(request, 'Invalid info')
            form = ResumeForm(request.POST, request.FILES)
            context = {
                'form' : form,
                }
            return render(request, 'add-resume.html', context)
       
    form = ResumeForm()
    
    context = {
        'form' : form,
    }
    
    return render(request, 'add-resume.html', context)

@login_required(login_url='login')    
def polls(request):
    polls = Poll.objects.all().order_by('-date')
    
    context = {
        'polls' : polls
    }
    
    return render(request, 'polls.html', context )

@login_required(login_url='login')
def add_poll(request):
    if request.method == 'POST':
        title = request.POST['title']
        choices_str = request.POST['choices']
        
        choices = choices_str.strip().split(',')
        choices.pop()
        
        poll = Poll(host=request.user, title=title)
        poll.save()
        
        for choice in choices:
            new_choice = Choice(body = choice)
            new_choice.save()
            poll.choices.add(new_choice)
        
        poll.save()
         
        return HttpResponse('success')
    return render(request, 'add-poll.html')

@login_required(login_url='login')
def poll(request, id):
    poll = Poll.objects.get(id = id)
    voted = False
    
    if request.user in poll.voters.all():
        voted = True
    
    context = {
        'poll' : poll,
        'voted' : voted,
        
    }
    return render(request, 'poll.html', context)

@login_required(login_url='login')
def poll_vote(request):
    
    
    choice_id = request.GET.get('choice')
    poll_id = request.GET.get('poll')
    
    
    poll = Poll.objects.get(id = poll_id)
    choice = poll.choices.get(id = choice_id)
    
    voted = False
    
    if request.user in poll.voters.all():
        voted = True
    
    if voted:
        return redirect(f"/poll/{poll_id}")
    
    poll.voters.add(request.user)
    
    
    choice.votes = choice.votes + 1
    
    choice.save()
    return redirect(f"/poll/{poll_id}")

