from django.shortcuts import render, get_object_or_404, redirect
from .models import SwapUser,request_swap
from django.contrib.auth.decorators import login_required

@login_required
def send_request(request, username):
    receiver = get_object_or_404(SwapUser, username=username)
    sender = request.user

    if request.method == 'POST':
        message = request.POST['message']
        skill_offered = sender.skills  # from sender
        skill_wanted = receiver.skills  # from receiver

        request_swap.objects.create(
            sender=sender,
            receiver=receiver,
            skill_offered=skill_offered,
            skill_learn=skill_wanted,
            message=message
        )

        return redirect('home')  # or a success page

    return render(request, 'send_request.html', {
        'receiver': receiver,
        'sender': sender
    })


@login_required
def my_requests(request):
    requests = request_swap.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'myrequests.html', {'requests': requests})

@login_required
def handle_request(request, request_id):
    swap_request = get_object_or_404(request_swap, id=request_id, receiver=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')
        suggestion = request.POST.get('suggestion')

        if action in ['Accepted', 'Rejected']:
            swap_request.status = action
            swap_request.message += f"\n\nReceiver's note: {suggestion}"
            swap_request.save()

    return redirect('my_requests')





