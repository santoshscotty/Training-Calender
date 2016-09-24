from django.shortcuts import render
from django.template import RequestContext
from tc.models import student,course,faculty

def Home(request):
	students=student.objects.all()
	courses=course.objects.all()
	qq=request.GET.get('r')
	if qq:
		students=students.filter(name__icontains=qq)
	rr=request.GET.get('q')
	if rr:
		courses=courses.filter(name__icontains=rr)
	return render(request,'home.html',{'students':students,'courses':courses})

def courseinfo(request,courseslug):
	cours=course.objects.get(slug=courseslug)
	return render(request,'courseinfo.html',{'course':cours})

def studentinfo(request,studentslug):
	stu=student.objects.get(slug=studentslug)
	return render(request,'studentinfo.html',{'student':stu})
