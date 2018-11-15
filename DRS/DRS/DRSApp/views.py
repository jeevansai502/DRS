from django.shortcuts import render
from django.views.generic import TemplateView


class RegisterPageView(TemplateView):
	def get(self,request):
		return render(request, 'register.html', context=None)