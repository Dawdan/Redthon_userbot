""" Command: اوقات الصلاة لعواصم الدول باللغـة العربيـة
Credit: @Redthon
@MSS3G -  """

import json
import requests
from . import *

@Redthon.on(admin_cmd(pattern="صلاة(?: |$)(.*)"))
async def get_adzan(adzan):
    MSS3G = adzan.pattern_match.group(1)
    if MSS3G == "صنعاء" or MSS3G == "اليمن":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Sanaa"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>صنعـاء</b>\
	            \n<b>الـدولة  : <b>اليمـن</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "مصر" or MSS3G == "القاهرة" or MSS3G == "القاهره":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Cairo"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>القاهـرة</b>\
	            \n<b>الـدولة  : <b>مصـر</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "بغداد" or MSS3G == "العراق":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Baghdad"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>بغـداد</b>\
	            \n<b>الـدولة  : <b>العـراق</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "دمشق" or MSS3G == "سوريا":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Damascus"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>دمشـق</b>\
	            \n<b>الـدولة  : <b>سـوريا</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "الدوحه" or MSS3G == "قطر":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Doha"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>الدوحـه</b>\
	            \n<b>الـدولة  : <b>قطـر</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "مسقط" or MSS3G == "سلطنه عمان":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Muscat"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>مسقـط</b>\
	            \n<b>الـدولة  : <b>سلطنـة عمـان</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "مكه" or MSS3G == "السعوديه":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Mecca"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>مكـه المكـرمـه</b>\
	            \n<b>الـدولة  : <b>المملكـة العربيـه السعـودية</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "بيروت" or MSS3G == "لبنان":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Beirut"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>بيـروت</b>\
	            \n<b>الـدولة  : <b>لبنـان</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "عمان" or MSS3G == "الاردن":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Amman"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>عَمـان</b>\
	            \n<b>الـدولة  : <b>الاردن</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "الرباط" or MSS3G == "المغرب":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Rabat"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>الربـاط</b>\
	            \n<b>الـدولة  : <b>المغـرب</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "الخرطوم" or MSS3G == "السودان":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Khartoum"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>الخرطـوم</b>\
	            \n<b>الـدولة  : <b>السـودان</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "بنغازي" or MSS3G == "ليبيا":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Benghazi"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>بنغـازي</b>\
	            \n<b>الـدولة  : <b>ليبيـا</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "تونس":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Tunis"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>تونـس</b>\
	            \n<b>الـدولة  : <b>تونـس</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")
    elif MSS3G == "ازمير" or MSS3G == "اسطنبول" or MSS3G == "انقره" or MSS3G == "تركيا":
	    url = f"https://api.pray.zone/v2/times/today.json?city=Izmir"
	    request = requests.get(url)
	    if request.status_code != 200:
	        await edit_delete(
	            adzan,
	            f"** لم يـتم العثور على هـذه المدينه {MSS3G}**\n**-يرجى كتابة اسم العاصمـه او الدولـة بشكـل صحيـح** ",
	            5,
	        )
	        return
	    result = json.loads(request.text)
	    Redthonresult = f"<b>🕋╎اوقـات الصـلاة بالتـوقيت المحلـي لعواصـم الـدول <b>\
	            \n\n<b>المـدينة     : <b>اسطنبـول</b>\
	            \n<b>الـدولة  : <b>تركيـا</b>\
	            \n<b>التـاريخ     : <b>{result['results']['datetime'][0]['date']['gregorian']}</b>\
	            \n<b>الهـجري    : <b>{result['results']['datetime'][0]['date']['hijri']}</b>\
	            \n\n<b>الامـساك    : <b>{result['results']['datetime'][0]['times']['Imsak']}</b>\
	            \n<b>شـروق الشمس  : <b>{result['results']['datetime'][0]['times']['Sunrise']}</b>\
	            \n<b>الـفجر     : <b>{result['results']['datetime'][0]['times']['Fajr']}</b>\
	            \n<b>الضـهر    : <b>{result['results']['datetime'][0]['times']['Dhuhr']}</b>\
	            \n<b>العـصر      : <b>{result['results']['datetime'][0]['times']['Asr']}</b>\
	            \n<b>غـروب الشمس   : <b>{result['results']['datetime'][0]['times']['Sunset']}</b>\
	            \n<b>المـغرب  : <b>{result['results']['datetime'][0]['times']['Maghrib']}</b>\
	            \n<b>العشـاء     : <b>{result['results']['datetime'][0]['times']['Isha']}</b>\
	            \n<b>منتـصف الليل : <b>{result['results']['datetime'][0]['times']['Midnight']}</b>\
		        \n\nᯓ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐑𝐞𝐝𝐭𝐡𝐨𝐧╎@Redthon\
	    "
	    await edit_or_reply(adzan, Redthonresult, "html")



