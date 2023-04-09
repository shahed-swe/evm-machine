from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Voter

# Create your views here.
@csrf_exempt
def vote(request):
    if request.method == 'POST':
        data = request.POST or json.loads(request.body)
        fingerprint_id = data.get('fingerprint_id')
        voter = Voter.objects.filter(fingerprint_id=int(fingerprint_id)).first()
        if voter is None:
            return JsonResponse({'success': False, 'error': 'Invalid fingerprint.'})
        elif voter.has_voted:
            return JsonResponse({'success': False, 'error': 'You have already voted.'})
        else:
            candidate_id = data.get('candidate_id', '')
            candidate = Candidate.objects.filter(id=candidate_id).first()
            if candidate is None:
                return JsonResponse({'success': False, 'error': 'Invalid candidate ID.'})
            vote = Vote(voter=voter, candidate=candidate)
            vote.save()
            voter.has_voted = True
            voter.save()
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method.'})

def home(request):
    return JsonResponse({'message': 'Server run successfully.'})

def candidates(request):
    candidates = Candidate.objects.annotate(num_votes=Count('vote'))
    candidates_list = []
    for candidate in candidates:
        candidate_dict = model_to_dict(candidate)
        candidate_dict['photo'] = candidate.photo.url
        candidate_dict['num_votes'] = candidate.num_votes
        candidates_list.append(candidate_dict)
    return JsonResponse(candidates_list, safe=False)


@csrf_exempt
def add_voter(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        fingerprint_id = request.POST.get('fingerprint_id', '')
        voter = Voter(name=name, fingerprint_id=fingerprint_id)
        voter.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})
