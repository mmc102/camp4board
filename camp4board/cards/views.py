from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm
from datetime import datetime 

def card_list(request):
    now = datetime.now()
    non_expired_cards = Card.objects.filter(expiration_date__gte=now)
    return render(request, 'cards/card_list.html', {'cards': non_expired_cards})

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('card_list')  # Replace 'card_list' with the name of your card list view
    else:
        form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})
