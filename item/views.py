from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Item,Category
from .forms import NewItemForm,EditItemForm
from django.db.models import Q
# Create your views here.
def items(request):
    items=Item.objects.filter(is_sold=False)
    categores=Category.objects.all()
    category_id=request.GET.get('category')
    query=request.GET.get('query','')
    if query:
        items=items.filter(Q(name__icontains=query) |
                           Q(description__icontains=query)
                           )
    if category_id:
        items=items.filter(category_id=category_id)

    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'categories':categores,
        'category_id':category_id
        })

def detail(request, pk):
    item=get_object_or_404(Item , pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        'item': item,
        'related_items':related_items
    })

@login_required
def newitem(request):
    if request.method == "POST":
        form=NewItemForm(request.POST , request.FILES)



        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form=NewItemForm()


    return render(request,'item/form.html',{
        'form':form,
        'title':'New Item'
    })




def edititem(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user) 

    if request.method == "POST":
        print('sabah')
        form = EditItemForm(request.POST , request.FILES ,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)
       
    return render(request,'item/form.html',{
        'form':form,
        'title':'Edit Item'
    })




@login_required
def deleteitem(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('dashboard:index')