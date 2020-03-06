from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class PostAuthor(AbstractUser):

    class Meta:
        verbose_name = u'Автор'
        verbose_name_plural = u'Авторы'

    def __init__(self, *args, **kwargs):
        super(PostAuthor, self).__init__(*args, **kwargs)
        self._meta.get_field('password').verbose_name = u'Пароль'
        self._meta.get_field('username').verbose_name = u'Никнейм'
        self._meta.get_field('username').help_text = u'Обязательное поле. Не более 150 символов. Только буквы, цифры и спецсимволы @/./+/-/_'
        self._meta.get_field('first_name').verbose_name = u'Имя'
        self._meta.get_field('last_name').verbose_name = u'Фамилия'
        self._meta.get_field('email').verbose_name = u'Электронный адрес'

    def __str__(self):
        return self.username

class Category(models.Model):
    title = models.CharField(
        verbose_name = u'Название категории',
        max_length=255,
        blank=True
        )
    slug = models.SlugField(
        verbose_name = u'Слаг (метка) категории',
        max_length=64,
        blank=True,
        default=None
        )

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def get_slug_by_name(name):
        slovar = {
            'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h',
            'J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q',
            'R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y',
            'Z':'z','а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
            'ж':'zh','з':'z','и':'i','й':'j','к':'k','л':'l','м':'m','н':'n',
            'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
            'ц':'c','ч':'ch','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
            'ю':'yu','я':'ya','А':'a','Б':'b','В':'v','Г':'g','Д':'d','Е':'e',
            'Ё':'yo','Ж':'zh','З':'z','И':'i','Й':'j','К':'k','Л':'l','М':'m',
            'Н':'n','О':'o','П':'p','Р':'r','С':'s','Т':'t','У':'u','Ф':'f',
            'Х':'h','Ц':'c','Ч':'ch','Ш':'sh','Щ':'sch','Ъ':'','Ы':'y','Ь':'',
            'Э':'e','Ю':'yu','Я':'ya',',':'','?':'','~':'','!':'','@':'','#':'',
            '$':'','%':'','^':'','&':'','*':'','(':'',')':'','=':'','+':'',
            ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
            '[':'',']':'','{':'','}':'','ґ':'','ї':'','є':'','Ґ':'g','Ї':'i',
            'Є':'e',' — ':'-',' – ':'-',' - ':'-','–':'','—':'',' ':'-'}
        for key in slovar:
            name = name.replace(key, slovar[key])
        return name

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(
        verbose_name = u'Название публикации',
        help_text = u'Обязательное поле',
        max_length=255
        )
    slug = models.SlugField(
        u'Слаг (метка) публикации',
        help_text = u'Поле можно оставить пустым. Автоматически сгенерируется',
        max_length=64,
        blank=True,
        default=None
        )
    status = models.CharField(
        verbose_name = u'Статус публикации',
        max_length=32,
        choices=[
            ('D', 'Черновик'),
            ('P', 'Опубликованное')
            ]
        )
    content = models.TextField(
        verbose_name = u'Содержание публикации',
        help_text = u'Обязательное поле'
        )
    updated = models.DateTimeField(
        verbose_name = u'Обновлено',
        default=timezone.now)
    publication_date = models.DateTimeField(
        verbose_name = u'Дата публикации',
        default=timezone.now
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
        verbose_name = u'Категория',
        related_name = 'posts'
        )
    author = models.ForeignKey(
        PostAuthor,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        verbose_name = u'Автор',
        related_name = 'posts'
        )

    class Meta:
        verbose_name = u'Публикация'
        verbose_name_plural = u'Публикации'

    def __str__(self):
        return f"#{self.id}: {self.title}"