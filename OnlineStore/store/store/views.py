from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Avg
from .models import Item, ItemTag, Comment
from .forms import CommentForm, SearchForm
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from taggit.models import Tag
from .paginator import paginator


def item_details(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    comments = Comment.objects.filter(item=item)
    average_rating = item.comments.aggregate(average=Avg('rating'))['average'] or 0
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.item = item
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, 'store/item_details.html', {
        'item': item,
        'comments': comments,
        'form': form,
        'average_rating': average_rating,
    })

def store(request):
    form = SearchForm(request.GET or None)
    query = request.GET.get('query', None)
    items = Item.objects.none()

    if query:
        items = Item.objects.all()
        items = sorted(items, key=lambda item: (
            fuzz.partial_ratio(query.lower(), item.title.lower()),
            fuzz.partial_ratio(query.lower(), item.description.lower()),
            max((fuzz.partial_ratio(query.lower(), tag.name.lower()) for tag in item.tags.all()), default=0)
        ), reverse=True)
        
        items = [item for item in items if (
            fuzz.partial_ratio(query.lower(), item.title.lower()) > 50 or
            fuzz.partial_ratio(query.lower(), item.description.lower()) > 50 or
            any(fuzz.partial_ratio(query.lower(), tag.name.lower()) > 50 for tag in item.tags.all())
        )]

    recommended_items = Item.objects.annotate(computed_average_rating=Avg('comments__rating')).filter(computed_average_rating__gt=4)
    
    return render(request, 'store/main_page.html', {
        'recommended_items': recommended_items,
        'items': items,
        'form': form
    })

def tag_details(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    items = Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'page_obj': paginator(request, items, 3),
    }
    return render(request, 'store/tag_details.html', context)

def tag_list(request):
    tags = ItemTag.objects.all()
    context = {
        'page_obj': paginator(request, tags, 6),
    }
    return render(request, 'store/tag_list.html', context)

def page2(request):
    items = Item.objects.filter(is_available=True)
    context = {
        'page_obj': paginator(request, items, 9),
        'range': [*range(1, 7)],  # For random css styles
    }
    return render(request, 'store/main_page2.html', context)
