import self as self
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Articles, CheckArticles
from .forms import ArticlesForm, CheckArticlesForm, create_news_form
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test


def moderator_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.groups.filter(name='Модератор').exists())
    return decorated_view_func(view_func)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news-detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView, LoginRequiredMixin):
    model = Articles
    template_name = 'news/update.html'
    form_class = ArticlesForm
    raise_exception = True


class NewsDeleteView(DeleteView, LoginRequiredMixin):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/news'
    raise_exception = True


class CheckNewsUpdateView(UpdateView, LoginRequiredMixin):
    model = CheckArticles
    template_name = 'news/update.html'
    form_class = ArticlesForm
    raise_exception = True


class CheckNewsDeleteView(DeleteView, LoginRequiredMixin):
    model = CheckArticles
    template_name = 'news/check-delete-confirm.html'
    success_url = '/news/check'
    raise_exception = True


def news(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})


@login_required
def create_news(request):
    if request.method == 'POST':
        form = create_news_form(request.POST)
        if form.is_valid():
            try:
                CheckArticles.objects.create(**form.cleaned_data)
                return redirect('news')
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = create_news_form()
    return render(request, 'news/create.html', {'form': form})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CheckArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'

    form = CheckArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


@login_required
def check_suggested_news(request):
    if request.method == 'POST':
        if request.POST.get('btn_type') == 'add':
            id = request.POST.get('id')  # получаем значение id
            check_article = CheckArticles.objects.get(id=id)
            article = Articles()  # создаем новый экземпляр класса Articles
            article.title = check_article.title  # присваиваем значения полям нового объекта из записи check_article
            article.anons = check_article.anons
            article.full_text = check_article.full_text
            article.date = check_article.date
            article.img_url = check_article.img_url
            article.save()  # сохраняем новую запись в таблице articles
            check_article.delete()  # удаляем запись из таблицы checkarticles

    check_news = CheckArticles.objects.order_by('-date')
    return render(request, 'news/check.html', {'check_news': check_news})
