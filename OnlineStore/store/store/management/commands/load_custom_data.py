import json
from django.core.management.base import BaseCommand
from store.models import Item, ItemTag

class Command(BaseCommand):
    help = 'Load data from JSON file'

    def handle(self, *args, **kwargs):
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            for item in data:
                model = item['model']
                pk = item['pk']
                fields = item['fields']
                
                if model == 'store.itemtag':
                    ItemTag.objects.update_or_create(pk=pk, defaults=fields)
                elif model == 'store.item':
                    tags_slugs = fields.pop('tags', [])
                    item_instance, _ = Item.objects.update_or_create(pk=pk, defaults=fields)
                    item_instance.tags.set(tags_slugs)
                    item_instance.save()
                    
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
