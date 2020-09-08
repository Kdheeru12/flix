from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from .models import viewer,Languages,Genre,Movies
from django.contrib import messages
from .form import MoviesForm
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        try:
            viewe = get_object_or_404(viewer,user=request.user)
            print(viewe)
            
        except:
            return redirect('/verification')
        return render(request,'index.html')
    else:
        return redirect('/login')
def signup(request):
    return render(request,'register.html')
def verification(request):
    if request.method == 'POST':
        m = request.POST['mobile']        
        number = viewer.objects.filter(mobile=m)
        if number:
            messages.info(request,'Moblie Already exist')
            return render(request,'mobile_verify.html')
        else:
            import urllib.request
            import urllib.parse
            import random
            otp = random.randint(100000,999999)
            globals()['otp']=otp
            globals()['mobile']=m
            def sendSMS(apikey, numbers, sender, message):
                params = {'apikey':'fJfBJnyz91c-TbqrXa8U1yvh9RFUFlIIypeUFJkyJN', 'numbers': numbers, 'message' : message, 'sender': sender}
                f = urllib.request.urlopen('https://api.textlocal.in/send/?'
                    + urllib.parse.urlencode(params))
                return (f.read(), f.code)

            resp, code = sendSMS('fJfBJnyz91c-TbqrXa8U1yvh9RFUFlIIypeUFJkyJN',  str(m),
                'TXTLCL', 'hello user otp for verification is "'+str(otp)+'" ')
            print(resp)
            context = {
            'mobile':m,
            }
            return render(request,'otp.html',context)
        return render(request,'mobile_verify.html')
    else:
        return render(request,'mobile_verify.html')
def otpverify(request):
    otp1 = otp
    if request.user.is_authenticated:
        if request.method == 'POST':
            ot = request.POST['otp']
            m = int(request.POST['mobile'])
            if otp1 == int(ot):
                view = viewer(user=request.user,mobile=m)
                view.save()
                return redirect('/')
            else:
                mobile = m
                messages.info(request,'invalid otp exist')
                return render(request,'otp.html',{'mobile':mobile})
        else:
            return render(request,'otp.html')
    else:
        return redirect('/')      
def login(request):
    return render(request,'creator-index.html')
def languages(request):
    if request.method == 'POST':
        lan = int(request.POST['la'])
        language=get_object_or_404(Languages,id=lan)
        language.delete()
        return redirect('/languages')
    else:
        lang = Languages.objects.all()
        return render(request,'admin-language.html',{'lang':lang})
def lanadd(request):
    if request.method == 'POST':
        langu = request.POST['lan']
        la = Languages(language=langu)
        la.save()
        return redirect('/languages')
    else:
        return render(request,'admin-language-add.html')
def lanedit(request,id):
    if request.method == 'POST':
        l = request.POST['edit']
        lan=get_object_or_404(Languages,id=int(id))
        print(lan)
        lan.language=l
        lan.save()
        print(lan)
        return redirect('/languages') 
    else:
        lan=get_object_or_404(Languages,id=int(id))
        return render(request,'admin-language-edit.html',{'lan':lan})
def genres(request):
    if request.method == 'POST':
        lan = int(request.POST['la'])
        language=get_object_or_404(Genre,id=lan)
        language.delete()
        return redirect('/geners')
    else:
        lang = Genre.objects.all()
        return render(request,'admin-genre.html',{'lang':lang})
def genresdd(request):
    if request.method == 'POST':
        langu = request.POST['gen']
        la = Genre(geners=langu)
        la.save()
        return redirect('/geners')
    else:
        return render(request,'admin-genre-add.html')
def genresdit(request,id):
    if request.method == 'POST':
        l = request.POST['edit']
        lan=get_object_or_404(Genre,id=int(id))
        print(lan)
        lan.Genre=l
        lan.save()
        print(lan)
        return redirect('/genres') 
    else:
        lan=get_object_or_404(Genre,id=int(id))
        return render(request,'admin-language-edit.html',{'lan':lan})
def profile(request):
    return render(request,'profile.html')
def creator(request):
    return render(request,'creator-index.html')
def creatorprofile(request):
    return render(request,'creator-profile.html')
def creatorvideos(request):
    movies = Movies.objects.filter(creator=request.user)
    context = {
        'movies':movies
    }
    return render(request,'creator-videos.html',context)
def creatorvideosadd(request):
    if request.method == 'POST':
        print('hhh')
        form = MoviesForm(request.POST,request.FILES or None)
        print(form.is_valid())
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
        return redirect('/creator-videos')
        
    else:
        form = MoviesForm()
        context ={
            'form':form
        }
        return render(request,'creator-videos-add.html',context)
def creatororders(request):
    return render(request,'creator-orders.html')
def creatorinvoice(request):
    return render(request,'creator-invoice.html')