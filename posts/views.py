from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

# FORM 
from .forms import PostForm

from datetime import datetime
# Create your views here.


posts = [

	{
		'name':'Blue Sky',
		'user':{'name':'Sergio furcio',
				'picture':'https://picsum.photos/60/60/?image=1005'},
		'timestamp':datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
		'picture':'https://picsum.photos/800/600?image=1036'
	},

	{
		'name':'Red Sky',
		'user':{'name':'Mariana_014',
				'picture':'https://picsum.photos/60/60/?image=1027'},
		'timestamp':datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
		'picture':'https://picsum.photos/800/800?image=903'
	},

	{
		'name':'Orange Sky.',
		'user':{'name':'julio_Vega',
				'picture':'https://picsum.photos/60/60/?image=883'},
		'timestamp':datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
		'picture':'https://picsum.photos/500/700?image=1076'
	},

	{
		'name':'Ocean.',
		'user':{'name':'fernada_12_nava',
				'picture':'https://picsum.photos/60/60/?image=1005'},
		'timestamp':datetime.now().strftime('%b %d, %Y - %H:%M hrs'),
		'picture':'https://picsum.photos/500/700?image=1076'
	}
]

@login_required
def lis_post(request): 
	content = {'posts':posts}

	return render(request, 'posts/feed.html',content)


@login_required
def new_post(request):

	if request.method == 'POST':
		# Se recibieron los datos del fomulario 
		print(request.POST)
		form = PostForm(request.POST,request.FILES)	

		if form.is_valid():
			# Los Datos son validos
			form.save()
			return redirect('feed')
	else:
		# No se esta recibiendo ningun dato del formulario
		form = PostForm()


	context = {	'form':form,
				'user':request.user}

	return render(request, 'posts/new_post.html',context)