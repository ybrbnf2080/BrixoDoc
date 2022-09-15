from django.urls import path, include, re_path

from rest_framework import routers

from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
    re_path("api/v1/article/$", views.ArticleAPIView.as_view()),
    path("api/v1/article/<int:pk>/", views.ArticleAPIViewItem.as_view()),

    path("api/v1/references/<int:art_no_id>/", views.ReferencesAPIViewItem.as_view()),
    path("api/v1/manufacture_search/<str:short_name>/", views.ManufactureSearchAPIViewItem.as_view()),
    path("api/v1/reference_search/<str:ref_no>/", views.ReferencesAPIViewItem.as_view()),
    path("api/v1/crit/<int:art_no_id>/", views.CharacteristicsAPIViewItem.as_view()),
    path("api/v1/document/<int:art_no_id>/", views.DocAPIViewItem.as_view()),

    path("api/v1/article/brand_filter/<int:brand_no>/", views.ArticleFilterBrandAPIViewItem.as_view()),
    path("api/v1/article/search/<str:art_no>/", views.ArticleSearchAPIViewItem.as_view()),
    path("api/v1/article/export/", views.GetExportTafAPIView.as_view()),
    path("api/v1/article/import/", views.GetImportTafAPIView.as_view()),
    path("api/v1/article/import/", views.GetImportTafAPIView.as_view()),
]
