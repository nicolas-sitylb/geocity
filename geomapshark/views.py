from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from permits import forms, models


class CustomPasswordResetView(PasswordResetView):

    extra_email_context = {'custom_host': ''}

    def get_context_data(self, **kwargs):
        context = super(CustomPasswordResetView, self).get_context_data(**kwargs)
        domain = 'https://' + self.request.build_absolute_uri().split('//')[1].split('/')[0]
        self.extra_email_context['custom_host'] = domain
        self.extra_email_context['site_name'] = self.request.build_absolute_uri().split('/')[2]
        return context


def permit_author_create(request):
    djangouserform = forms.NewDjangoAuthUserForm(request.POST or None)
    permitauthorform = forms.GenericAuthorForm(request.POST or None)
    is_valid = djangouserform.is_valid() and permitauthorform.is_valid()

    if is_valid:
        new_user = djangouserform.save()
        permitauthorform.instance.user = new_user
        permitauthorform.save()

        login(request, new_user)
        if settings.ENABLE_2FA:
            return HttpResponseRedirect(
                reverse('two_factor:profile'))
        return HttpResponseRedirect(
            reverse('permits:permit_requests_list'))

    return render(
        request,
        'permits/permit_request_author.html',
        {
            'permitauthorform': permitauthorform,
            'djangouserform': djangouserform
        }
    )


@login_required
def permit_author_edit(request):

    djangouserform = forms.DjangoAuthUserForm(request.POST or None, instance=request.user)
    # prvent a crash when admin accesses this page
    permitauthorform = None
    if hasattr(request.user, 'permitauthor'):
        permit_author_instance = get_object_or_404(models.PermitAuthor, pk=request.user.permitauthor.pk)
        permitauthorform = forms.GenericAuthorForm(request.POST or None, instance=permit_author_instance)

    if djangouserform.is_valid() and permitauthorform and permitauthorform.is_valid():
        user = djangouserform.save()
        permitauthorform.instance.user = user
        permitauthorform.save()

        return HttpResponseRedirect(
            reverse('permits:permit_requests_list'))

    return render(
        request,
        'permits/permit_request_author.html',
        {
            'permitauthorform': permitauthorform,
            'djangouserform': djangouserform
        }
    )
