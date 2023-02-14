from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *


def index(request):
    return render(request, "auctions/index.html", {
        "products" : product.objects.all()
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def search(request):
    query = request.POST["q"]
    return render(request, "auctions/results.html",{
        "results" : product.objects.filter(title__contains=query)
    })

def entry(request, entry):
    if request.method == "POST":

        bid = Bids(
        user = request.user,
        listing = product.objects.get(title=entry),
        bid = request.POST.get('newbid'),
        timestamp = datetime.now())

        bid.save()
        return HttpResponseRedirect(reverse("entry",kwargs={"entry":entry}
        ))
        
    else:
        return render(request, "auctions/entry.html",{
            "product": product.objects.get(title=entry)
        })

def categoria(request, catid):
    return render(request, "auctions/category.html", {
        "listings" : product.objects.filter(categ = Cat.objects.get(category=catid)),
        "cate" : catid
        })

def publish(request):

    if request.method == "POST":

        lista = product(
            crator = request.user,
            title = request.POST.get('title').capitalize(),
            description = request.POST.get('description'),
            starting_bid = request.POST.get('starting_bid'),
            img_url = request.POST.get('img_url'),
            categ = Cat.objects.get(category=request.POST.get('categ'))
        )
        title = request.POST.get('title').capitalize()

        lista.save()
        #return HttpResponseRedirect(reverse("index"))
        return HttpResponseRedirect(reverse("entry",kwargs={"entry":title}
        ))

    else:
        return render(request , "auctions/publish.html",{
            "categories" : Cat.objects.order_by('category').values_list('category', flat=True)
        })

def watchlist(request):
    return render(request, "auctions/watchlist.html",{
    "watchlist" : User.objects.filter(watchlist)
    })
