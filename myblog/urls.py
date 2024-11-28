from django.urls import path
from .views import MainView, AboutView, PostDetailView, ContactView, SignUpView, SignInView, logout_view, FeedBackView, SuccessView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('', logout_view, name='index'),
    path('signout/', logout_view, name='signout'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', FeedBackView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
]