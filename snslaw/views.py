import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import MyclientForm, ClientFileForm, NewTadFileForm, UserInfoForm
from datetime import date, datetime
from .models import MyClient, PhonePrefix, Publisher, ClientFiles
from django.views.generic import ListView, DetailView
from django.utils import timezone


def index(request):
    return render(request, "snslaw/index.html")


def addrecord(request):
    submitted = False
    new_client = "No name"
    if request.method == 'POST':
        form = MyclientForm(request.POST)
        if form.is_valid():
            form.save()
            new_client = request.POST['first_name'] + " " + request.POST['last_name']
            return render(request, "snslaw/add_record.html", {"submitted": True, "new_client": new_client})
    else:
        form = MyclientForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'snslaw/add_record.html',
        {'form': form, 'submitted': submitted, 'new_client': new_client}
    )


def add(request):
    template = loader.get_template('snslaw/add.html')
    default_date = "1968-04-26"
    context = {
        'default_date': default_date,
    }
    return HttpResponse(template.render(context, request))


def calc_input(request):
    template = loader.get_template('snslaw/calc_input.html')
    # default_date = "1968-04-26"
    context = {
        # 'sum': sum1,
        # 'schat_percent': schat_percent,
    }
    return HttpResponse(template.render(context, request))

def calculate(request):
    sum1 = request.POST['sum']
    schat_percent = request.POST['schat_percent']
    res = int(sum1) * int(schat_percent)

    # }
    return render(request, "result.html", {"result": res})




def mynewfile (request):
    submitted = False
    if request.method == 'POST':
        form = ClientFileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.file_owner_id = 1
            post.save()
            return redirect('/snslaw/mynewfile/?submitted=True')
    else:
        form = ClientFileForm()

        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'snslaw/mynewfile.html',
        {'form': form, 'submitted': submitted}
    )

def newfile(request, id):
    submitted = False
    if request.method == 'POST':
        form = ClientFileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.file_owner_id = int(id)
            post.save()
            return HttpResponseRedirect('/snslaw/show_clients/?submitted=True')
    else:
        form = ClientFileForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'snslaw/newfile.html',
        {'form': form, 'submitted': submitted}
    )


# def addfile(request):
#     submitted = False
#     # current_client = MyClient.objects.filter(pk=id)
#     if request.method == 'POST':
#         form = ClientFileForm(request.POST)
#         if form.is_valid():
#             # post = form.save(commit=False)
#             # post.file_owner_id = id
#             form.save()
#             return HttpResponseRedirect('/snslaw/addfile/?submitted=True')
#     else:
#         form = ClientFileForm()
#         if 'submitted' in request.GET:
#             submitted = True
#
#     return render(request, 'snslaw/addfile.html', {'form': form, 'submitted': submitted})

def addfile(request, id):
    submitted = False
    # current_client = MyClient.objects.filter(pk=id)
    if request.method == 'POST':
        form = ClientFileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.file_owner_id = int(id)
            post.save()
            return HttpResponseRedirect('/snslaw/addfile/<id>?submitted=True')
    else:
        form = ClientFileForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'snslaw/addfile.html', {'form': form, 'submitted': submitted})


def show_clients(request):
    client_list = MyClient.objects.all().values()  # כל הרשומות

    template = loader.get_template('snslaw/show_clients.html')
    context = {
        'client_list': client_list,
    }
    return HttpResponse(template.render(context, request))


# def update(request, id):  # old update
#     myclient = MyClient.objects.get(id=id)
#     template = loader.get_template('snslaw/update.html')
#     context = {
#         'myclient': myclient,
#     }
#     return HttpResponse(template.render(context, request))

def update(request, id):
    myclient = get_object_or_404(MyClient, pk=id)
    if request.method == 'POST':
        form = MyclientForm(request.POST, instance=myclient)
        if form.is_valid():
            myclient.save()
            return redirect('snslaw/client_details.html', pk=myclient.id)
    else:
        form = MyclientForm(instance=myclient)
    return render(request, 'snslaw/update.html', {'form': form, 'myclient': myclient})


def client_detail(request, id):
    myclient = MyClient.objects.get(id=id)
    client_files = myclient.newtadfile_set.all()
    template = loader.get_template('snslaw/client_detail.html')
    if request.method == 'POST':
        a = request.POST['actions']
        if a == 'newffile':
            return render(request, "snslaw/newfile.html", {"id": id})

        else:
            pass
    else:
        context = {
            'myclient': myclient,
            'client_files': client_files,
        }
    return HttpResponse(template.render(context, request))


def delete_record(request, id):
    myclient = MyClient.objects.get(id=id)
    context = {
        'myclient': myclient,
    }
    myclient.delete()
    template = loader.get_template('snslaw/delete_record.html')

    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    clnt = MyClient.objects.get(id=id)
    clnt.first_name = request.POST['first']
    clnt.last_name = request.POST['last']
    clnt.id_number = request.POST['id_number']
    clnt.phone1_prefix = request.POST['phone1_prefix']
    clnt.phone1 = request.POST['phone1']
    clnt.phone2_prefix = request.POST['phone2_prefix']
    clnt.phone2 = request.POST['phone2']
    clnt.birth_date = request.POST['birth']
    print(type(request.POST['birth']), request.POST['birth'])
    # print(datetime.strptime(clnt.birth_date, "%d-%B-%Y"))
    # print(datetime.strptime(clnt.birth_date, "%x"))
    # clnt.birth_date = datetime.date(request.POST['birth'], "YYYY-MM-DD")
    # print(datetime.strptime(clnt.birth_date, "YYYY-MM-DD"))
    clnt.address_city = request.POST['city']
    clnt.address_number = request.POST['number']
    clnt.address_street = request.POST['street']
    clnt.address_pob = request.POST['pob']
    clnt.kupa = request.POST['kupa']
    clnt.mail = request.POST['mail']
    clnt.gender = request.POST['gender']
    clnt.address_zip = request.POST['zip']
    clnt.save()
    return HttpResponseRedirect('/snslaw/show_clients/?submitted=True')

#         title = 'History'
#
#         def init_with_context(self, context):
#             # request = context['request']
#             # # we use sessions to store the visited pages stack
#             # history = request.session.get('history', [])
#             history = MyClient.objects.all().values()
#             for item in history:
#                 self.children.append(MenuItem(
#                     title=item['title'],
#                     url=item['url']
#                 ))


def mytest(request):

    return render(request, "snslaw/mytest.html")


def tadfile(request, id):
    submitted = False
    # header = ClientFiles.objects.get(pk=2)
    # header = forms.ModelChoiceField(queryset=ClientFiles.objects.values('file_type'))
    # print(header, "ppppp")
    if request.method == 'POST':
        form = NewTadFileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # print(id, "id", header)
            post.file_owner_id = int(id)
            # post.file_header = header
            post.save()
            # form.save()
            # return HttpResponseRedirect('/snslaw/tadfile/id?submitted=True')
            return render(request, "snslaw/tadfile.html", {"id": id, "submitted":True})
    else:
        form = NewTadFileForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'snslaw/tadfile.html',
        {'form': form, 'submitted': submitted}
    )


def mytest1(request):

    # return HttpResponse('<h1>Page was found</h1>')  # החזרת קוד שגיאה
    # client_list = MyClient.objects.all().values()
    submitted = False
    # if request.method == 'POST':
    form = UserInfoForm(request.POST)
    if form.is_valid():
        # form.save()
        return HttpResponseRedirect('/snslaw/mytest1/?submitted=True')
    else:
        form = UserInfoForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request,
        'snslaw/mytest1.html',
        {'form': form, 'submitted':submitted}
    )