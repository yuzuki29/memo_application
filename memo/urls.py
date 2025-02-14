from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  #一覧
    path('tag_list', views.TagListView.as_view(), name='tag_list'),  #タグ一覧
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),   # メモ詳細
    path('create/', views.CreateView.as_view(), name='create'),     # 新規投稿ページ
    path('tag_create/', views.TagCreateView.as_view(), name='tag_create'), 
    path('<int:pk>/update/', views.UpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name="delete"), 
    path('tag_delete/', views.TagBulkDeleteView.as_view(), name="tag_delete"),
    path('search/', views.search_memo, name='search'), 
]