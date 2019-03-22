from django.shortcuts import render

# Create your views here.
from .models import InfoModelForm
from django.shortcuts import redirect
from .forms import InfoModelFormAdd

def index(request):
    return render(request, 'lists_index.html', {})

def info(request):
    infodata = InfoModelForm.objects.all()
    header = ['Id','Name','Mail','Gender','Organization','Years','CreateDate']
    my_dict2 = {
        'title':'test',
        'val':infodata,
        'header':header
    }
    return render(request, 'info.html',my_dict2)

def create(request):
    if (request.method == 'POST'):
        obj = InfoModelForm()
        info = InfoModelFormAdd(request.POST,instance=obj)
        info.save()
        return redirect(to='/lists/info')
    modelform_dict = {
        'title':'modelformTest',
        'form':InfoModelFormAdd(),
    }
    return render(request, 'create.html',modelform_dict)

def update(request, num):
    obj = InfoModelForm.objects.get(id=num)
    # when Post
    if (request.method == 'POST'):
        info = InfoModelFormAdd(request.POST, instance=obj)
        info.save()
        return redirect(to='/lists/info')
    update_dict = {
        'title':'Update Info',
        'id':num,
        'form':InfoModelFormAdd(instance=obj),
    }
    return render(request, 'update.html',update_dict)

from django.http import HttpResponse
from django.urls import reverse
def test(request):
    return HttpResponse("hoge")
#def test(request, num):
#    urlName = reverse('suburl', args=[num])
#    return HttpResponse("testtest {0} url={1}".format(num, urlName))
