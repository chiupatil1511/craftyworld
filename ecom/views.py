from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render
import pyrebase
import random
import string
import json
import urllib.request
from django.shortcuts import redirect
from datetime import date
import razorpay
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

#rule:
# // {
# //   "rules": {
# //     ".read": "now < 1627842600000",  // 2021-8-2
# //     ".write": "now < 1627842600000",  // 2021-8-2
# //   }
# // }
# {
role = "con"
firebaseConfig = {
    'apiKey': "AIzaSyAHoAW5WGu3ArXRbAQWZNYW8yz_Wrd8lkw",
    'authDomain': "db-crafty.firebaseapp.com",
    'databaseURL': "https://db-crafty-default-rtdb.firebaseio.com",
    'projectId': "db-crafty",
    'storageBucket': "db-crafty.appspot.com",
    'messagingSenderId': "68963004171",
    'appId': "1:68963004171:web:1bf82d5407b0dbe2f1bc0e",
    'measurementId': "G-C4B4TMPYMS"
  }
firebase1 = pyrebase.initialize_app(firebaseConfig)
authe = firebase1.auth()
database = firebase1.database()

def index(request):
    global curuser
    curuser = authe.current_user
    # id = database.child('Added_Items').shallow().get().val()
    # lis_id = []
    # for i in id:
    #     lis_id.append(i)
    # details = {}
    # # city = {}
    # for i in lis_id:
    #     det = database.child('Added_Items').child(i).get().val()
    #     sellid = database.child('Added_Items').child(i).child('sellid').get().val()
    #     # c = database.child('Farmer').child('Details').child(farmid).child('City').get().val()
    #
    #     diction = dict(det)
    #     details[i] = diction
    #     # city[i] = c
    # details2 = {
    #     'det': details,
    #     'uid': lis_id,
    #     # 'city': city,
    # }
    # return render(request, 'index.html',details2)
    return render(request, 'index.html', {'cur': curuser})

def account(request):
    return render(request, 'account.html')


def Csignup(request):
    lettersU = string.ascii_uppercase
    lettersD = string.digits
    id = (''.join(random.choice(lettersD) for i in range(3)) + ''.join(random.choice(lettersU) for i in range(1)))
    id1 = 'CW' + id
    name = request.POST.get('name')
    email = request.POST.get('email')
    contactno = request.POST.get('contact')
    address = request.POST.get('address')
    city = request.POST.get('city')
    pin = request.POST.get('pin')
    passw = request.POST.get('pass')
    try:
        user = authe.create_user_with_email_and_password(email, passw)
        mess = 'user created successfully'

        Uid = user['localId']
        data = {
            'Name': name,
            'Email': email,
            'Mobile_No': contactno,
            'Address': address,
            'City': city,
            'Pin code': pin,
            'Cid': id1,
            'Password': passw,
        }
        database.child('Consumer').child('Details').child(Uid).set(data)
        return render(request, "index.html", {'cur': user})
    except:
        mess = 'Failed to create Account!!'
        return render(request, "index.html")


def Clogin(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')
    role = 'con'
    try:
        user = authe.sign_in_with_email_and_password(email, password)
        # id = database.child('Added_Items').shallow().get().val()
        # lis_id = []
        # for i in id:
        #     lis_id.append(i)
        #
        # details = {}
        # farm = {}
        # city = {}
        # for i in lis_id:
        #     det = database.child('Added_Items').child(i).get().val()
        #     farmid = database.child('Added_Items').child(i).child('sellid').get().val()
        #     c = database.child('Seller').child('Details').child(farmid).child('City').get().val()
        #
        #     diction = dict(det)
        #     details[i] = diction
        #     city[i] = c
        #
        # details2 = {
        #     'det': details,
        #     'uid': lis_id,
        #     'city': city,
        # }
        # return redirect('/displaycart/')
        return render(request, 'index.html', {'cur': user})
    except:
        message = "invalid credentials"
        return render(request, "index.html", {'mess': message})


def selsignup(request):
    lettersU = string.ascii_uppercase
    lettersD = string.digits
    id = (''.join(random.choice(lettersD) for i in range(3)) + ''.join(random.choice(lettersU) for i in range(1)))
    id1 = 'CW' + id
    name = request.POST.get('name')
    email = request.POST.get('email')
    adhar = request.POST.get('adhar')
    address = request.POST.get('address')
    city = request.POST.get('city')
    contact = request.POST.get('contact')
    pin = request.POST.get('pin')
    passw = request.POST.get('pass')
    passek = str('CW' + passw)
    try:
        user = authe.create_user_with_email_and_password(email, passek)
        mess = 'user created successfully'

        Uid = user['localId']
        data = {
            'Name': name,
            'Email': email,
            'Mobile_No': contact,
            'Adhar_No': adhar,
            'Address': address,
            'Pin code': pin,
            'Fid': id1,
            'Password': passw,
            'City': city,
        }
        # print("dataaaa:",data)
        database.child('Seller').child('Details').child(Uid).set(data)
        return render(request, 'index.html', {'mess': mess, 'cur': user})
    except:
        mess = 'Failed to create Account!!'
        return render(request, "index.html", {'mess': mess})


def selsignin(request):
    global curuser
    email = request.POST.get('email')
    PW = request.POST.get('pass')
    PWek = str('CW' + PW)
    try:
        user = authe.sign_in_with_email_and_password(email, PWek)
        curuser = authe.current_user
        # sellid = curuser['localId']
        # proid = database.child('Added_Items').shallow().get().val()
        # products = []
        # for i in proid:
        #     products.append(i)
        #
        # details = {}
        # p = 0
        # for i in products:
        #     det = database.child('Added_Items').child(i).get().val()
        #     if det['sellid'] == sellid:
        #         diction = dict(det)
        #
        #         diction['proid'] = i
        #         details[p] = diction
        #         p += 1
        # details2 = {
        #     'det': details,
        # }
        mes = "You are Loged in"
        return render(request, "aditem.html", {'mess': mes})
    except:
        mes = "Invalid Credentials22222"
        return render(request, "index.html", {'mess': mes})

    # global role
    # global curuser
    # email = request.POST.get('email')
    # PW = request.POST.get('pass')
    # PWek = str('ck' + PW)
    #
    # methodpost = request.POST.get('mainlogin')
    # methodpost1 = request.POST.get('innerlogin')
    #
    # if methodpost1:
    #
    #     role = request.POST.get('RoleName')
    #     try:
    #         user = authe.sign_in_with_email_and_password(email, PWek)
    #         curuser = authe.current_user
    #
    #         sellid = curuser['localId']
    #         # print('--------------PWek----------', PWek)
    #         try:
    #             proid = database.child('Added_Items').shallow().get().val()
    #             products = []
    #             for i in proid:
    #                 products.append(i)
    #
    #             details = {}
    #             p = 0
    #             for i in products:
    #                 det = database.child('Added_Items').child(i).get().val()
    #                 if det['sellid'] == sellid:
    #                     diction = dict(det)
    #
    #                     diction['proid'] = i
    #                     details[p] = diction
    #                     p += 1
    #
    #             details2 = {
    #                 'det': details,
    #             }
    #             if role == 'sell':
    #                 return render(request, "aditem.html", details2)
    #             else:
    #                 return render(request, "index.html", {'cur': user})
    #         except:
    #             return render(request, "index.html")
    #     except:
    #         mes = "Invalid Credentials111111"
    #         return render(request, "index.html", {'mess': mes})
    #
    # elif methodpost:
    #     role = request.POST.get('RoleName')
    #     try:
    #         user = authe.sign_in_with_email_and_password(email, PWek)
    #
    #         curuser = authe.current_user
    #         sellid = curuser['localId']
    #         # session_id = user['localId']
    #         # request.session['uid'] = str(session_id)
    #         mes = "You are Loged in"
    #         return render(request, "index.html", {'mess': mes, 'cur': user})
    #     except:
    #         mes = "Invalid Credentials22222"
    #
    #         return render(request, "index.html", {'mess': mes})

def seller(request):
    curuser = authe.current_user
    if curuser:
        additem = request.POST.get('additem')
        sellid = curuser['localId']
        if additem:
            lettersD = string.digits
            oid = (''.join(random.choice(lettersD) for i in range(3)))
            vname = request.POST.get('Item Name')
            vprice = request.POST.get('price')
            vquant = request.POST.get('Quantity')
            url = request.POST.get('url')
            proid = vname[0:3] + oid
            # p = database.child('Seller').child('Details').child(sellid).child('City').get().val()
            fn = database.child('Seller').child('Details').child(sellid).child('Name').get().val()

            productdata = {
                'Product_name': vname,
                'Price': vprice,
                'Quantity': vquant,
                'sellid': sellid,
                'url': url,
                # 'city': c,
                'fname': fn
            }
            database.child('Added_Items').child(proid).set(productdata)

        proid = database.child('Added_Items').shallow().get().val()
        products = []
        for i in proid:
            products.append(i)

        details = {}
        p = 0
        for i in products:
            det = database.child('Added_Items').child(i).get().val()

            if det['sellid'] == sellid:
                diction = dict(det)
                diction['proid'] = i
                details[p] = diction
                p += 1
        details2 = {
            'det': details,
        }

        return render(request, 'aditem.html', details2)
    else:
        return render(request, 'farmlogin.html')


def products(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)
    details = {}
    # city = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        sellid = database.child('Added_Items').child(i).child('sellid').get().val()
        p =database.child('Added_Items').child(i).child('Price').get().val()

        diction = dict(det)
        details[i] = diction
        # city[i] = c
    details2 = {
        'det': details,
        'uid': lis_id,
        'Price':p,
        # 'city': city,
    }
    return render(request, 'products.html', details2)


def blackbox(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Black box'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def glitterbottle(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Glitter bottle'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def heartframe(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Heart frame'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def wallhanging(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'wall hanging'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def kitkatcake(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Kitkat cake'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def clock(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Clock'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def teddy(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Teddy'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def photoframe(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Photo frame'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def chocolatecake(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Chocolate cake'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def cups(request):
    id = database.child('Added_Items').shallow().get().val()
    lis_id = []
    for i in id:
        lis_id.append(i)

    details = {}
    for i in lis_id:
        det = database.child('Added_Items').child(i).get().val()
        if (det['Product_name'] == 'Cups'):
            diction = dict(det)
            details[i] = diction

    details2 = {
        'det': details,
        'uid': lis_id
    }
    return render(request, 'products.html', details2)

def mainpro(request):
    uid = request.GET.get('z')

    proname = database.child('Added_Items').child(uid).child('Product_name').get().val()
    amount = database.child('Added_Items').child(uid).child('Price').get().val()
    quantity = database.child('Added_Items').child(uid).child('Quantity').get().val()
    url = database.child('Added_Items').child(uid).child('url').get().val()
    fname = database.child('Added_Items').child(uid).child('fname').get().val()
    return render(request,'productdetail.html',{ 'proname': proname,'amount': amount,'quantity': quantity, 'url': url, 'fname': fname, 'uid':uid})



def addtocart(request):

    curuser = authe.current_user
    if curuser and role == 'con':
        cid = curuser['localId']
        uid = request.GET.get('z')
        reqquant = request.POST.get('req')
        proname = database.child('Added_Items').child(uid).child('Product_name').get().val()
        amount = database.child('Added_Items').child(uid).child('Price').get().val()
        quantity = database.child('Added_Items').child(uid).child('Quantity').get().val()
        url = database.child('Added_Items').child(uid).child('url').get().val()
        fname = database.child('Added_Items').child(uid).child('fname').get().val()
        sid = database.child('Added_Items').child(uid).child('sellid').get().val()

        productdata = {
            'Productname': proname,
            'Price': amount,
            'Requiredquantity':  reqquant,
            'url': url,
            'sid':sid,
            'totalprice': int(amount) * int(reqquant),

        }

        database.child('Cart').child(cid).child(uid).set(productdata)

        # return render(request, 'product.html',{'proname': proname, 'amount': amount,  'quantity': quantity,
        #                                        'url': url, 'fname': fname,'uid': uid})
        return render(request, 'productdetail.html', {'proname': proname, 'amount': amount, 'quantity': quantity,
                                                'url': url, 'fname': fname,'sid': sid, 'uid': uid})
    else:
        mess = "You need to login"
        return render(request,'consumerlogin.html',{'mess':mess})


def displaycart(request):
    curuser = authe.current_user
    if curuser:
        cid = curuser['localId']
        try:
            sub = request.POST.get('minus')
            addq = request.POST.get('plus')
            id = request.GET.get('proid')
            if sub:
                qunatity = database.child('Cart').child(cid).child(id).child('Requiredquantity').get().val()
                itemprice = database.child('Cart').child(cid).child(id).child('Price').get().val()
                newq = int(qunatity) - 1
                if newq <= 0:
                    newq = 1
                else:
                    tp = int(itemprice) * int(newq)
                    up = {
                        'Requiredquantity': newq,
                        'totalprice': tp
                    }
                    database.child('Cart').child(cid).child(id).update(up)
            elif addq:
                qunatity = database.child('Cart').child(cid).child(id).child('Requiredquantity').get().val()
                newq = int(qunatity) + 1
                itemprice = database.child('Cart').child(cid).child(id).child('Price').get().val()
                tp = int(itemprice) * int(newq)
                up = {
                    'Requiredquantity': newq,
                    'totalprice': tp
                }
                database.child('Cart').child(cid).child(id).update(up)

            proid = database.child('Cart').child(cid).shallow().get().val()
            products = []
            for i in proid:
                products.append(i)
            details = {}
            totamt = []
            maxquant = {}
            sum = 0
            sum1 = 0

            for i in products:
                tamount = database.child('Cart').child(cid).child(i).child('totalprice').get().val()
                sum = sum + tamount
                det = database.child('Cart').child(cid).child(i).get().val()
                maxquantallow = database.child('Added_Items').child(i).child('Quantity').get().val()

                maxquant[i] = maxquantallow

                diction = dict(det)
                details[i] = diction
            sum1 = sum + 20

            add = database.child('Consumer').child('Details').child(cid).child('Address').get().val()
            city = database.child('Consumer').child('Details').child(cid).child('City').get().val()
            pin = database.child('Consumer').child('Details').child(cid).child('Pin code').get().val()

            details2 = {
                'det': details,
                'uid': products,
                'sum': sum,
                'sum1': sum1,
                'add': add,
                'city': city,
                'pin': pin,
                'mq': maxquant,
            }
            # print(details2)
            return render(request, 'cart.html', details2)
        except:
            return render(request, 'nocart.html')
    else:
        mess = "You need to login"
        return render(request, 'consumerlogin.html', {'mess': mess})


def removefromcart(request):
    curuser = authe.current_user
    cid = curuser['localId']
    uid = request.GET.get('z')

    # to remove from cart

    database.child('Cart').child(cid).child(uid).remove()
    try:
        proid = database.child('Cart').child(cid).shallow().get().val()
        products = []
        for i in proid:
            products.append(i)
        details = {}
        totamt = []
        maxquant = {}
        sum = 0
        sum1 = 0
        for i in products:
            tamount = database.child('Cart').child(cid).child(i).child('totalprice').get().val()
            sum = sum + tamount
            det = database.child('Cart').child(cid).child(i).get().val()
            maxquantallow = database.child('Added_Items').child(i).child('Quantity').get().val()

            # diction1 = dict(maxquantallow)
            maxquant[i] = maxquantallow

            diction = dict(det)
            # diction['maxquant']=maxquantallow
            details[i] = diction
        sum1 = sum + 30

        add = database.child('Consumer').child('Details').child(cid).child('Address').get().val()
        city = database.child('Consumer').child('Details').child(cid).child('City').get().val()
        pin = database.child('Consumer').child('Details').child(cid).child('Pin code').get().val()

        details2 = {
            'det': details,
            'uid': products,
            'sum': sum,
            'sum1': sum1,
            'add': add,
            'city': city,
            'pin': pin,
            'mq': maxquant,
        }

        return render(request, 'cart.html', details2)
    except:
        return render(request, 'nocart.html')


def razor(request):
    curuser = authe.current_user
    if request.method == 'POST':
        curuser = authe.current_user
        cid = curuser['localId']
        amount1 = int(request.GET.get('e'))* 100
        client = razorpay.Client(auth=('rzp_test_0KGK9KaxLVwGjU','bqBQqKCMxP4mES6ORkjqqKpP'))
        rep = ('CW'.join(random.choice(string.ascii_uppercase) for i in range(3)) + ''.join(random.choice(string.digits) for i in range(2)))
        orderinfo = client.order.create(dict (amount=amount1, currency="INR", receipt=rep))
        odid = orderinfo['id']
        amm = orderinfo['amount']

        proid = database.child('Cart').child(cid).shallow().get().val()
        products = []
        for i in proid:
            products.append(i)
        details = {}
        maxquant = {}
        sum = 0

        for i in products:
            tamount = database.child('Cart').child(cid).child(i).child('totalprice').get().val()
            sum = sum + tamount
            det = database.child('Cart').child(cid).child(i).get().val()
            maxquantallow = database.child('Added_Items').child(i).child('Quantity').get().val()

            maxquant[i] = maxquantallow

            diction = dict(det)
            details[i] = diction
        sum1 = sum + 20

        add = database.child('Consumer').child('Details').child(cid).child('Address').get().val()
        city = database.child('Consumer').child('Details').child(cid).child('City').get().val()
        pin = database.child('Consumer').child('Details').child(cid).child('Pin code').get().val()

        details2 = {
            'det': details,
            'uid': products,
            'sum': sum,
            'sum1': sum1,
            'add': add,
            'city': city,
            'pin': pin,
            'mq': maxquant,
            'orderinfo': orderinfo,
            'odid':odid,
            'amm': amm,
        }
        return render(request,'confirmorder.html', details2)
    else:
        return render(request, 'index.html',{'cur':curuser})




@csrf_exempt
def success(request):
    global orderid, amount, orderid, amount
    from datetime import date
    today = date.today()
    # d1 = today.strftime("%d/%m/%Y")
    d1 = today.strftime("%Y-%m-%d")
    orderid = request.GET.get('oid')
    amount = request.GET.get('amm')

    curuser = authe.current_user
    cid = curuser['localId']

    name = database.child('Consumer').child('Details').child(cid).child('Name').get().val()
    add = database.child('Consumer').child('Details').child(cid).child('Address').get().val()
    city = database.child('Consumer').child('Details').child(cid).child('City').get().val()
    pin = database.child('Consumer').child('Details').child(cid).child('Pin code').get().val()
    emailid = database.child('Consumer').child('Details').child(cid).child('Email').get().val()

    address = str(add) +"  "+ str(city) +"  "+ str(pin)


    proid = database.child('Cart').child(cid).shallow().get().val()
    products = []
    for i in proid:
        products.append(i)
    details = {}
    sum = 0

    for i in products:
        tamount = database.child('Cart').child(cid).child(i).child('totalprice').get().val()
        sum = sum + tamount
        det = database.child('Cart').child(cid).child(i).get().val()
        diction = dict(det)
        details[i] = diction
        details2 = {
            'Caddress':address,
            'Product_name': diction['Productname'],
            'Required_quant': diction['Requiredquantity'],
            'farmer_id': diction['sid'],
            'OrderDate': d1,
            'Pickup_date': 'None',
            'Pickup_status': 'notpicked',
            'Deliverystatus': 'notdelivered',
        }
        database.child('orderplaced').child(cid).child(orderid).child(i).set(details2)
    sum1 = sum + 20
    info = {
            "title": 'Order Confrimation',
            "orderid": orderid,
            "amount": amount,
            "date": d1,
            "name":name,
            "address":address,
            'sum': sum,
            'sum1': sum1,
            "det": details,
        }
    html_content = render_to_string("emailtemp.html", info)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        'Order Confrimation',
        text_content,
        settings.EMAIL_HOST_USER,
        [emailid],
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
    database.child('Cart').child(cid).remove()
    return render(request, 'thank.html')


def productdetail(request):
    return render(request, 'productdetail.html')


def farmlogin(request):
    return render(request,'farmlogin.html')


def consumerlogin(request):
    return render(request,'consumerlogin.html')


def cart(request):
    return render(request, 'cart.html')


def payment(request):
    return render(request, 'payment.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')


def aditem(request):
    return render(request, 'aditem.html')


def confirmorder(request):
    return render(request, 'confirmorder.html')


def emailtemp(request):
    return render(request, 'emailtemp.html')


def myorders(request):
    return render(request, 'myorders.html')


def myprof(request):
    return render(request, 'myprof.html')


def nocart(request):
    return render(request, 'nocart.html')


def pickup(request):
    return render(request, 'pickup.html')


def thank(request):
    return render(request, 'thank.html')

def logout(request):
    try:
        auth.logout(request)
        authe.current_user = None
        return render(request, "index.html")
    except:
        return render(request, "products.html")