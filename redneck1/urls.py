from django.urls import path
from . import views

urlpatterns=[
path("",views.index,name='index'),
path("ships",views.ships,name='ships'),
path("crew",views.crew,name='crew'),
path("createaccount",views.createaccount,name='createaccount'),
path("accountsubmit",views.accountsubmit,name='accountsubmit'),
path("login",views.login_view,name='loginview'),
path("loginsubmit",views.loginsubmit,name='loginsubmit'),
path("log_user_out",views.log_user_out,name='userlogout'),
path("times",views.times,name='times'),
path("cruises/<int:cruise_id>",views.cruiseinfo,name='details'),
path("reviews",views.reviews,name='reviews'),
path("review",views.review_form,name='reviewform'),
path("reviewsub",views.reviewsubmit,name='reviewsubmit'),
path("gettix",views.gettix,name='gettix'),
path("tixsubmit",views.ticketsubmit,name='ticketsubmit'),
path("merch",views.merch,name='merch'),
path("merch/smokeyt",views.smokeyt,name='smokeyt'),
path("merch/swamplifet",views.swamplifet,name='swamplifet'),
path("merch/swamplaket",views.swamplaket,name='swamplaket'),
path("merch/pieceofshipt",views.pieceofshipt,name='pieceofshipt'),
path("merch/fordt",views.fordt,name='fordt'),
path("merch/addtocart",views.addtocart,name='addtocart'),
path("merch/cart",views.shoppingcart,name='cart'),
path("merch/cartremove",views.cartremove,name='cartremove'),
]