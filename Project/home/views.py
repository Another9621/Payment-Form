from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
def index(request):
    params={}
    var=""
    try:
        if(request.method=='POST'):
            name=request.POST.get('name')
            gender=request.POST.get('gender')
            address=request.POST.get('address')
            email=request.POST.get('email')
            pincode=request.POST.get('pincode')
            mobi=request.POST.get('mobile')
            amnit=request.POST.get('amnt')
            cardtype=request.POST.get('card type')
            cardnumber=request.POST.get('card number')
            cvv=request.POST.get('cvv')
            vt=request.POST.get('validity')
            params={'Name':name,'Gender':gender,'Address':address,'Email':email,'Pincode':pincode,'Mob':mobi,'Amt':amnit,'cdn':cardnumber,'Vt':vt,'Card type':cardtype}
            
            url='/home/confirm?output={}'.format(params)
            pl=len(pincode)
            pn=len(cardnumber)
            if(pl!=6):
                raise forms.ValidationError('Invalid Pincode')
            if(pn!=16):
                raise forms.ValidationError('Invalid card number')
            return HttpResponseRedirect(url)
            
    except Exception as e:
            var='Invalid Pincode'
            var1='Invalid card number'
            return render(request,'home/paymentform.html',{'var':var,'var1':var1})
            print("e",e)
   
    
    return render(request,'home/paymentform.html',params)
# Create your views here.

def conf(request):
    data={}
    if request.method=="GET":
        output=request.GET.get('output')
    res2=eval(output)
    #res2=json.loads(res)
    data={
        'name1':res2['Name'],
        'gender1':res2['Gender'],
        'add1':res2['Address'],
        'em':res2['Email'],
        'pin':res2['Pincode'],
        'mob':res2['Mob'],
        'amt':res2['Amt'],
        'ct':res2['Card type'],
        'cn':res2['cdn'],
        'vt':res2['Vt'],

    }
    print(type(res2))
    print(data)
    return render(request,'home/confirm.html',data)
def otp(request):
    return render(request,'home/otp.html')
def tq(request):
    return render(request,'home/tanq.html')