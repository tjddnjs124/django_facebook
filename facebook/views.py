from django.shortcuts import render , redirect
from facebook.models import Article, Page, Comment

count = 0
count2 = 0

# Create your views here.
def play(request):
    return render(request, 'play.html')

def play2(request):
    lee = '이'
    global count
    count = count + 1
    return render(request, 'play2.html', {'name' : lee, 'cnt' : count})

def profile(request):
    return render(request, 'profile.html')

def event(request):
    global count2
    count2 = count2 + 1
    check = False
    if count2 ==7:
        check = True
    return render(request, 'event.html', {'cnt' : count2, 'check' : check})

def newsfeed(request):
    articles = Article.objects.all()

    return render(request, 'newsfeed.html', {'articles' : articles })

def detail_feed(request, pk):
    article = Article.objects.get(pk = pk)

    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            author = request.POST['nickname'],
            text = request.POST['reply'],
            password = request.POST['password']
        )
        return redirect(f'/feed/{article.pk}')
    return render(request, 'detail_feed.html', {'feed' : article})

def pages(request):
    pages = Page.objects.all()
    return render(request, 'pages.html', {'pages' : pages})

def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            text = request.POST['content']
            text = text + ' - thank you !'
            new_article = Article.objects.create(
                author = request.POST['author'],
                title = request.POST['title'],
                text = request.POST['content'],
                password = request.POST['password'],
            )
            return redirect(f'/feed/{new_article.pk}')
    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk =pk)
    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()
            return redirect('/')
    return render(request, 'remove_feed.html', {'feed' : article})

def edit_feed(request,pk):
    article = Article.objects.get(pk = pk)
    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{article.pk}')
    return render(request, 'edit_feed.html',{'feed' : article})

def fail(request):
    return render(request, 'fail.html')