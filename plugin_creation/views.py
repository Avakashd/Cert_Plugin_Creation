from django.shortcuts import render
from plugin_latest import main1
from django.template import loader

from django.http import HttpResponse


def create_plugin(request):
	return render(request,'create_plugin.html')

def plugin(request):
	if request.method == "POST":
		old_plugin = request.POST.get('old_plugin_name')
		newPlugin = request.POST.get('new_plugin_name')
		oldESXver = request.POST.get('old_esx_version')
		newESXVer = request.POST.get('new_esx_version')
		oldWorkbenchVer = request.POST.get('old_wb_version')
		newWorkbenchVer = request.POST.get('new_wb_version')
		path = request.POST.get('path')
		print(old_plugin,newPlugin,path)
		main1(old_plugin,newPlugin,oldESXver,newESXVer,oldWorkbenchVer,newWorkbenchVer,path)
	return render(request, 'plugin.html')