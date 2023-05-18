from audioop import avg
from telnetlib import STATUS
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg
from .models import *
from datetime import date
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, 'index.html')


def associate(request):
    if request.method == 'POST':
        name = request.POST['name']
        addr = request.POST['address']
        head = request.POST['assochead']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['pass']
        if username == '':
            messages.info(request, "please enter the username")
            return redirect("associate")

        elif password == '':
            messages.info(request, "please enter the password")
            return redirect("associate")

        elif name == '':
            messages.info(request, "please enter the name")
            return redirect("associate")
        else:
            if Login.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect("associate")
            elif Association.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect("associate")
            else:
                login = Login.objects.create(
                    username=username, password=password, types='associate', status='0')
                user = Association.objects.create(
                    name=name, addr=addr, assochead=head, email=email, phno=phone, username=username, logid=login)
                user.save()
                login.save()
                msg = "Successfully Registered"
                print('Registered')
                return redirect("login")
                return render(request, 'associateRegister.html', {"msg": msg})
    else:
        return render(request, 'associateRegister.html')


def photographer(request):
    assoc = Association.objects.filter(logid__status__contains="1")
    if request.method == "POST" and request.FILES['myfile']:
        print(1)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        name = request.POST['name']
        addr = request.POST['address']
        gender = request.POST['gender']
        district = request.POST['district']
        special = request.POST['special']
        email = request.POST['email']
        phone = request.POST['phone']
        img = url
        assoc = request.POST['assoc']
        username = request.POST['username']
        insta = request.POST['insta']
        fb = request.POST['fb']
        profile = request.FILES['profile']
        password = request.POST['pass']

        if Login.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect("photographer")
        elif Photographer.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect("photographer")
        else:
            login = Login.objects.create(
                username=username, password=password, types='photographer', status='0')
            user = Photographer.objects.create(name=name, addr=addr, gender=gender, district=district, specialization=special,
                                               email=email, phone=phone, image=img, association1=assoc, logid=login, insta=insta, fb=fb, profile=profile)
            user.save()
            login.save()
            msg = "Successfully Registered"
            print('Registered')
            return redirect("login")
    else:
        return render(request, 'photographerRegister.html', {'assoc': assoc})


def user(request):
    if request.method == 'POST':
        name = request.POST['name']
        addr = request.POST['address']
        gender = request.POST['gender']
        district = request.POST['district']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['pass']

        if Login.objects.filter(username=username).exists():
            messages.info(request, "username taken")
            return redirect("user")
        elif Customer.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect("user")
        else:
            login = Login.objects.create(
                username=username, password=password, types='user', status='0')
            user = Customer.objects.create(
                name=name, addr=addr, gender=gender, district=district, email=email, phone=phone, logid=login)
            user.save()
            login.save()
            msg = "Successfully Registered"
            print('Registered')
            return redirect("login")
    else:
        return render(request, 'user.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        if Login.objects.filter(username=username, password=password).exists():
            login = Login.objects.get(username=username, password=password)
            print(login.types)
            if login.status == '1':
                if login is not None:
                    if login.types == 'admin':
                        messages.info(
                            request, "Successfully Logged in by user")
                        return redirect('adminHome')
                    elif login.types == 'associate':
                        aid = Association.objects.get(logid=login.id)
                        print("hhhhhhhhh", aid.id)
                        request.session['aid'] = aid.id
                        msg = "Successfully Login"
                        return redirect('associateHome')
                    elif login.types == 'photographer':
                        pid = Photographer.objects.get(logid=login.id)
                        request.session['pid'] = pid.id
                        msg = "Successfully Login"
                        return redirect('photographerHome')
                    else:
                        cid = Customer.objects.get(logid=login.id)
                        request.session['cid'] = cid.id
                        messages.info(
                            request, "Successfully Logged in by user")
                        msg = "Successfully Login"
                        return redirect('userHome')
                else:
                    return redirect('login')
            else:
                msg = "Admin not Approved"
                return render(request, 'login.html', {'msg': msg})
        else:
            messages.info(request, "Invalid username or password")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def adminHome(request):
    return render(request, 'adminHome.html')


def photographerHome(request):
    return render(request, 'photographerHome.html')


def userHome(request):
    return render(request, 'userHome.html')


def approval(request):
    return render(request, 'approval.html')


def associateHome(request):
    return render(request, 'associateHome.html')


def usprofile(request):
    id = request.session['cid']
    user = Customer.objects.get(id=id)
    return render(request, 'usprofile.html', {'user': user})


def viewuserphotographers(request):
    graphers = Photographer.objects.filter(logid__status__contains="1")
    return render(request, 'viewuserphotographers.html', {'graphers': graphers})


def customerreview(request):
    msg = ''
    pid = request.GET.get("id")
    cid = request.session['cid']
    photo = Photographer.objects.get(id=pid)
    cust = Customer.objects.get(id=cid)
    if request.method == 'POST':
        rating = request.POST['rating']
        feedback = request.POST['feed']
        s = review.objects.create(
            phid=photo, cid=cust, rating=rating, feedback=feedback)
        s.save()
        msg = 'Rated Successfully'
    return render(request, 'customerreview.html', {'msg': msg})


def viewphotographers(request):
    graphers = Photographer.objects.filter(logid__status__contains="1")
    print(graphers)
    return render(request, 'viewphotographers.html', {'graphers': graphers})


def awards(request):
    msg = ''
    aid = request.session['aid']
    assoc = Association.objects.get(id=aid)
    grapher = Photographer.objects.filter(logid__status__contains="1")

    if request.method == 'POST':
        award = request.POST['award']
        assos = request.POST['assoc']
        graph = request.POST['grapher']
        date = request.POST['date']
        desc = request.POST['desc']
        award = Award.objects.create(
            award=award, assocname=assos, pname=graph, desc=desc, date=date)
        award.save()
        msg = "Successfully Added"
    return render(request, 'awards.html', {'assoc': assoc, 'grapher': grapher, "msg": msg})


def feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedback': feedback})


def complaint(request):
    return render(request, 'complaint.html')


def rating(request):
    return render(request, 'rating.html')


def context(request):
    msg = ''
    aid = request.session['aid']
    assoc = Association.objects.get(id=aid)
    if request.method == 'POST':
        event = request.POST['event']
        assos = request.POST['assoc']
        loc = request.POST['loc']
        date = request.POST['date']
        desc = request.POST['desc']
        notification = Notification.objects.create(
            event=event, assocname=assos, loc=loc, desc=desc, date=date)
        notification.save()
        msg = "Successfully Added"
    return render(request, 'context.html', {'assoc': assoc, "msg": msg})


def phprofile(request):
    id = request.session['pid']
    graphers = Photographer.objects.get(id=id)
    print(graphers)
    return render(request, 'phprofile.html', {'graphers': graphers})


def editprofile(request):
    id = request.GET.get('id')
    graphers = Photographer.objects.get(id=id)
    url = graphers.image
    assoc = Association.objects.filter(logid__status__contains="1")
    if request.method == "POST":
        print(1)
        if request.FILES:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
        name = request.POST['name']
        addr = request.POST['address']
        district = request.POST['district']
        special = request.POST['special']
        email = request.POST['email']
        phone = request.POST['phone']
        img = url
        assoc = request.POST['assoc']
        user = Photographer.objects.filter(id=id).update(
            name=name, addr=addr, district=district, specialization=special, email=email, phone=phone, image=img, association1=assoc)
        return redirect('phprofile')
    return render(request, 'editprofile.html', {'graphers': graphers, 'assoc': assoc})


def edituserprofile(request):
    id = request.GET.get('id')
    user = Customer.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        addr = request.POST['address']
        district = request.POST['district']
        email = request.POST['email']
        phone = request.POST['phone']
        user = Customer.objects.filter(id=id).update(
            name=name, addr=addr, district=district, email=email, phone=phone)
        return redirect('usprofile')
    return render(request, 'edituserprofile.html', {'user': user})


def specification(request):
    msg = ''
    id = request.session['pid']
    photo = Photographer.objects.get(id=id)
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        camera = request.POST['camera']
        cmodel = request.POST['cmodel']
        desc = request.POST['desc']
        img = url
        spec = Specification.objects.create(
            camera=camera, cmodel=cmodel, image=img, desc=desc, phid=photo)
        spec.save()
        msg = "Successfully Added"
    return render(request, 'specification.html', {'msg': msg})


def arts(request):
    msg = ''
    id = request.session['pid']
    photo = Photographer.objects.get(id=id)
    images = Artgallery.objects.filter(phid=id)
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        caption = request.POST['caption']
        amount = request.POST['amount']
        img = url
        upim = Artgallery.objects.create(
            caption=caption, amount=amount, image=img, phid=photo)
        upim.save()
        msg = "Successfully Added"
    return render(request, 'arts.html', {'msg': msg, 'images': images})


def sales(request):
    msg = ''
    id = request.session['pid']
    photo = Photographer.objects.get(id=id)
    images = Giftgallery.objects.filter(phid=id)
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        caption = request.POST['caption']
        amount = request.POST['amount']
        img = url
        upim = Giftgallery.objects.create(
            caption=caption, amount=amount, image=img, phid=photo)
        upim.save()
        msg = "Successfully Added"
    return render(request, 'sales.html', {'msg': msg, 'images': images})


def imageupload(request):
    msg = ''
    id = request.session['pid']
    photo = Photographer.objects.get(id=id)
    images = Photographerimage.objects.filter(phid=id)
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        caption = request.POST['caption']
        img = url
        upim = Photographerimage.objects.create(
            caption=caption, image=img, phid=photo)
        upim.save()
        msg = "Successfully Added"
    return render(request, 'imageupload.html', {'msg': msg, 'images': images})


def videoupload(request):
    msg = ''
    id = request.session['pid']
    photo = Photographer.objects.get(id=id)
    images = Photographervideo.objects.filter(phid=id)
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        caption = request.POST['caption']
        link = url
        upvd = Photographervideo.objects.create(
            caption=caption, link=link, phid=photo)
        upvd.save()
        msg = "Successfully Added"
    return render(request, 'videoupload.html', {'msg': msg, 'images': images})


def addfeedback(request):
    msg = ''
    cid = request.session['cid']
    cust = Customer.objects.get(id=cid)
    if request.method == 'POST':
        feed = request.POST['feed']
        feedback = Feedback.objects.create(cid=cust, feedback=feed)
        feedback.save()
        msg = 'Feedback Added Successfully'
    return render(request, 'addfeedback.html', {'msg': msg})


def workstatus(request):
    msg = ''
    id = request.GET.get('id')
    pid = request.session['pid']
    photo = Photographer.objects.get(id=pid)
    if request.method == "POST" and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        caption = request.POST['caption']
        date = request.POST['date']
        desc = request.POST['desc']
        status = request.POST['status']
        link = url
        wrkstatus = Workstatus.objects.filter(bkid=id).update(
            caption=caption, link=link, date=date, desc=desc, phid=photo)
        book = Booking.objects.filter(id=id).update(status=status)
        msg = "Successfully Added"
    return render(request, 'workstatus.html', {'msg': msg})


def viewfests(request):
    fests = Notification.objects.all()
    return render(request, 'viewfests.html', {'fests': fests})


def viewarts(request):
    arts = Artgallery.objects.all()
    return render(request, 'viewarts.html', {'arts': arts})


def payment(request):
    id = request.GET.get('id')
    cid = request.session['cid']
    art = Artgallery.objects.get(id=id)
    cust = Customer.objects.get(id=cid)
    return render(request, 'payment.html', {'art': art, 'cust': cust})


def salepayment(request):
    id = request.GET.get('id')
    cid = request.session['cid']
    art = Giftgallery.objects.get(id=id)
    cust = Customer.objects.get(id=cid)
    return render(request, 'salepayment.html', {'art': art, 'cust': cust})


def payinterface(request):
    msg = ''
    id = request.GET.get('id')
    cid = request.session['cid']
    art = Artgallery.objects.get(id=id)
    photo = Photographer.objects.get(id=art.phid.id)
    cust = Customer.objects.get(id=cid)
    if request.method == "POST":
        payment = Payment.objects.create(
            amount=art.amount, custid=cust, phid=photo)
        purchase = purchased.objects.create(
            pmid=payment, artid=art, phid=photo)
        payment.save()
        purchase.save()
        msg = 'Paid Successfully'
    return render(request, 'payinterface.html', {'art': art, 'cust': cust, 'msg': msg})


def salepayinterface(request):
    msg = ''
    id = request.GET.get('id')
    cid = request.session['cid']
    art = Giftgallery.objects.get(id=id)
    photo = Photographer.objects.get(id=art.phid.id)
    cust = Customer.objects.get(id=cid)
    if request.method == "POST":
        payment = Payment.objects.create(
            amount=art.amount, custid=cust, phid=photo)
        purchase = purchased.objects.create(
            pmid=payment, saleid=art, phid=photo)
        payment.save()
        purchase.save()
        msg = 'Paid Successfully'
    return render(request, 'salepayinterface.html', {'art': art, 'cust': cust, 'msg': msg})


def purchase(request):
    id = request.session['pid']
    pur = purchased.objects.filter(phid=id)
    return render(request, 'purchase.html', {'pur': pur})


def viewsales(request):
    sales = Giftgallery.objects.all()
    return render(request, 'viewsales.html', {'sales': sales})


def commited(request):
    pid = request.session['pid']
    bookings = Booking.objects.filter(phid=pid, status='commited')
    return render(request, 'commited.html', {'book': bookings})


def viewdetails(request):
    id = request.GET.get('id')
    graphers = Photographer.objects.get(id=id)
    specify = Specification.objects.filter(phid=id)
    rate = review.objects.filter(phid=id).aggregate(avg1=Avg('rating'))
    d = rate['avg1']
    print(d)
    return render(request, 'viewdetails.html', {'graphers': graphers, 'specify': specify, 'd': d})


def viewbooking(request):
    pid = request.session['pid']
    bookings = Booking.objects.filter(phid=pid, status=None)
    return render(request, 'viewbooking.html', {'book': bookings})


def committ(request):
    msg = ''
    pid = request.session['pid']
    photo = Photographer.objects.get(id=pid)
    id = request.GET.get('id')
    book = Booking.objects.get(id=id)
    if request.method == 'POST':
        amount = request.POST['amount']
        Booking.objects.filter(id=id).update(tamount=amount, status='commited')
        wrkstatus = Workstatus.objects.create(phid=photo, bkid=book)
        wrkstatus.save()
        msg = 'commited'
        return redirect("photographerHome")
    return render(request, 'commit.html', {'msg': msg})


def addbooking(request):
    msg = ''
    id = request.GET.get('id')
    cid = request.session['cid']
    cust = Customer.objects.get(id=cid)
    graphers = Photographer.objects.get(id=id)
    dt = date.today()
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        days = request.POST['days']
        loc = request.POST['loc']
        desc = request.POST['desc']
        fdt = datetime.strptime(fromdate, '%Y-%m-%d')
        tdt = datetime.strptime(todate, '%Y-%m-%d')
        # if (dt<fdt.date()) or (dt<tdt.date()):
        #     msg='Inavalid Date'
        #     return redirect("/viewuserphotographers")
        booking = Booking.objects.create(
            phid=graphers, fromdate=fromdate, todate=todate, days=days, location=loc, description=desc, cid=cust)
        booking.save()
        msg = 'Booking Request Send'
    return render(request, 'addbooking.html', {'graphers': graphers, 'msg': msg})


def addcomplaint(request):
    return render(request, 'addcomplaint.html')


def approvegrapher(request):
    aprgrapher = Photographer.objects.filter(logid__status__contains="0")
    return render(request, 'approvegrapher.html', {'phuser': aprgrapher})


def approveassociation(request):
    aprassoc = Association.objects.filter(logid__status__contains="0")
    return render(request, 'approveassociation.html', {'asuser': aprassoc})


def viewbookstatus(request):
    cid = request.session['cid']
    bookings = Booking.objects.filter(cid=cid).exclude(status='cancel')
    return render(request, 'viewbookstatus.html', {'book': bookings})


def viewwrkstatus(request):
    id = request.GET.get('id')
    status = Workstatus.objects.filter(bkid=id)
    return render(request, 'viewwrkstatus.html', {'status': status})


def approveuser(request):
    apruser = Customer.objects.filter(logid__status__contains="0")
    return render(request, 'approveuser.html', {'user': apruser})


def approve(request):
    id = request.GET.get("id")
    users = request.GET.get("user")
    print('--------------------------------------------')
    print(users)
    print('--------------------------------------------')
    user = Login.objects.filter(id=id).update(status='1')
    if users == 'user':
        return redirect('/approveuser')
    elif users == 'photographer':
        return redirect('/approvegrapher')
    elif users == 'association':
        return redirect('/approveassociation')

    return redirect('adminHome')


def cancel(request):
    id = request.GET.get('id')
    Booking.objects.filter(id=id).update(status='cancel')
    return redirect('viewbookstatus')


def forTemplate(request):
    pid = request.session['pid']
    if request.POST:
        caption = request.POST['caption']
        cust = request.POST['assoc']
        images = request.FILES.getlist('images')
        ph = Photographer.objects.get(id=pid)
        cid = Customer.objects.get(id=cust)
        ft = ForAlbum.objects.create(phid=ph, cid=cid, caption=caption)
        ft.save()
        for image in images:
            ai = AlbumImages.objects.create(fa=ft, images=image)
            ai.save()

    custs = Customer.objects.all()
    datas = ForAlbum.objects.filter(phid__id=pid).order_by("-id")
    return render(request, "forTemplate.html", {"custs": custs, "datas": datas})


def templates(request):
    id = request.GET['id']
    datas = ForAlbum.objects.get(id=id)
    data = AlbumImages.objects.filter(fa__id=id)
    return render(request, "template.html", {"data": data, "datas": datas})


def viewAlbum(request):
    cid = request.session['cid']

    datas = ForAlbum.objects.filter(cid__id=cid).order_by("-id")
    return render(request, "viewAlbum.html", {"datas": datas})
