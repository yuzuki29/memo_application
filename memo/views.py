from django.shortcuts import render, redirect
from django.views import generic    # 汎用ビューのインポート
from .forms import MemoForm
from .models import Memo,Tag     # models.pyのMemo/Tagクラスをインポート
from django.urls import reverse_lazy 
from django.views.generic import ListView, View


def search_memo(request):
    query = request.GET.get('q')  # クエリパラメータからタグIDを取得
    if query:
        memos = Memo.objects.filter(tags__id=query)  # タグIDでフィルタリング
    else:
        memos = Memo.objects.all()  # タグが選択されていない場合、全メモを表示

    tags = Tag.objects.all()  # タグのリストを取得
    return render(request, 'memo/search.html', {'memos': memos, 'tags': tags})


class MemoListView(ListView):
    model = Memo

    def get_queryset(self):
        return Memo.objects.prefetch_related('tags').all()

# IndexViewクラスを作成
class IndexView(generic.ListView):
    model = Memo     # Memoモデルを使用
    template_name = 'memo/index.html'    # 使用するテンプレート名を指定
    
# Tag_ListViewクラスを作成
class TagListView(generic.ListView):
    model = Tag     # Memoモデルを使用
    template_name = 'memo/tag_list.html'    # 使用するテンプレート名を指定
    
# DetailViewクラスを作成
class DetailView(generic.DetailView):
    model = Memo
    template_name = 'memo/detail.html'
    
# CreateViewクラスを作成
class CreateView(generic.CreateView):
    model = Memo
    template_name = 'memo/create.html'
    form_class = MemoForm
    
# Tag_CreateViewクラスを作成　タグの作成
class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'memo/tag_create.html'
    fields = ['name']
    success_url = reverse_lazy('memo:index')
    
# UpdateViewクラスを作成
class UpdateView(generic.UpdateView):
    model = Memo
    template_name = 'memo/create.html'
    form_class = MemoForm
    
# DeleteViewクラスを作成
class DeleteView(generic.DeleteView):
    model = Memo
    template_name = 'memo/delete.html'
    success_url = reverse_lazy('memo:index')

class TagBulkDeleteView(View):
    def post(self, request, *args, **kwargs):
        tag_ids = request.POST.getlist("selected_tags")  # 選択されたタグのIDリスト
        Tag.objects.filter(id__in=tag_ids).delete()
        return redirect('memo:tag_list')