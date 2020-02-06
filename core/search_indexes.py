import datetime
from haystack import indexes
from .models import Item, Wholesaler, Order


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    #pub_date = models.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Item

#    def index_queryset(self, using=None):
#        """Used when the entire index for model is updated."""
#        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
