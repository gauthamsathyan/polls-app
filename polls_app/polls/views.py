from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Poll
from django.utils import timezone
import json

def index(request):
    return render(request, 'polls.html')

@csrf_exempt
def create_poll(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question', '')
        poll = Poll.objects.create(question=question, pub_date=timezone.now())
        return JsonResponse({'poll_id': poll.id}, status=201)  # Return the ID of the new poll
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)