from django.shortcuts import render,redirect
from notesapp.models import document

def editor(request):
	docid=int(request.GET.get('docid',0))
	docum=document.objects.all()

	if request.method== 'POST':
		docid=int(request.POST.get('docid',0))
		title=request.POST.get('title')
		content=request.POST.get('content',' ')

		if docid>0:
			doc=document.objects.get(pk=docid)
			doc.title=title
			doc.content=content
			doc.save()

			return redirect('/?docid=%i' % docid)

		else:
			doc=document.objects.create(title=title,content=content)

			return redirect('/?docid=%i' % doc.id)

	if docid>0:
		doc=document.objects.get(pk=docid)
	else:
		doc=' '


	context = {
	'docid':docid,
	'docum':docum,
	'doc':doc
	}
	return render(request,'editor.html',context)

def delete_document(request,docid):
		doc=document.objects.get(pk=docid)
		doc.delete()
		return redirect('/?docid=0')
