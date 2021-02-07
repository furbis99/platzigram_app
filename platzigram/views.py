from django.http import HttpResponse
import json 

def sorted_list(request):
	""" sorts a list received from the get method """

	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers) 

	return HttpResponse(str(sorted_ints), content_type='application/json')


def entry_authorization(request,nombre,edad):
	""" entry authorization permit """

	if (edad > 15):
		mensaje = f"Bienvenido(a) al sitio de platzigram {nombre}"
	else:
		mensaje = f"Este sitio solo es para mayores de 15 años."

	return HttpResponse(mensaje)