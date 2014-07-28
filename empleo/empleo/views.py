#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from models import *
from django.http import HttpResponse
from django import template
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os
import datetime
from django.contrib.auth.decorators import login_required
import StringIO
from capcha import capthaGenerate
import urllib2
import hashlib
from PIL import Image
######################################################################
@csrf_exempt
@login_required
def edite_cv2(request):

	if request.method == "POST":
		obj = CV.objects.filter(id = request.POST['id'])[0]
		obj.ip = request.META['REMOTE_ADDR']
		obj.date = datetime.datetime.now()
		obj.title=request.POST['title']
		obj.area=request.POST['areal']
		obj.education=request.POST['education']
		obj.experencia=request.POST['experencia']
		obj.english=request.POST['english']
		obj.age=request.POST['age']
		obj.url= request.POST['url']
		obj.firma= request.POST['name']
		obj.type= request.POST['tipo']
		obj.user = request.user.id
		obj.permiso = request.POST['permiso']
		obj.nacional = request.POST['nacional']
		obj.user=request.user.id
		

		try:
			obj.cv= request.FILES['CV']
		except:
			pass

		obj.save()

		ur=''
		try:
			ur=obj.cv.url
		except:
			ur=''
		d={'date':obj.date,'title':obj.title,'areal':obj.area,'education':obj.education,'experencia':obj.experencia,'age':obj.age, 'english':obj.english,'permiso':obj.permiso,'nacional':obj.nacional,'firma':obj.firma,'type':obj.type, 'id':obj.id,'urlcv':ur,'url':obj.url,'srip':'document.location.href="/"'}

		if (request.user.is_superuser) or (str(request.user.id) == str(obj.user)):
			t = get_template("edit_cv.html")
			c = Context({'id':obj.id})
			html2 = t.render(c)
			d.update({'edit':html2})
			
		t = get_template("cv_view.html")
		c = Context(d)
		html = t.render(c)

		return HttpResponse(html)

############################################################################
@login_required
def send(request,idd):
	if request.method == "GET":
		title = CV.objects.filter(id = idd)[0].title

		cap=  capthaGenerate(request)
		stt = request.user.first_name + ' '+ request.user.last_name
		mm = hashlib.md5()
		mm.update(cap[1])
		if request.user.is_superuser:
			disb=''
		else:
			disb='disabled'
		d={'capcha':cap[0],'email':request.user.email,'name': stt,'capcha_value': mm.hexdigest(),'disb':disb,'titl':title, 'id':idd}
		t = get_template("send.html")
		c = Context(d)
		c.update(csrf(request))
		html = t.render(c)
		return HttpResponse(html)
	if request.method == "POST":
		obj = CV.objects.filter(id = request.POST['id'])[0]
		email=obj.email
		url='http://localhost:8000/oferta_view/'+str(obj.id)
		title=obj.title
		
		d={'url':url,'title':title, 'Text': request.POST['text'],'email':request.POST['email']}
		t = get_template("send_mail.html")
		c = Context(d)
		text = t.render(c)
		
		send_mail(title, text, 'ofertasdeempleo@bk.ru',    [email], fail_silently=False)
		
		d={}
		t = get_template("mail.html")
		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)

######################################################################

######################################################################
@csrf_protect
def edite_cv(request):
	if request.method == 'POST':
		list=CV.objects.filter(id = request.POST['id'])
		if len(list) == 0:
			return redirect('/')
		obj=list[0]
		t = get_template("edite_cv.html")
		list1=[]
		if obj.area == 'Argentina':
			list1.append('<option selected>Argentina</option>')
		else:
			list1.append('<option>Argentina</option>')
		
		if obj.area == 'Buenos Aires':
			list1.append('<option selected>Buenos Aires</option>')
		else:
			list1.append('<option>Buenos Aires</option>')
			
		if obj.area == 'Catamarca':
			list1.append('<option selected>Catamarca</option>')
		else:
			list1.append('<option>Catamarca</option>')
			
		if obj.area == 'Chaco':
			list1.append('<option selected>Chaco</option>')
		else:
			list1.append('<option>Chaco</option>')
			
		if obj.area == 'Chubut':
			list1.append('<option selected>Chubut</option>')
		else:
			list1.append('<option>Chubut</option>')
			
		if obj.area == 'Corrientes':
			list1.append('<option selected>Corrientes</option>')
		else:
			list1.append('<option>Corrientes</option>')
			
		if obj.area == 'Córdoba':
			list1.append('<option selected>Córdoba</option>')
		else:
			list1.append('<option>Córdoba</option>')
			
		if obj.area == 'Ríos':
			list1.append('<option selected>Ríos</option>')
		else:
			list1.append('<option>Ríos</option>')
			
		if obj.area == 'Entre':
			list1.append('<option selected>Entre</option>')
		else:
			list1.append('<option>Entre</option>')
		
		if obj.area == 'Formosa':
			list1.append('<option selected>Formosa</option>')
		else:
			list1.append('<option>Formosa</option>')
		
		if obj.area == 'Jujuy':
			list1.append('<option selected>Jujuy</option>')
		else:
			list1.append('<option>Jujuy</option>')
		
		if obj.area == 'La Pampa':
			list1.append('<option selected>La Pampa</option>')
		else:
			list1.append('<option>La Pampa</option>')

		if obj.area == 'La Rioja':
			list1.append('<option selected>La Rioja</option>')
		else:
			list1.append('<option>La Rioja</option>')
			
		if obj.area == 'Mendoza':
			list1.append('<option selected>Mendoza</option>')
		else:
			list1.append('<option>Mendoza</option>')
			
		if obj.area == 'Misiones':
			list1.append('<option selected>Misiones</option>')
		else:
			list1.append('<option>Misiones</option>')
			
		if obj.area == 'Neuquén':
			list1.append('<option selected>Neuquén</option>')
		else:
			list1.append('<option>Neuquén</option>')

		if obj.area == 'Río Negro':
			list1.append('<option selected>Río Negro</option>')
		else:
			list1.append('<option>Río Negro</option>')
			
		if obj.area == 'Salta':
			list1.append('<option selected>Salta</option>')
		else:
			list1.append('<option>Salta</option>')
			
		if obj.area == 'San Juan':
			list1.append('<option selected>San Juan</option>')
		else:
			list1.append('<option>San Juan</option>')
			
		if obj.area == 'San Luis':
			list1.append('<option selected>San Luis</option>')
		else:
			list1.append('<option>San Luis</option>')
			
		if obj.area == 'Santa Cruz':
			list1.append('<option selected>Santa Cruz</option>')
		else:
			list1.append('<option>Santa Cruz</option>')
			
		if obj.area == 'Santa Fe':
			list1.append('<option selected>Santa Fe</option>')
		else:
			list1.append('<option>Santa Fe</option>')
			
		if obj.area == 'Santiago del Estero':
			list1.append('<option selected>Santiago del Estero</option>')
		else:
			list1.append('<option>Santiago del Estero</option>')
			
		if obj.area == 'Tierra del Fuego':
			list1.append('<option selected>Tierra del Fuego</option>')
		else:
			list1.append('<option>Tierra del Fuego</option>')
			
		if obj.area == 'Tucumán':
			list1.append('<option selected>Tucumán</option>')
		else:
			list1.append('<option>Tucumán</option>')
		
			
		list2=[]

		if obj.type == 'Cualquiera':
			list2.append('<option selected>Cualquiera</option>')
		else:
			list2.append('<option>Cualquiera</option>')

			
		if obj.type == 'Tiempo parcial':
			list2.append('<option selected>Tiempo parcial</option>')
		else:
			list2.append('<option>Tiempo parcial</option>')

		
		if obj.type == 'Tiempo completo':
			list2.append('<option selected>Tiempo completo</option>')
		else:
			list2.append('<option>Tiempo completo</option>')

			
		if obj.type == 'Autónomo':
			list2.append('<option selected>Autónomo</option>')
		else:
			list2.append('<option>Autónomo</option>')

		if obj.type == 'Temporal':
			list2.append('<option selected>Temporal</option>')
		else:
			list2.append('<option>Temporal</option>')

		if obj.type == 'Prácticas':
			list2.append('<option selected>Prácticas</option>')
		else:
			list2.append('<option>Prácticas</option>')

		if obj.type == 'Voluntariado':
			list2.append('<option selected>Voluntariado</option>')
		else:
			list2.append('<option>Voluntariado</option>')
	

		ur=''
		try:
			ur=obj.cv.path
		except:
			pass

		d={'title':obj.title,'education':obj.education,'experencia':obj.experencia,'email':obj.email,'firma':obj.firma,'url':obj.url,'list1':list1,'list2':list2,'id':obj.id,'age':obj.age,'english':obj.english,'permiso':obj.permiso,'nacional':obj.nacional,'firma':obj.firma,'urlcv':ur}

		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)
######################################################################
def grab(request):
	if request.method == 'GET':
		if not request.user.is_superuser:
			return redirect('/')
		step = 1
		st=''
		for j in range(10):
			step=step+20
			#url='http://www.computrabajo.com.ar/bt-ofrlistado.htm?BqdPalabras=&BqdComienzo='+str(step)+'&Bqd=%2BST001%20%2BTM001%20%20'
			#
			url='http://www.computrabajo.com.ar/bt-ofrlistado.htm?BqdPalabras=&BqdComienzo='+str(step)+'&Bqd=%2BST004%20%2BTM001%20%20'
			page = urllib2.urlopen(url)
			html = page.read()
			nom=html.find('Resultados')
			html=html[nom+2:]
			
			for i in range(20):
				nom=nom=html.find('href')
				html=html[nom+6:]
				nom = html.find('>')
				st=st+'http://www.computrabajo.com.ar/'+html[0:nom-1]+" <br>"
				###################################################
				obj=Oferta()
				#obj.area = "Buenos Aires"
				obj.area = "Córdoba"
				obj.date = datetime.datetime.now()
				obj.ip = request.META['REMOTE_ADDR']
				url1='http://www.computrabajo.com.ar/'+html[0:nom-1]
				page1 = urllib2.urlopen(url1)
				html1 = page1.read()
				n=html1.find('pagead/show_ads.js">')
				html1=html1[n+3:]
				n=html1.find('pagead/show_ads.js">')
				html1=html1[n+3:]
				
				n=html1.find('<b>')
				html1=html1[n+3:]
				n=html1.find('</b>')
				obj.firma=html1[:n].decode('cp1252')
				html1=html1[n+2:]
				
				
				n=html1.find('<b>')
				html1=html1[n+3:]
				n=html1.find('</b>')
				obj.title=html1[:n].decode('cp1252')
				html1=html1[n+2:]
				
				
				n=html1.find('face="Tahoma, Arial">')
				html1=html1[n+21:]
				n=html1.find('</font>')
				obj.Descripcion=html1[:n].decode('cp1252')
				html1=html1[n+2:]
				
				
				n=html1.find('Salario')
				html1=html1[n:]
				n=html1.find('face="Tahoma, Arial">')
				html1=html1[n+21:]
				n=html1.find('</font>')
				obj.Descripcion= obj.Descripcion+' Salario: '+html1[:n].decode('cp1252')
				html1=html1[n+2:]
				
				
				n=html1.find('Tipo de trabajo:')
				html1=html1[n:]
				n=html1.find('face="Tahoma, Arial">')
				html1=html1[n+21:]
				n=html1.find('</font>')
				
				obj.type= html1[:n].decode('cp1252').strip()
				
				html1=html1[n+2:]
				
				#obj.Requisitos='  '
				
				n=html1.find('Correo')
				html1=html1[n:]
				n=html1.find(' <td>')
				html1=html1[n+5:]
				n=html1.find('</td>')
				link = 'http://www.computrabajo.com.ar/'+html1[10:n-2].decode('cp1252')
				img = urllib2.urlopen(link).read()
				im = Image.open(StringIO.StringIO(img))
				response = HttpResponse(mimetype="image/png")
				return response
				#return HttpResponse(im.size[0]//20)
				email=''
				x=0
				while x<im.size[0]:
					im1 = im.crop((x,0,x+8,im.size[1]))
					sum=0
					for i in range(8):
						for j in range(im.size[1]):
							sum = sum +im1.getpixel((i,j))
					if sum == 0:
						email=email+' '
					elif sum == 4:
						email=email+'.'
					elif sum == 12:
						
						email=email+'r'
					elif sum == 20:
						email=email+'r'
					elif sum == 30:
						email=email+'@'
					elif sum == 14:
						email=email+'v'
					elif sum == 21:
						email=email+'a'
					elif sum == 16:
						email=email+'t'
					elif sum == 18:
						im2 = im.crop((x,4,x+8,12))
						sum2 = 0
						for k in range(8):
							for m in range(8):
								sum2 = sum2 +im2.getpixel((k,m))
						im2.save(response, "png")
						#email=email+'s'
						#return response
						#return HttpResponse(sum2)
						if sum2 == 12:
							email=email+'s'
						else:
							email=email+'o'
						
					elif sum == 15:
						email=email+'c'
					elif sum == 23:
						email=email+'m'
					elif sum == 17:
						email=email+'n'
					elif sum == 27:
						email=email+'g'
					else:
						im1.save(response, "png")
						return response
						return HttpResponse(sum)
					x = x+8
				obj.email = email
				
				#return HttpResponse('http://www.computrabajo.com.ar/'+html1[10:n-2].decode('cp1252'))
				#obj.Requisitos=  html1[:n].decode('cp1252')
				
				#return HttpResponse(obj.Requisitos)
				html1=html1[n+2:]
				
				
				obj.save()
				#except:
				#	return HttpResponse(obj.firma)
				###################################################
				
				html=html[nom:]
			
		return HttpResponse(st)

#######################################################################
@csrf_exempt
def cv_view(request,id):
	if request.method == "GET":
		list=CV.objects.filter(id=id)
		if len(list)==0:
			return redirect('/')
		obj=list[0]
		ur=''
		try:
			ur=obj.cv.url
		except:
			ur=''
		d={'date':obj.date,'title':obj.title,'areal':obj.area,'education':obj.education,'experencia':obj.experencia,'age':obj.age, 'english':obj.english,'permiso':obj.permiso,'nacional':obj.nacional,'firma':obj.firma,'type':obj.type, 'id':obj.id,'urlcv':ur,'url':obj.url,'srip':"window.close();"}

		if (request.user.is_superuser) or (str(request.user.id) == str(obj.user)):
			t = get_template("edit_cv.html")
			c = Context({'id':obj.id})
			html2 = t.render(c)
			d.update({'edit':html2})
			
		t = get_template("cv_view.html")
		c = Context(d)
		html = t.render(c)

		return HttpResponse(html)
############################################################################
@login_required
def send_cv(request,idd):
	if request.method == "GET":
		title = Oferta.objects.filter(id = idd)[0].title

		cap=  capthaGenerate(request)
		stt = request.user.first_name + ' '+ request.user.last_name
		mm = hashlib.md5()
		mm.update(cap[1])
		if request.user.is_superuser:
			disb=''
		else:
			disb='disabled'
		d={'capcha':cap[0],'email':request.user.email,'name': stt,'capcha_value': mm.hexdigest(),'disb':disb,'titl':title, 'id':idd}
		t = get_template("send_cv.html")
		c = Context(d)
		c.update(csrf(request))
		html = t.render(c)
		return HttpResponse(html)
	if request.method == "POST":
		obj = Oferta.objects.filter(id = request.POST['id'])[0]
		email=obj.email
		url='http://localhost:8000/oferta_view/'+str(obj.id)
		title=obj.title
		
		d={'url':url,'title':title, 'Nombre': request.POST['name'],'email':request.POST['email'],'local':request.POST['areal'],'Experencia':request.POST['experencia'],'Estudios': request.POST['education'],'Edad': request.POST['age'],'english':request.POST['english'],'Permiso': request.POST['permiso'],'Nacionalidad': request.POST['nacional']}
		t = get_template("send_mail_cv.html")
		c = Context(d)
		text = t.render(c)
		
		try:
			cv = request.FILES['CV']
			mail = EmailMessage(title, text, 'ofertasdeempleo@bk.ru', [email])
			mail.attach(cv.name, cv.read(), cv.content_type)
			mail.send()
		except:
			send_mail(title, text, 'ofertasdeempleo@bk.ru',    [email], fail_silently=False)
		
		d={}
		t = get_template("mail.html")
		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)

######################################################################
#######################################################################
def rss(request):
	if request.method == "GET":
		list = Oferta.objects.all().order_by('-date')[0:20]
		L=[]
		for i in list:
			obj=RSS()
			obj.date = i.date
			obj.subject=i.title
			obj.text = i.Descripcion
			obj.url= 'http://localhost:8000/oferta_view/'+str(i.id)
			L.append(obj)
		d={'date':datetime.datetime.now(),'List':L}
		t = get_template("rss.html")
		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)

#######################################################################

@csrf_protect
def save_oferta(request):
	if request.method == 'POST':
		list=Oferta.objects.filter(id = request.POST['id'])
		if len(list) == 0:
			return HttpResponse(0)
	
		obj=list[0]
		obj.title=request.POST['title']
		obj.area=request.POST['areal']
		obj.Descripcion=request.POST['description']
		obj.Requisitos=request.POST['requisitos']
		obj.email=request.POST['email']
		obj.firma=request.POST['firma']
		obj.url=request.POST['url']
		obj.type=request.POST['tipo']
		obj.save()
		return HttpResponse(1)

@csrf_protect
def edite_oferta(request):
	if request.method == 'POST':
		list=Oferta.objects.filter(id = request.POST['id'])
		if len(list) == 0:
			return redirect('/')
		obj=list[0]
		t = get_template("edite_oferta.html")
		list1=[]
		if obj.area == 'Argentina':
			list1.append('<option selected>Argentina</option>')
		else:
			list1.append('<option>Argentina</option>')
		
		if obj.area == 'Buenos Aires':
			list1.append('<option selected>Buenos Aires</option>')
		else:
			list1.append('<option>Buenos Aires</option>')
			
		if obj.area == 'Catamarca':
			list1.append('<option selected>Catamarca</option>')
		else:
			list1.append('<option>Catamarca</option>')
			
		if obj.area == 'Chaco':
			list1.append('<option selected>Chaco</option>')
		else:
			list1.append('<option>Chaco</option>')
			
		if obj.area == 'Chubut':
			list1.append('<option selected>Chubut</option>')
		else:
			list1.append('<option>Chubut</option>')
			
		if obj.area == 'Corrientes':
			list1.append('<option selected>Corrientes</option>')
		else:
			list1.append('<option>Corrientes</option>')
			
		if obj.area == 'Córdoba':
			list1.append('<option selected>Córdoba</option>')
		else:
			list1.append('<option>Córdoba</option>')
			
		if obj.area == 'Ríos':
			list1.append('<option selected>Ríos</option>')
		else:
			list1.append('<option>Ríos</option>')
			
		if obj.area == 'Entre':
			list1.append('<option selected>Entre</option>')
		else:
			list1.append('<option>Entre</option>')
		
		if obj.area == 'Formosa':
			list1.append('<option selected>Formosa</option>')
		else:
			list1.append('<option>Formosa</option>')
		
		if obj.area == 'Jujuy':
			list1.append('<option selected>Jujuy</option>')
		else:
			list1.append('<option>Jujuy</option>')
		
		if obj.area == 'La Pampa':
			list1.append('<option selected>La Pampa</option>')
		else:
			list1.append('<option>La Pampa</option>')

		if obj.area == 'La Rioja':
			list1.append('<option selected>La Rioja</option>')
		else:
			list1.append('<option>La Rioja</option>')
			
		if obj.area == 'Mendoza':
			list1.append('<option selected>Mendoza</option>')
		else:
			list1.append('<option>Mendoza</option>')
			
		if obj.area == 'Misiones':
			list1.append('<option selected>Misiones</option>')
		else:
			list1.append('<option>Misiones</option>')
			
		if obj.area == 'Neuquén':
			list1.append('<option selected>Neuquén</option>')
		else:
			list1.append('<option>Neuquén</option>')

		if obj.area == 'Río Negro':
			list1.append('<option selected>Río Negro</option>')
		else:
			list1.append('<option>Río Negro</option>')
			
		if obj.area == 'Salta':
			list1.append('<option selected>Salta</option>')
		else:
			list1.append('<option>Salta</option>')
			
		if obj.area == 'San Juan':
			list1.append('<option selected>San Juan</option>')
		else:
			list1.append('<option>San Juan</option>')
			
		if obj.area == 'San Luis':
			list1.append('<option selected>San Luis</option>')
		else:
			list1.append('<option>San Luis</option>')
			
		if obj.area == 'Santa Cruz':
			list1.append('<option selected>Santa Cruz</option>')
		else:
			list1.append('<option>Santa Cruz</option>')
			
		if obj.area == 'Santa Fe':
			list1.append('<option selected>Santa Fe</option>')
		else:
			list1.append('<option>Santa Fe</option>')
			
		if obj.area == 'Santiago del Estero':
			list1.append('<option selected>Santiago del Estero</option>')
		else:
			list1.append('<option>Santiago del Estero</option>')
			
		if obj.area == 'Tierra del Fuego':
			list1.append('<option selected>Tierra del Fuego</option>')
		else:
			list1.append('<option>Tierra del Fuego</option>')
			
		if obj.area == 'Tucumán':
			list1.append('<option selected>Tucumán</option>')
		else:
			list1.append('<option>Tucumán</option>')
		
			
		list2=[]

		if obj.type == 'Cualquiera':
			list2.append('<option selected>Cualquiera</option>')
		else:
			list2.append('<option>Cualquiera</option>')

			
		if obj.type == 'Tiempo parcial':
			list2.append('<option selected>Tiempo parcial</option>')
		else:
			list2.append('<option>Tiempo parcial</option>')

			
		if obj.type == 'Tiempo completo':
			list2.append('<option selected>Tiempo completo</option>')
		else:
			list2.append('<option>Tiempo completo</option>')

			
		if obj.type == 'Autónomo':
			list2.append('<option selected>Autónomo</option>')
		else:
			list2.append('<option>Autónomo</option>')

		if obj.type == 'Temporal':
			list2.append('<option selected>Temporal</option>')
		else:
			list2.append('<option>Temporal</option>')

		if obj.type == 'Prácticas':
			list2.append('<option selected>Prácticas</option>')
		else:
			list2.append('<option>Prácticas</option>')

		if obj.type == 'Voluntariado':
			list2.append('<option selected>Voluntariado</option>')
		else:
			list2.append('<option>Voluntariado</option>')



		d={'title':obj.title,'description':obj.Descripcion,'requisitos':obj.Requisitos,'email':obj.email,'firma':obj.firma,'url':obj.url,'list1':list1,'list2':list2,'id':obj.id}
		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)


@csrf_protect
def delete_oferta(request):
	if request.method == 'POST':
		list=Oferta.objects.filter(id = request.POST['id'])
		for i in list:
			i.delete()
		return redirect('/')
		

@csrf_protect
def delete_cv(request):
	if request.method == 'POST':
		list=CV.objects.filter(id = request.POST['id'])
		for i in list:
			i.delete()
		return redirect('/')


@csrf_exempt
def oferta_view(request,id):
	if request.method == "GET":
		list=Oferta.objects.filter(id=id)
		if len(list)==0:
			return redirect('/')
		obj=list[0]
		d={'date':obj.date,'title':obj.title,'area':obj.area,'Descripcion':obj.Descripcion,'Requisitos':obj.Requisitos, 'firma':obj.firma,'type':obj.type, 'id':obj.id,'srip':'window.close();'}

		if (request.user.is_superuser) or (str(request.user.id) == obj.user):
			t = get_template("edit.html")
			c = Context({'id':obj.id})
			html2 = t.render(c)
			d.update({'edit':html2})
			
		t = get_template("oferta_view.html")
		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)



@csrf_exempt
def check_capcha(request):
# return HttpResponse(5)
	if request.method == 'POST':
		pass

	else:
		m = capthaGenerate(request)
		mm = hashlib.md5()
		mm.update(m[1])
		d={'capcha_value': mm.hexdigest(), 'capcha': m[0]}
		t = get_template("capcha_group.html")
		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)

@login_required
def oferta(request):
	if request.method == "GET":
		cap=  capthaGenerate(request)
		st = ''#request.user.first_name + ' '+ request.user.last_name
		mm = hashlib.md5()
		mm.update(cap[1])
		if request.user.is_superuser:
			disb=''
		else:
			disb='disabled'
		d={'capcha':cap[0],'email':request.user.email,'firma': st,'capcha_value': mm.hexdigest(),'disb':disb}
		t = get_template("oferta.html")
		c = Context(d)
		c.update(csrf(request))
		html = t.render(c)
		return HttpResponse(html)
	if request.method == "POST":
		obj = Oferta()
		obj.ip = request.META['REMOTE_ADDR']
		obj.date = datetime.datetime.now()
		obj.title=request.POST['title']
		obj.area=request.POST['areal']
		obj.Descripcion=request.POST['description']
		obj.Requisitos=request.POST['requisitos']
		if request.user.is_superuser:
			obj.email= request.POST['contacto']
		else:
			obj.email= request.POST['email']
		obj.url= request.POST['url']
		obj.firma= request.POST['firma']
		obj.type= request.POST['tipo']
		obj.user = request.user.id
		obj.save()
		d={'date':obj.date,'title':obj.title,'area':obj.area,'Descripcion':obj.Descripcion,'Requisitos':obj.Requisitos, 'firma':obj.firma,'type':obj.type,'srip':'document.location.href="/"'}
		t = get_template("edit.html")
		c = Context({'id':obj.id})
		html2 = t.render(c)
		d.update({'edit':html2})
		t = get_template("oferta_view.html")
		c = Context(d)
		html = t.render(c)
		return HttpResponse(html)
############################################################################
@login_required
def cv(request):
	if request.method == "GET":
		cap=  capthaGenerate(request)
		stt = request.user.first_name + ' '+ request.user.last_name
		mm = hashlib.md5()
		mm.update(cap[1])
		if request.user.is_superuser:
			disb=''
		else:
			disb='disabled'
		d={'capcha':cap[0],'email':request.user.email,'name': stt,'capcha_value': mm.hexdigest(),'disb':disb,'srip':'document.location.href="/"'}
		t = get_template("cv.html")
		c = Context(d)
		c.update(csrf(request))
		html = t.render(c)
		return HttpResponse(html)
	if request.method == "POST":
		obj = CV()
		obj.ip = request.META['REMOTE_ADDR']
		obj.date = datetime.datetime.now()
		obj.title=request.POST['title']
		obj.area=request.POST['areal']
		obj.education=request.POST['education']
		obj.experencia=request.POST['experencia']
		obj.english=request.POST['english']
		obj.age=request.POST['age']
		if request.user.is_superuser:
			obj.email= request.POST['contacto']
		else:
			obj.email= request.POST['email']
		obj.url= request.POST['url']
		obj.firma= request.POST['name']
		obj.type= request.POST['tipo']
		obj.user = request.user.id
		obj.permiso = request.POST['permiso']
		obj.nacional = request.POST['nacional']
		obj.user=request.user.id
		

		try:
			obj.cv= request.FILES['CV']
		except:
			pass

		obj.save()

		ur=''
		try:
			ur=obj.cv.url
		except:
			ur=''
		d={'date':obj.date,'title':obj.title,'areal':obj.area,'education':obj.education,'experencia':obj.experencia,'age':obj.age, 'english':obj.english,'permiso':obj.permiso,'nacional':obj.nacional,'firma':obj.firma,'type':obj.type, 'id':obj.id,'urlcv':ur,'url':obj.url,'srip':'document.location.href="/"'}

		if (request.user.is_superuser) or (str(request.user.id) == str(obj.user)):
			t = get_template("edit_cv.html")
			c = Context({'id':obj.id})
			html2 = t.render(c)
			d.update({'edit':html2})
			
		t = get_template("cv_view.html")
		c = Context(d)
		html = t.render(c)

		return HttpResponse(html)

######################################################################

######################################################################
#@csrf_exempt
def home(request):
	if request.method == "GET":
		list = Oferta.objects.all().order_by('-date')[0:20]
		n= Oferta.objects.all().count()
		m = n // 20
		if m > 25:
			m = 25
		st='<div class="btn-toolbar">'
		for i in range(m):
			if (i==0):
				
				st = st+'<div class="btn-group"><button style="background-color: CornflowerBlue;" type=submnt" onclick="fnt('
				st=st+"'"+str(i)+"'"
				st=st+');"> '+str(i*20+20)+' </button></div>'
			else:
				st = st+'<div class="btn-group"><button type=submnt" onclick="fnt('
				st=st+"'"+str(i)+"'"
				st=st+');"> '+str(i*20+20)+' </button></div>'
		m=st+'</div>'
		L=[]
		for i in list:
			obj = Oferta_View()
			obj.id= i.id
			obj.title= i.title
			obj.areal= i.area
			obj.type= i.type
			obj.firma= i.firma
			obj.date= i.date
			L.append(obj)
		d={'List':L, 'm':m}
		t = get_template("home.html")
		html = t.render(Context(d))
		return HttpResponse(html)
########################################################################################

@csrf_exempt
def next_page(request):
	if request.method == "POST":
		if (request.POST['sr']=='1'):
			titl='Organización'
			url='oferta_view'
			K=Oferta;
		else:
			K=CV;
			titl='Candidato'
			url='cv_view'
		stp=int(request.POST['pages'])

		fl_areal = False
		areal = request.POST['areal']
		if (areal != 'Argentina'):
			fl_areal = True

		fl_type = False
		tipo = request.POST['type']
		if (tipo != 'Cualquiera'):
			fl_type = True
		
		
		if (fl_areal == False):
			if (fl_type == False):
				list = K.objects.all().order_by('-date')[stp*20:stp*20+20]
				n= K.objects.all().count()

			else:
				list = K.objects.filter(type = tipo).order_by('date')[stp*20:stp*20+20]
				n= K.objects.filter(type = tipo.strip()).count()

		else:
			if (fl_type == False):
				list = K.objects.filter(area = areal).order_by('date')[stp*20:stp*20+20]
				n= K.objects.filter(area = areal).count()

			else:
				list = K.objects.filter(area = areal, type = tipo).order_by('date')[stp*20:stp*20+20]
				n= K.objects.filter(area = areal, type = tipo).count()
		
		

		if (request.POST['palabra_clave'] != 'Palabra clave...' or request.POST['palabra_clave'] == ''):

			search = request.POST['palabra_clave'].split()
			L=[]
			for i in list:
				for j in search:
					if request.POST['sr']==1:
						
						if ((i.title.lower().find(j.lower())>-1) or (i.Descripcion.lower().find(j.lower())>-1) or (i.Requisitos.lower().find(j.lower())>-1)):
							L.append(i)
							continue
					else:
						
						
						if i.title.lower().find(j.lower())>-1:
							L.append(i)
							continue
			list = L
			n = len(list)

		m = n // 20
		if m > 25:
			m = 25
		st='<div class="btn-toolbar">'
		for i in range(m):
			if (i==stp):
				
				st = st+'<div class="btn-group"><button style="background-color: CornflowerBlue;" type=submnt" onclick="fnt('
				st=st+"'"+str(i)+"'"
				st=st+');"> '+str(i*20+20)+' </button></div>'
			else:
				st = st+'<div class="btn-group"><button type=submnt" onclick="fnt('
				st=st+"'"+str(i)+"'"
				st=st+');"> '+str(i*20+20)+' </button></div>'
		m=st+'</div>'
		L=[]
		for i in list:
			obj = Oferta_View()
			obj.id= i.id
			obj.title= i.title
			obj.areal= i.area
			obj.type= i.type
			obj.firma= i.firma
			obj.date= i.date
			L.append(obj)
		d={'List':L, 'm':m, 'title': titl,'url':url}
		t = get_template("next_page.html")
		html = t.render(Context(d))
		return HttpResponse(html)
########################################################

