from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from .forms import CardForm, CommentForm
from django.shortcuts import render
from .models import Card, Comment
GOAL =100

def card_list(request):
    all_cards = Card.objects.all()
    count_of_cards = len(all_cards)
    non_expired = sorted([card for card in all_cards if not card.is_expired], key=lambda x: x.create_date, reverse=True)
    for card in non_expired:
        card.comments = Comment.objects.filter(card=card)
    return render(request, 'cards/card_list.html', {'cards': non_expired,  'percentage': (count_of_cards/GOAL)*100, 'total_posts': count_of_cards, 'goal':GOAL})

def add_card(request):

    all_cards = Card.objects.all()
    count_of_cards = len(all_cards)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'cards/add_card.html', {'form': form, 'errors':form.errors})

    form = CardForm()
    return render(request, 'cards/add_card.html', {'form': form, 'goal':GOAL,'percentage': (count_of_cards/GOAL)*100, 'total_posts': count_of_cards})

def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    comments = Comment.objects.filter(card=card)
    comment_form = CommentForm()

    all_cards = Card.objects.all()
    count_of_cards = len(all_cards)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.card = card
            new_comment.save()
            return redirect('card_detail', card_id=card_id)

    return render(request, 'cards/card_detail.html', {'card': card, 'comments': comments, 'comment_form': comment_form,  'percentage': (count_of_cards/GOAL)*100, 'total_posts': count_of_cards, 'goal':GOAL})
