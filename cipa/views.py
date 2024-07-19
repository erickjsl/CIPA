from django.shortcuts import render, get_object_or_404
from .models import Membro, Reuniao

def membros_list(request):
    membros = Membro.objects.all()
    return render(request, 'cipa/membros_list.html', {'membros': membros})

def reunioes_list(request):
    reunioes = Reuniao.objects.all()
    return render(request, 'cipa/reunioes_list.html', {'reunioes': reunioes})

def membro_detail(request, pk):
    membro = get_object_or_404(Membro, pk=pk)
    return render(request, 'cipa/membro_detail.html', {'membro': membro})

def reuniao_detail(request, pk):
    reuniao = get_object_or_404(Reuniao, pk=pk)
    return render(request, 'cipa/reuniao_detail.html', {'reuniao': reuniao})
