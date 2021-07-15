from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    context = {
        "non_closed_visits": [{
            "passcode": visit.passcard.passcode,
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.get_local_entered_at(),
            "duration": visit.get_duration(),
            "is_strange": visit.is_long()
        } for visit in Visit.objects.filter(leaved_at=None)],
    }
    return render(request, 'storage_information.html', context)
