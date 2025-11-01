import requests
from django.http import JsonResponse


def get_access_token(request):
    consumer_key = 'MPESA_CONSUMER_KEY'
    consumer_secret = 'MPESA_CONSUMER_SECRET'
    acces_token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    auth = (consumer_key, consumer_secret)

    try:
        response = requests.get(acces_token_url, auth=auth)
        response.raise_for_status()
        result = response.json()
        # print(result)
        access_token = result['access_token']
        return JsonResponse({'access_token': access_token})
    except requests.exceptions.RequestException as error:
        return JsonResponse({'error': str(error)})
