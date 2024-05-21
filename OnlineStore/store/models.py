from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase
from django.contrib.auth.models import User
from django.db.models import Avg

class ItemTag(TagBase):
    image = models.ImageField(
        upload_to='categories/',
        verbose_name='Изображение',
        blank=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
    )

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

class TaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(
        ItemTag,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name='Категория',
    )

class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название',)
    description = models.TextField(verbose_name='Описание',)
    slug = models.CharField(
        unique=True,
        max_length=50,
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления',)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Новая цена',
    )
    old_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Старая цена',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='items/',
        blank=True,
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='Доступно',
    )
    tags = TaggableManager(through='taggit.TaggedItem', related_name="tagged_items", verbose_name='Категории',)
    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
        verbose_name='Средняя оценка'
    )

    def update_average_rating(self):
        avg_rating = self.comments.aggregate(average=Avg('rating'))['average']
        self.average_rating = avg_rating if avg_rating else 0
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} ({self.rating} stars)'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'