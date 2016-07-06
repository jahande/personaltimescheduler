# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from schedulerApp.models import WorkSheet, WorkTime, Profile
from schedulerApp.forms import ProfileForm, RegistrationForm
from django.contrib.auth.models import User
#from django.views.decorators.csrf import csrf_protect
import datetime
from django.contrib.auth.decorators import login_required

#@csrf_protect
@login_required
def scheduler2(request, wsId=None):
    #current_date = datetime.datetime.now(
    #csrf_token = {}
    #csrf_token.update(csrf(request))
    #csrfContext = RequestContext(request)
    isStuff = request.user.is_staff

    if request.method == 'POST' and 'workSheetName' in request.POST:
        ws = WorkSheet.objects.create(name=request.POST['workSheetName'], user=request.user)
        return HttpResponseRedirect('/scheduler2/' + str(ws.id))
        #form = WorkSheetForm(request.POST)
        #if form.is_valid():
        #    ws_data = form.cleaned_data
        #   ws = WorkSheet.objects.create(name=ws_data['name'],)
        #   return HttpResponseRedirect('/scheduler2/'+ws.id)

    if not wsId or wsId < 1 or not WorkSheet.objects.count() or not WorkSheet.objects.filter(
        id=wsId, user=request.user) or not WorkSheet.objects.filter(id=wsId, user=request.user)[0]:
        wsIds = WorkSheet.objects.filter(user=request.user)
        if wsIds and wsIds[len(wsIds) - 1]:
            wsId = wsIds[len(wsIds) - 1].id
        else:
            wsId = None

        if not wsId:
            message = 'Please add a work sheet first'
            return render_to_response('scheduler/scheduler2.html', RequestContext(request, locals()))
        else:
            return HttpResponseRedirect('/scheduler2/' + str(wsId))
    if request.method == 'POST':
        if 'finish' in request.POST:
            finish = request.POST['finish']
            if finish == 'ok':
                workTime = WorkTime.objects.filter(workSheet=int(wsId)).order_by('-start')[0]
                workTime.end = datetime.datetime.now()
                workTime.save()
                return HttpResponseRedirect('/scheduler2/' + str(wsId))
        elif 'workTime' in request.POST:
            workTimes = WorkTime.objects.filter(workSheet=int(wsId)).order_by('-start')
            if workTimes and workTimes[0]:
                workTime = workTimes[0]
                if not workTime.end:
                    workTime.end = datetime.datetime.now()
                    workTime.save()
            workTimeName = request.POST['workTime']
            workTime = WorkTime()
            workTime.name = workTimeName
            workTime.start = datetime.datetime.now()
            ws = WorkSheet.objects.filter(id=wsId)[0]
            workTime.workSheet = ws
            workTime.save()

            return HttpResponseRedirect('/scheduler2/' + wsId)
    else:
    #workTimes = WorkTime.objects.filter(workSheet=workSheets[len(workSheets)-1].id
        workSheet = WorkSheet.objects.filter(id=wsId, user=request.user)[0]
        #form = WorkSheetForm()
        workSheets = WorkSheet.objects.filter(user=request.user)
        workTimes = WorkTime.objects.filter(workSheet=workSheet)
        initialData = locals()
        csrfContext = RequestContext(request, initialData)
        return render_to_response('scheduler/scheduler2.html', csrfContext)


@login_required
def profile(request):
    db_profiles = Profile.objects.filter(user=request.user)
    db_profile = None
    if db_profiles:
        db_profile = db_profiles[0]
    if request.method == 'POST':

    #   filledProfileForm = ProfileForm(request.POST)
    ##     cd = filledProfileForm
    # return HttpResponseRedirect('/accounts/profile/')
        profileForm = ProfileForm(request.POST, request.FILES, request.user)#, instance=request.user.profile)
        #profileForm = ProfileForm(instance=request.user.profile)
        if profileForm.is_valid():
            #profileForm.save()
            pfd = profileForm.cleaned_data
            #db_profile = Profile.objects.filter(user=request.user)[0]
            if db_profile:
                db_profile.image.delete()
                db_profile.image = pfd['image']
                db_profile.save()
                return HttpResponseRedirect('/accounts/profile/')
            else:
                p = Profile.objects.create(image=pfd['image'], user=request.user)
                return HttpResponseRedirect('/accounts/profile/')
    else:
        profileForm = ProfileForm()
        csrfContext = RequestContext(request, locals())
        return render_to_response('scheduler/profile.html', csrfContext)


def signup(request,message=None):
    if request.method == 'POST':
        registrationForm = RegistrationForm(request.POST, request.FILES)#, instance=request.user.profile)
        if registrationForm.is_valid():
            rfData = registrationForm.cleaned_data
            u = User()
            u.set_password(rfData['password'])
            u.username = rfData['username']
            u.first_name = rfData['first_name']
            u.last_name = rfData['last_name']
            u.email = rfData['email']
            u.save()

                   # (username=rfData['username'], password=rfData['password'], email=rfData['email'],
                #first_name=rfData['first_name'], last_name=rfData['last_name'])
            p = Profile.objects.create(user=u,image=rfData['image'])
            #message = 'Account successfuly created. you can login now.'
            return HttpResponseRedirect('registration/signup/?message=1')
        else:
            message = 'data is not valid'
            return render_to_response('registration/signup.html', RequestContext(request, locals()))
    else:
        if True and 'message' in request.GET:
            message = 'you have message!'
            if request.GET['message']=='1':
                type=1
                message = 'Account successfuly created. you can login now.'
        registrationForm = RegistrationForm()
        return render_to_response('registration/signup.html', RequestContext(request, locals()))

def page_creator(request):
    return render_to_response('scheduler/page_creator.html');
def page_creator2(request):
    return render_to_response('scheduler/page_creator2.html');