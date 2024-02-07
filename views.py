from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'orders/client_form.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'orders/client_list.html', {'clients': clients})

def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'orders/client_form.html', {'form': form})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'orders/client_confirm_delete.html', {'client': client})