from django.shortcuts import render
from .models import Client
from commande.filters import CommandeFiltre
from django.contrib.auth.decorators import login_required


@login_required(login_url='acces')
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commandes = client.commande_set.all()
    commande_total = commandes.count()
    my_filter = CommandeFiltre(request.GET, queryset=commandes)  # Relier notre filtre à notre vue
    commandes = my_filter.qs

    context = {'client': client, 'commandes': commandes, 'commande_total': commande_total, 'my_filter': my_filter}
    return render(request, 'client/list_client.html', context)
