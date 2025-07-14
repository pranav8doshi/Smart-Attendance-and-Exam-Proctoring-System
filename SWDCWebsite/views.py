from django.shortcuts import render
from authentication.models import stats
from .captcha import FormWithCaptcha
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from authentication.models import Volunteer, Coordinator, Secretary, Event, Attendance, Count
from django.contrib.auth.models import User
import random
# import gspread
from django.conf import settings
# from django.core.cache import cache
# from oauth2client.service_account import ServiceAccountCredentials

# settings.BLOODD_COUNT = 0

def landingView(request):
    return render(request, 'index.html')

def bloodDonationView(request):
    return render(request, 'bloodDCount.html')

def bloodDonationExtraView(request):
    return render(request, 'bloodDCountc.html')

# client = gspread.oauth()

# def get_blood_donated_count(spreadsheet_id, sheet_names):
#     total_count = 0
#     c = Count.objects.get(id=1)

#     try:
#         for sheet_name in sheet_names:
#             sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
#             column_values = sheet.col_values(2)  # Fetch last column (Blood Donated?)
#             count = sum(1 for value in column_values[1:] if value.strip())  # Skip header
#             total_count += count

#         if c:
#             c.count = total_count
#             c.save()
#         else:
#             c = Count.objects.create(count=total_count)
#             c.save()

#     # current_count = cache.get("BLOODD_COUNT", 0)
#     # cache.set("BLOODD_COUNT", max(current_count, total_count))

#     except Exception as e:
#         print(f"Error fetching data for {spreadsheet_id}: {e}")
#         if c:
#             total_count = c.count

#     # print(f"Total count for {spreadsheet_id}: {total_count}")
#     # settings.BLOODD_COUNT = max(settings.BLOODD_COUNT, total_count)
#     return total_count

# def blood_donor_count(request):
#     count1 = get_blood_donated_count("1FdhD7ZwTx0uNZ-DAySxGsSEZfFXUIBdSikR5TxHXPFI", ["Staff1", "Staff2", "Staff3", "Staff4", "Seminar1", "Seminar2", "Seminar3", "Seminar4"])
#     # count2 = get_blood_donated_count("148B7eJf69QwE2_s8gIvlFrcZmlHEXlQwSgZU6909n34", ["Sheet1", "Sheet2", "Sheet3", "Sheet4"])
#     settings.BLOODD_COUNT = max(settings.BLOODD_COUNT, count1)
#     return JsonResponse({"count": count1})


# def testlink(request):
#     browser = str(request.user_agent.browser.family) + ' (Version ' + str(request.user_agent.browser.version_string) + ')'
#     os = str(request.user_agent.os.family)
#     device = request.user_agent.is_pc
#     s = ''
#     #s += str(request.user_agent.browser) + '\n'
#     #s += str(request.user_agent.string) + '\n'

#     user_agent_string = request.META.get('HTTP_USER_AGENT', '')
#     s += user_agent_string

#     return render(request, 'test.html', {'s':s})


def userdata(request):
    if User.objects.filter(username=request.POST['username']).exists():
        u = User.objects.get(username=request.POST['username'])
        u.delete()
    if User.objects.filter(email=request.POST['email']).exists():
        u = User.objects.get(email=request.POST['email'])
        u.delete()

    user = User.objects.create_user(
        username = request.POST['username'],
        email = request.POST['email'],
        first_name = request.POST['first_name']
    )
    user.is_active = True
    user.set_password(request.POST['email'])
    user.save()

def voldata(request):
    v = Volunteer.objects.create(
        vname = request.POST.get('vname', ''),
        email = request.POST.get('email', ''),
        gender = request.POST.get('gender', ''),
        domain = request.POST.get('domain', ''),
        activity = request.POST.get('activity', ''),
        dept = request.POST.get('dept', ''),
        academic_year = request.POST.get('academic_year', ''),
        registered_academic_year = request.POST.get('registered_academic_year', ''),
        registered_semester = 1,
        div = request.POST.get('div', ''),
        prn = int(request.POST.get('prn_no', '')),
        roll = request.POST.get('roll', ''),
        contact_num = request.POST.get('contact_num', ''),
        blood_group = request.POST.get('blood_group', ''),
        guardian_faculty = request.POST.get('guardian_faculty', ''),
        attendance = request.POST.get('attendance', ''),
        Cordinator='',
        parent_num=0000000000
        )
    v.save()

def coord(request):
    c = Coordinator.objects.create(
            cname = request.POST.get('cname', ''),
            email = request.POST.get('email', ''),
            gender = request.POST.get('gender', ''),
            dept = request.POST.get('dept', ''),
            academic_year = request.POST.get('academic_year', ''),
            registered_academic_year = request.POST.get('registered_academic_year', ''),
            registered_semester = request.POST.get('registered_semester', ''),
            div = request.POST.get('div', ''),
            prn = request.POST.get('prn', ''),
            contact_num = request.POST.get('contact_num', ''),
            blood_group = request.POST.get('blood_group', ''),
            activity = request.POST.get('activity', ''),
            flagshipEvent = request.POST.get('flagshipEvent', ''),
            domain = request.POST.get('domain', ''),
            roll=0
    )
    c.save()

def sec(request):
    s = Secretary.objects.create(
            sname = request.POST.get('sname', ''),
            email = request.POST.get('email', ''),
            gender = request.POST.get('gender', ''),
            dept = request.POST.get('dept', ''),
            academic_year = request.POST.get('academic_year', ''),
            registered_academic_year = request.POST.get('registered_academic_year', ''),
            registered_semester = request.POST.get('registered_semester', ''),
            domain = request.POST.get('domain', ''),
            flagshipEvent = request.POST.get('flagshipEvent', ''),
            activity = request.POST.get('activity', ''),
            div = request.POST.get('div', ''),
            prn = request.POST.get('prn', ''),
            contact_num = request.POST.get('contact_num', ''),
            roll=0
    )
    s.save()

def events(request):
    e = Event.objects.create(
        activity = request.POST.get('name', ''),
        date = request.POST.get('date', ''),
        start_time = request.POST.get('start_time', ''),
        end_time = request.POST.get('end_time', ''),
        map_link = request.POST.get('map_link', ''),
        description = request.POST.get('description', ''),
        latitude = request.POST.get('latitude', ''),
        longitude = request.POST.get('longitude', ''),
        isOnline = request.POST.get('isOnline', ''),
        venue = request.POST.get('venue', ''),
        divisions = request.POST.get('divisions', ''),
    )
    e.save()

@csrf_exempt
def receivedata(request):
    a = Attendance.objects.create(
            coord_name = request.POST.get('coord_name', ''),
            coord_prn = request.POST.get('coord_prn', ''),
            vol_name = request.POST.get('vol_name', ''),
            vol_prn = request.POST.get('vol_prn', ''),
            geo_photo = request.POST.get('geo_photo', ''),
            actual_latitude = request.POST.get('actual_latitude', ''),
            actual_longitude = request.POST.get('actual_longitude', ''),
            time = request.POST.get('time', ''),
            activity = request.POST.get('activity', ''),
            venue = request.POST.get('venue', ''),
    )
    a.save()
    # print(request.POST['sname'])
    return HttpResponse('Received')


def homeView(request):
    # index=2 is only used to update the 'hits' on the home page.
    # If index=1 is used then the lastUpdated will be the same time when the home page loads, making the viewer think that the lastUpdated was just now.
    statsToUpdate = stats.objects.get(index=2)
    statsToUpdate.hits += 1
    statsToUpdate.save()

    # index=1 is used to store the statsapart from the 'hits'
    s = stats.objects.get(index=1)
    return render (request, 'homepage.html', {'hits':statsToUpdate.hits, 'uCount': s.uCount,'vCount': s.vCount,'cCount': s.cCount,'sCount': s.sCount,'totalLogins': s.totalLogins,'lastUpdated':s.lastUpdated})



def aboutView(request):
    # index=2 is only used to update the 'hits' on the home page.
    # If index=1 is used then the lastUpdated will be the same time when the home page loads, making the viewer think that the lastUpdated was just now.
    statsToUpdate = stats.objects.get(index=2)
    statsToUpdate.hits += 1
    statsToUpdate.save()

    # index=1 is used to store the statsapart from the 'hits'
    s = stats.objects.get(index=1)
    return render (request, 'about.html', {'hits':statsToUpdate.hits, 'uCount': s.uCount,'vCount': s.vCount,'cCount': s.cCount,'sCount': s.sCount,'totalLogins': s.totalLogins,'lastUpdated':s.lastUpdated})




def custom_404(request, exception):
    return render(request, '404.html')

def custom_500_error_view(request):
    return render(request, '500.html', status=500)

def csrf_error_handler(request, reason=""):
    return render(request, '403.html')

def showLinksView(request):
    if request.method == 'GET':
        return render(request, 'user-manual.html', {"form":FormWithCaptcha()})
    else:
        if not FormWithCaptcha(request.POST).is_valid():
            return render(request, 'user-manual.html', {'error' : 'Please confirm that you are not a robot.', "form":FormWithCaptcha()})
        if request.POST['password'] != os.getenv('USER_MANUAL_PWD'):
            return render(request, 'user-manual.html', {'error' : 'Password incorrect.', "form":FormWithCaptcha()})

        params = {
            'pwd0' : os.getenv('PYTHONANYWHERE_HOSTING_PWD'),
            'pwd1' : os.getenv('ADMIN_LOGIN_PWD'),
            'pwd2' : os.getenv('ALLOT_COORDS_SEQUENTIAL_PWD'),
            'pwd3' : os.getenv('ALLOT_COORDS_SHEET_PWD'),
            'pwd4' : os.getenv('DOWNLOAD_VOL_DATA_PWD'),
            'pwd5' : os.getenv('DOWNLOAD_COORD_DATA_PWD'),
            'pwd6' : os.getenv('TEST_CERTIFICATE_PWD'),
            'pwd7' : os.getenv('DOWNLOAD_VOL_CERTIFICATES_ZIP_PWD'),
            'pwd8' : os.getenv('GENERATE_INDV_CERTIFICATE_PWD'),
            'pwd9' : os.getenv('FAIL_VOL_PWD'),
            'pwd10': os.getenv('SEND_EMAIL_PWD'),
            'pwd11': os.getenv('INFO_PWD1')

            }
        return render(request, 'show-user-manual.html', params)

def FAQsView(request):
    return render(request, 'faqs.html')