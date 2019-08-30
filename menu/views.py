from django.shortcuts import render, redirect
from django.http import Http404
from operator import attrgetter
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *


def menu_list(request):
    """
    Menu List View
    """
    all_menus = Menu.objects.all().prefetch_related('items')
    menus = []
    for menu in all_menus:
        if menu.expiration_date >= timezone.now().date():
            menus.append(menu)

    menus = sorted(menus, key=attrgetter('expiration_date'))
    return render(request, 'menu/list_all_current_menus.html', {'menus': menus})


def menu_detail(request, pk):
    """
    Menu Detail View
    """
    menu = Menu.objects.get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    """
    Item Detail View
    """
    try:
        item = Item.objects\
            .select_related('chef')\
            .prefetch_related('ingredients')\
            .get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/detail_item.html', {'item': item})


def create_new_menu(request):
    """
    Create New Menu View
    """
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            form.save_m2m()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menu/menu_edit.html', {'form': form})


def edit_menu(request, pk):
    """
    Edit Menu View
    """
    try:
        menu = Menu.objects.prefetch_related('items').get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == "POST":
        form = MenuForm(instance=menu, data=request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            form.save_m2m()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu/menu_edit.html', {'form': form})
