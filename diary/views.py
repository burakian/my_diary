from django.shortcuts import render,redirect,get_object_or_404
from .forms import NippoModelForm
from .models import Day
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import tukiate
class IndexView(generic.ListView):
    model=Day
    paginate_by=3
class AddView(LoginRequiredMixin,generic.CreateView):
    model=Day
    form_class=NippoModelForm
    success_url=reverse_lazy("diary:index")
class UpdateView(LoginRequiredMixin,generic.UpdateView):
    model=Day
    form_class=NippoModelForm
    success_url=reverse_lazy("diary:index")

class DeleteView(LoginRequiredMixin,generic.DeleteView):
    model=Day
    success_url=reverse_lazy("diary:index")
class DetailView(generic.DetailView):
    model=Day

# class ImagesCreateView(CreateView):
#     template_name = 'img/image_form.html' # 上記のTemplateのパス
#     form_class = Day # 上記のFormを設定

#     def post(self, request, *args, **kwargs):   # リクエストがpostの際の処理をオーバーライドして記載
#         form = Day(request.POST, request.FILES) 
#         if not form.is_valid(): # validationでエラーがあれば、formに戻る（エラーメッセージを返す）
#             return render(request, self.template_name, {'form': form}, )
#         form.save() # formを保存
#         return redirect(reverse_lazy('image:index')) # 成功した際の遷移先

def top(request):
    ctx={}
    ctx={
        "tukiate":tukiate.hinichi()
    }
    return render(request,"diary/top.html",ctx)