from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_local_entered_at(self):
        return timezone.localtime(self.entered_at)

    def get_local_leaved_at(self):
        return timezone.localtime(self.leaved_at)

    def get_local_now(self):
        return timezone.now().replace(microsecond=0)

    def get_duration(self):
        if self.leaved_at:
            return self.get_local_leaved_at() - self.get_local_entered_at()
        return self.get_local_now() - self.get_local_entered_at()

    def is_long(self, limit=3600):
        return self.get_duration().total_seconds() > limit

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
