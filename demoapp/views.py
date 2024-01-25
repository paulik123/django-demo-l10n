from django.shortcuts import render, redirect
from demoapp.models import Demo
from demoapp.forms import DemoForm
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):

	context = {
		"demos": Demo.objects.all(),
		"form": DemoForm()
	}

	return render(request, 'demoapp/index.html', context)

@require_http_methods(['POST'])
def add_demo(request):
	form = DemoForm(request.POST)

	if form.is_valid():
		form.save()
	else:
		messages.error(request, "Form error")

	return redirect('index')
	

def edit_demo(request, pk):
	demo = get_object_or_404(Demo, pk=pk)

	form = DemoForm(instance=demo)

	context = {
		"demos": Demo.objects.all(),
		"form": form
	}

	return render(request, 'demoapp/edit.html', context)