from datetime import date
from math import prod
from multiprocessing import context
from django.shortcuts import redirect, render

from core.models import product
# Create your views here.
def search(request):

    if request.method == "POST":
        print('SEARCH FORM POST CONTENTS ', request.POST)

        products = product.objects.all()
        
        date_from = request.POST.get('date_from', None)
        date_to = request.POST.get('date_to', None)
        user_id = request.POST.get('user_id', None)

        print('aaaaaaaaaaaaa' , date_from, date_to, user_id)

        if date_from == date_to == user_id == '':
            print('error select one')
            context = {
                'error_message' : " エラー：　※　少なくとも1つを選択してください"
            }

            return render(request, 'management/kensaku.html' , context)
        
        #Filter based on from date
        
        if date_from:
            products = product.objects.all().filter(created_at__gte = date_from)
        
        if date_to:
            products = product.objects.all().filter(created_at__lte = date_to)

        # Filtering based on ID
        if user_id:
            products = product.objects.all().filter(id = user_id)

        context = {
            'products' : products
        }

        return render(request, 'management/kensaku.html' , context)

    else:
        #GET REQUEST   
        return render(request, 'management/kensaku.html')


def search_form_action(request):

    print('search_form_action')

    if request.method == "POST":

        print('the search form action contents are ', request.POST)
        return redirect('https://www.google.com')

    else:

        return redirect('https://www.google.com')
