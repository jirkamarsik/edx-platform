"""
LTI Provider API endpoint urls.
"""

from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url(r'^courses/{}/(?P<usage_id>[^/]*)$'.format(settings.COURSE_ID_PATTERN),
        'lti_provider.views.lti_launch', name="lti_provider_launch"),
    url(r'^lti_run$', 'lti_provider.views.lti_run', name="lti_provider_run"),
)
