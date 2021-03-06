#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from cmdb.forms import IdcForm
from .models import Idc
from django.contrib.auth.decorators import login_required

@login_required
def idc(request):
    temp_name = "cmdb/cmdb-header.html"
    idc_info = Idc.objects.all()
    return render(request, 'cmdb/idc.html', locals())

@login_required
def idc_add(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == "POST":
        idc_form = IdcForm(request.POST)
        if idc_form.is_valid():
            idc_form.save()
            tips = u"增加成功！"
            display_control = ""
        else:
            tips = u"增加失败！"
            display_control = ""
        return render(request, "cmdb/idc_add.html", locals())
    else:
        display_control = "none"
        idc_form = IdcForm()
        return render(request, "cmdb/idc_add.html", locals())

@login_required
def idc_del(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == 'POST':
        idc_items = request.POST.getlist('idc_check', [])
        if idc_items:
            for n in idc_items:
                Idc.objects.filter(id=n).delete()
    idc_info = Idc.objects.all()
    return render(request, "cmdb/idc.html", locals())

@login_required
def idc_edit(request, ids):
    obj = Idc.objects.get(id=ids)
    allidc = Idc.objects.all()
    return render(request, "cmdb/idc_edit.html", locals())

@login_required
def idc_save(request):
    temp_name = "cmdb/cmdb-header.html"
    if request.method == 'POST':
        idc_id = request.POST.get('id')
        mini = request.POST.get('idc_mini')
        name = request.POST.get('name')
        address = request.POST.get('address')
        tel = request.POST.get('tel')
        contact = request.POST.get('contact')
        contact_phone = request.POST.get('contact_phone')
        cabinet = request.POST.get('cabinet')
        ip_range = request.POST.get('ip_range')
        bandwidth = request.POST.get('bandwidth')
        idc_item = Idc.objects.get(id=idc_id)
        idc_item.name = name
        idc_item.address = address
        idc_item.tel = tel
        idc_item.contact = contact
        idc_item.contact_phone = contact_phone
        idc_item.cabinet = cabinet
        idc_item.ip_range = ip_range
        idc_item.bandwidth = bandwidth
        idc_item.save()
        obj = idc_item
        status = 1
    else:
        status = 2
    return render(request, "cmdb/idc_edit.html", locals())