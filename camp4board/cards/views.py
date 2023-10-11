from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm
from django.utils import timezone
from django.utils import timezone
from django.shortcuts import render
from .models import Card

def card_list(request):
    now = timezone.now()
    all_cards = Card.objects.all()
    non_expired = [card for card in all_cards if card.expiration_date >= now]
    return render(request, 'cards/card_list.html', {'cards': non_expired})

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form})
