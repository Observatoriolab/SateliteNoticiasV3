from django.urls import include, path
from rest_framework.routers import DefaultRouter
from backend.news.api import views as qv

router = DefaultRouter()
#API ENDPOINTS NEWS GENERAL (CRUD)
router.register(r"news", qv.NewsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    
    #Para sacar las noticias correspondientes a tags determinados
    path("news/tags/<str:value>/",
        qv.NewsListAPIView.as_view(),
        name="news-list"),

    path("news/<int:pk>/rating/",
        qv.NewsRatingAPIView.as_view(),
        name="news-rating"),

    #API ENDPOINTS COMMENT
    path("news/<slug:slug>/comments/",
        qv.CommentListAPIView.as_view(),
        name="comment-list"),

    path("news/<slug:slug>/comment/",
        qv.CommentCreateAPIView.as_view(),
        name="comment-create"),

     path("comments/<int:pk>/",
        qv.CommentRUDAPIView.as_view(),
        name="comment-detail"),

     path("comments/<int:pk>/like/",
        qv.CommentLikeAPIView.as_view(),
        name="comment-like"),



    #API ENDPOINTS EDITION
    path("news/<slug:slug>/editions/",
        qv.EditionListAPIView.as_view(),
        name="edition-list"),

    path("news/<slug:slug>/edition/",
        qv.EditionCreateAPIView.as_view(),
        name="edition-create"),

     path("editions/<int:pk>/",
        qv.EditionRUDAPIView.as_view(),
        name="edition-detail"),

     path("editions/<int:pk>/like/",
        qv.EditionLikeAPIView.as_view(),
        name="edition-like")
]
    

