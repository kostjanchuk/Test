from django.urls import path, include
# from .views import WomenApiView, WomenApiList, WomenUpdateApiView
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)

print(router.urls)
urlpatterns = [
    # path('womenlist/', WomenApiView.as_view()),
    # path('womenlist/<int:pk>/', WomenApiView.as_view()),
    # path('womenlist2/', WomenApiList.as_view()),
    # path('womenlist2/<int:pk>/', WomenApiList.as_view()),
    # path('womenlist/update/', WomenUpdateApiView.as_view()),
    # path('womenlist/update/<int:pk>/', WomenUpdateApiView.as_view()),
    # path('womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('', include(router.urls)),
    path('womenlist/', WomenApiList.as_view()),
    path('womenlist/<int:pk>/', WomenApiUpdate.as_view()),
    path('womendelete/<int:pk>/', WomenApiDestroy.as_view()),
]