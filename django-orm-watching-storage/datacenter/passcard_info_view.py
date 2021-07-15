from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404, render


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    context = {
        "passcard": passcard,
        "this_passcard_visits": [{
            "entered_at": visit.get_local_entered_at(),
            "duration": visit.get_duration(),
            "is_strange": visit.is_long()
        } for visit in Visit.objects.filter(passcard=passcard)],
    }
    return render(request, 'passcard_info.html', context)
