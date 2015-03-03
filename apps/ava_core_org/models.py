from django.db import models
from django.core.urlresolvers import reverse

from apps.ava_core.models import TimeStampedModel
from apps.ava_core_identity.models import Identifier


class Organisation (TimeStampedModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
        return reverse('org-detail',kwargs={'pk': self.pk})


class OrganisationGroup (TimeStampedModel):
    '''
    A group of identities that exists within an organisation.
    '''

    AD = 'AD'
    SOCIAL = 'SO'
    PROJECT = 'PR'
    WORKING = 'WG'
    TEAM = 'TE'

    GROUP_TYPE_CHOICES = (
        (AD,      'Active Directory'),
        (SOCIAL,  'Social Group'),
        (PROJECT, 'Project'),
        (WORKING, 'Working Group'),
        (TEAM,    'Team'),
    )

    name = models.CharField(max_length=100)
    grouptype = models.CharField(max_length=7,
                                 choices=GROUP_TYPE_CHOICES,
                                 default=AD,
                                 verbose_name='Group Type')
    organisation = models.ForeignKey('Organisation', null=False)

    def __unicode__(self):
        return self.name or u''

    def get_absolute_url(self):
        return reverse('org-group-detail',kwargs={'pk': self.pk})


class GroupIdentifier(TimeStampedModel):
    group = models.ForeignKey(OrganisationGroup, null=False)
    identifier = models.ForeignKey(Identifier, null=False)

    def __unicode__(self):
        return self.group.name +" -> " + self.identifier.identifier

    def get_absolute_url(self):
        return reverse('group-detail',kwargs={'pk': self.pk})

    class Meta:
        unique_together = ("identifier", "group")
