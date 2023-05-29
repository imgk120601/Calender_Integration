 

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from google_auth_oauthlib.flow import Flow

from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View
from google.oauth2 import credentials
from django.conf import settings

from googleapiclient.discovery import build

def home(request):
    return HttpResponse("Hello, Django!")

'''

class GoogleCalendarInitView(View):
    def get(self, request):
        flow = Flow.from_client_secrets_file(
            request.settings.GOOGLE_CLIENT_SECRETS_JSON,
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        )
        flow.redirect_uri = request.build_absolute_uri('/rest/v1/calendar/redirect/')

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
        )
        request.session['oauth_state'] = state

        return JsonResponse({'authorization_url': authorization_url})


class GoogleCalendarRedirectView(View):
    def get(self, request):
        state = request.GET.get('state')
        if state != request.session.get('oauth_state'):
            return HttpResponseBadRequest('Invalid state parameter.')

        flow = Flow.from_client_secrets_file(
            request.settings.GOOGLE_CLIENT_SECRETS_JSON,
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        )
        flow.redirect_uri = request.build_absolute_uri('/rest/v1/calendar/redirect/')

        try:
            flow.fetch_token(authorization_response=request.get_full_path())
        except Exception as e:
            return HttpResponseBadRequest(f'Failed to fetch token: {e}')

        credentials = flow.credentials

        service = build('calendar', 'v3', credentials=credentials)

        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        # Process and return the events as desired

        return JsonResponse({'events': events})


'''
# View for initiating OAuth flow
def GoogleCalendarInitView(request):
    flow = Flow.from_client_secrets_file(
        'C:\\Users\\imgk1\\Desktop\\online learning\\django_convin_intern\\client_secret.json'
,
        scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        redirect_uri=request.build_absolute_uri(reverse('calendar_integration:redirect')),
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
    )
    request.session['state'] = state
    return HttpResponseRedirect(authorization_url)

# View for handling redirect from Google
def GoogleCalendarRedirectView(request):
    state = request.session.pop('state', '')
    flow = Flow.from_client_secrets_file(
        'C:\\Users\\imgk1\\Desktop\\online learning\\django_convin_intern\\client_secret.json'
,
        scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        state=state,
      #redirect_uri = request.build_absolute_uri(reverse('calendar_integration:redirect'))
      redirect_uri=request.build_absolute_uri(reverse('calendar_integration:redirect')).replace('http://', 'https://')


    )
    flow.fetch_token(
        authorization_response=request.build_absolute_uri(),
    )
    credentials = flow.credentials
    # Use the credentials to make API requests to the user's calendar
    # Fetch the list of events and process them as needed
    # ...
    service = build('calendar', 'v3', credentials=credentials)

    events_result = service.events().list(calendarId='primary', maxResults=10).execute()
    events = events_result.get('items', [])

    # Process and return the events as desired

    return JsonResponse({'events': events})
    
    #return render(request, 'redirect.html')

