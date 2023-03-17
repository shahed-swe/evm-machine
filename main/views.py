from django.shortcuts import render
from .models import *

# Create your views here.
def vote(request):
    if request.method == 'POST':
        fingerprint_id = request.POST.get('fingerprint_id', '')
        voter = Voter.objects.filter(fingerprint_id=fingerprint_id).first()
        if voter is None:
            return JsonResponse({'success': False, 'error': 'Invalid fingerprint.'})
        elif voter.has_voted:
            return JsonResponse({'success': False, 'error': 'You have already voted.'})
        else:
            candidate_id = request.POST.get('candidate_id', '')
            candidate = Candidate.objects.filter(id=candidate_id).first()
            if candidate is None:
                return JsonResponse({'success': False, 'error': 'Invalid candidate ID.'})
            vote = Vote(voter=voter, candidate=candidate)
            vote.save()
            voter.has_voted = True
            voter.save()
            return JsonResponse({'success': True})

def home(request):
    return render(request, 'home.html')

def candidates(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates.html', {'candidates': candidates})