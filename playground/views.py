from django.shortcuts import render
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Sum, Max, Min, Avg, Count
from django.contrib.contenttypes.models import ContentType
from django.db import transaction


from store.models import OrderItem, Product, Order, Customer, Collection
from tags.models import TaggedItem


def say_hello(request):

    return render(request, 'hello.html', {'name': 'Mosh'})
