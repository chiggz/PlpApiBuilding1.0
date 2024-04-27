import requests
import re
from django.shortcuts import render


def home(request):
  #USING APIS.
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[1]["id"]

  # Example 2
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]
  match = re.search(r'breeds/([^/]+)/', result2)
  breed_name = None
  if match:
    breed_name = match.group(1)
    print(breed_name)
  else:
    print("No match found")
  # Example 3
  respon3 = requests.get('https://api.thecatapi.com/v1/images/search')
  data3 = respon3.json()
  result3 = data3[0]["url"]
  return render(request, 'templates/index.html', {'result': result, 'result2': result2, 'breed_name': breed_name, 'result3': result3})
