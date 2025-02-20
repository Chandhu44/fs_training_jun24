from django.shortcuts import render, redirect,get_object_or_404
from .models import Vendor 
# Create your views here.
def vendors_list(req):
    vendors = Vendor.objects.all()
    return render(req,'vendors-list.html',{'vendors':vendors})

def vendors_create(req):
    if req.method == "POST":
        vendor = Vendor()
        vendor.name = req.POST['name'] 
        vendor.ratings = req.POST['ratings'] 
        vendor.place = req.POST['place'] 
        vendor.phone_number = req.POST['phone_number'] 
        vendor.save()
        return redirect("/")
        
    return render(req, 'vendors-create.html')

def vendors_edit(req, id):
    vendor = get_object_or_404(Vendor,pk=id)
    if req.method == "POST":
        name = req.POST['name']
        vendor.name = name 
        vendor.ratings = req.POST['ratings'] 
        vendor.place = req.POST['place'] 
        vendor.phone_number = req.POST['phone_number'] 
        vendor.save()
        return redirect("/")        

    return render(req, 'vendors-edit.html',{'vendor':vendor})
