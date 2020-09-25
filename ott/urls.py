from django.contrib import admin
from django.urls import path,include,re_path
from .import views
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from ott.views import PostDetailView


urlpatterns = [
    path('',views.homepage,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('verification',views.verification,name='verify'),
    path('otp-verify',views.otpverify,name='verify'),
    path('languages',views.languages,name='language'),
    path('languages-add',views.lanadd,name='lanadd'),
    path('<id>/lan-edit',views.lanedit,name='lanedit'),
    path('geners',views.genres,name='language'),
    path('geners-add',views.genresdd,name='lanadd'),
    path('<id>/geners-edit',views.genresdit,name='lanedit'),
    path('profile',views.profile,name='profile'),
    path('creator',views.creator),
    path('creator-profile',views.creatorprofile),
    path('creator-videos',views.creatorvideos),
    path('creator-videos-add',views.creatorvideosadd),
    path('creator-orders',views.creatororders),
    path('creator-invoice',views.creatorinvoice),
    path('<slug>/movie-details',views.moviedetail),
    path('<movie>/add-crew',views.addcrew),
    path('adminstrator',views.adminstrator),
    path('admin-contentcreator',views.admincontentcreator),
    path('admin-viewers',views.adminviewers),
    path('admin-languages',views.adminlan),
    path('admin-genre',views.admingenres),
    path('admin-age',views.adminage),
    path('admin-guidance',views.adminguidance),
    path('admin-videos',views.adminvideos),
    path('accounts/inactive/',views.homepage),
    path('categories',views.categories),
    path('coming_soon',views.comingsoon),
    path('favoriesl',views.favo),
    path('newarrival',views.newarrivals),
    path('order_history',views.orders),
    path('towatch',views.towatch),
    path('trending',views.trending),
    path('likes',views.likes,name='likes'),
    path('bookmarks',views.bookmark,name='bookmarks'),
    path('serialized/<slug>',views.post_serialized_view,name='serialized'),
    #path('<slug>/view_video',views.videoview),
    path('admin-banner',views.banner),
    path('search_query=<slug>',views.search),
    path('<slug:slug>/view_video', PostDetailView.as_view(), name='detail'),
]