from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Cruise,Review,Passenger,Product,ShoppingCartItem
from django.core.exceptions import ValidationError
from django.http import HttpResponse,JsonResponse
from django.db.models import Sum
# Create your views here.
#renders main page
def index(request):
    context = {
    "isauth":request.user.is_authenticated
    }
    return render(request,'redneck1/pag1.html',context)

#renders page w/info about ships
def ships(request):
    return render(request,'redneck1/page2.html')

#renders page w/info about crew
def crew(request):
    return render(request,'redneck1/page3.html')

#Next two methods are the account creation page+submission handling
def createaccount(request):
    return render(request,'redneck1/createaccount.html')
def accountsubmit(request):
    try:
        password=request.POST['passcode']
        username=request.POST['username']
        user=User.objects.create_user(username=username,password=password)
        user.save()
    except KeyError:
        address=reverse('createaccount')
        return render(request,'redneck1/error.html',{"problem":"account not created","message":"You left some input fields blank","address":address})
    except IntegrityError:
        address=reverse('createaccount')
        return render(request,'redneck1/error.html',{"problem":"account not created","message":"That username already exists","address":address})
    return render(request,'redneck1/createsuccess.html')

#next three method render login page and login handling as well logout
def login_view(request):
    return render(request,'redneck1/login.html')
def loginsubmit(request):
    username=request.POST['username']
    password=request.POST['passcode']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return render(request,'redneck1/loggedin.html')
    else:
        address=reverse('loginview')
        return render(request,'redneck1/error.html',{"problem":"Not logged in","message":"Either the username or password was invalid","address":address})
def log_user_out(request):
    logout(request)
    return redirect('index')

#renders arrival/departures
def times(request):
    context={
    'cruises':Cruise.objects.all()
    }
    return render(request,'redneck1/page4.html',context)

#renders details page for each cruise
def cruiseinfo(request,cruise_id):
    cruise=Cruise.objects.get(pk=cruise_id)
    context={
    'cruise':cruise,
    'passengers':cruise.passengers.all()
    }
    return render(request,'redneck1/details.html',context)

#next few methods render testimonials page as well as review submission and handling
def reviews(request):
    context={
    'reviews':Review.objects.all()
    }
    return render(request,'redneck1/reviews.html',context)
def review_form(request):
    context={
    'cruises':Cruise.objects.all()
    }
    return render(request,'redneck1/reviewform.html',context)
def reviewsubmit(request):
    try:
        cruise=Cruise.objects.get(pk=int(request.POST['cruise']))
        contents=request.POST['reviewcontents']
        print(request.user)
        if len(contents)<11:
            address=reverse('reviewform')
            return render(request,'redneck1/error.html',{'problem':'Review not submitted','message':'The length of the review was too short','address':address})
        review=Review(username=User.objects.get(username=request.user),cruise=cruise,contents=contents)
        review.save()
    except KeyError:
        address=reverse('reviewform')
        return render(request,'redneck1/error.html',{'problem':'Review not submitted','message':'You left either the contents or the select field blank','address':address})
    return redirect('reviews')
#next few methods deal w/ticketing, issuing new tickets, etc
def gettix(request):
    context={
    'cruises':Cruise.objects.all()
    }
    return render(request,'redneck1/gettix.html',context)
def ticketsubmit(request):
    try:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        cruise=Cruise.objects.get(pk=int(request.POST['cruise']))
        passenger=Passenger(first_name=first_name,last_name=last_name,cruise=cruise)
        passenger.save()
        context={
        'passengername':first_name+" "+last_name,
        'cruise':cruise

        }
    except KeyError:
        address=reverse('gettix')
        return render(request,'redneck1/error.html',{'problem':'tickets not booked','message': 'one or more fields was not entered','address':address})
    return render(request,'redneck1/gottix.html',context)

#renders the merch page and detail pages for each T
def merch(request):
    return render(request,'redneck1/merch.html')
def smokeyt(request):
    return render(request,'redneck1/smokeyt.html')
def swamplifet(request):
    return render(request,'redneck1/swamplifet.html')
def swamplaket(request):
    return render(request,'redneck1/swamplake.html')
def pieceofshipt(request):
    return render(request,'redneck1/pieceofship.html')
def fordt(request):
    return render(request,'redneck1/ford.html')

#url to handle adding something to cart
def addtocart(request):
    try:
        name=request.POST['name']
        quantity=int(request.POST['quantity'])
        user=User.objects.get(username=request.user)
        product=Product.objects.get(name=name)
        price=product.price*quantity
        cartitem=ShoppingCartItem(username=user,product=product,quantity=quantity,price=price)
        cartitem.save()
    except KeyError:
        address=reverse('merch')
        return render(request,'redneck1/error.html',{'problem':'Item not added to cart','message': 'one or more fields was not entered','address':address})
    except ValidationError:
        address=reverse('merch')
        return render(request,'redneck1/error.html',{'problem':'Item not added to cart','message': 'You entered an invalid input in the quantity field','address':address})
    return redirect('merch')
#renders the shopping cart
def shoppingcart(request):
    name=request.user
    cartitems=User.objects.get(username=request.user).shoppingcart.all()
    total=cartitems.aggregate(total=Sum('price'))['total']
    if total is not None:
        totalstr='{:,.2f}'.format(total)
    else:
        totalstr="0.00"
    print(total)
    context={
    'username':name,
    'cart':cartitems,
    'total':totalstr,
    }
    return render(request,'redneck1/shoppingcart.html',context)
def cartremove(request):
    if request.method == 'POST':
        item_id=int(request.POST['item_id'])
        total=float(request.POST['current_total'])
        cartitem=ShoppingCartItem.objects.get(id=item_id)
        total-=cartitem.price
        totalstr='{:,.2f}'.format(total)
        cartitem.delete()
        return JsonResponse({'newtotal':totalstr})
    else:
        response=HttpResponse('request not a post')
        return reponse
