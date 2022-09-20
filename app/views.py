from django.shortcuts import render
from .models import Book
from .forms import SignUpForm
from django.contrib.auth.models import User,Group

# Create your views here.
def home(request):
    books=Book.objects.all()
    return render(request, 'home.html',{'books':books})

def librarian_view(request):
    fm=SignUpForm()
    return render(request, 'librarian.html',{'fm':fm})

def member_view(request):
        return render(request, 'member.html')


def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        mem_type = request.POST['mem']
        user=User.objects.create(username=username,first_name=fname, last_name=lname,password=pass1)
        if mem_type=='librarian':
               group=Group.objects.get(name='librarian')
               group.user_set.add(user) 
        if mem_type=='member':
               group=Group.objects.get(name='member')
               group.user_set.add(user) 
        
        print(fname,lname,username,pass1,pass2,mem_type)

     
        return render(request, 'signup.html')
    else:
         return render(request, 'signup.html')



def login_view(request):
    return render(request,'login.html')