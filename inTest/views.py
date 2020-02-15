from django.shortcuts import render,HttpResponse
from inTest import models
# Create your views here.
def show(request):
    user_list = models.Mark.objects.order_by("mark")
    return render(request,"show.html",{'user_list':user_list})
def addNew(request):
    if request.method == "post":
        nameMark = request.POST.get('nameMark')
        newMark = request.POST.get('newMark')
        print(newMark)
        if models.Mark.objects.get(name=nameMark):
            mark0 = models.Mark.objects.get(name=nameMark)
            mark0.mark = newMark
            mark0.save()
            return render(request,"show.html")
        else:
            mark0 = models.Mark()
            name = mark0.name
            mark = mark0.mark
            mark0.is_active = True
            mark0.save()
            return render(request, "show.html")

