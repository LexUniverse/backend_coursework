from .models import Articles, CheckArticles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, CharField
from django.forms.forms import Form

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'img_url']

        widgets = {
            "title": TextInput(attrs={
                'class': 'input__field',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'input__field',
                'placeholder': 'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class': 'input__field',
                'placeholder': 'Текст статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'input__field',
                'placeholder': 'year-month-day hours:minutes:seconds'
            }),
            "img_url": Textarea(attrs={
                'class': 'input__field',
                'placeholder': 'Ссылка на картинку'
            })
        }

class CheckArticlesForm(ModelForm):
    class Meta:
        model = CheckArticles
        fields = ['title', 'anons', 'full_text', 'date', 'img_url']

        widgets = {
            "title": TextInput(attrs={
                'class': 'input__field',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'input__field',
                'placeholder': 'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class': 'input__field',
                'placeholder': 'Текст статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'input__field',
                'placeholder': 'year-month-day hours:minutes:seconds'
            }),
            "img_url": Textarea(attrs={
                'class': 'input__field',
                'placeholder': 'Ссылка на картинку'
            })
        }

class create_news_form(Form):
    title = CharField(max_length=255, widget=TextInput(attrs={'class': 'input__field','placeholder': 'Название статьи'}), label='')
    anons = CharField(max_length=255, widget=TextInput(attrs={'class': 'input__field','placeholder': 'Анонс'}), label='')
    full_text = CharField(widget=Textarea(attrs={'class': 'input__field', 'placeholder': 'Текст статьи'}), label='')
    img_url = CharField(widget=Textarea(attrs={'class': 'input__field', 'placeholder': 'Ссылка на картинку'}), label='')
    class Meta:
        model = CheckArticles

