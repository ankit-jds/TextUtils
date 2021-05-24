#I have created this file - Ankit Tamboli
from django.http import HttpResponse
#video:8 templates 
from django.shortcuts import render

def index(request):
	return render(request,'index.html')
	
def analysedtext(request):
	#Get the text by POST request
	djtext=request.POST.get('text','default')
	removepunc=request.POST.get('removepunc','off')
	newlineremove=request.POST.get('newlineremove','off')
	charcount=request.POST.get('charcount','off')
	extraspaceremove=request.POST.get('extraspaceremove','off')
	
	#Analyse the text
	analysed =djtext
	operations_done=[]
	if removepunc=='on':
		operations_done.append("Removed Punctuations")
		punctuations='''`|~!@#$%^&*()_/\-{}[]"';:<>,.?'''
		tmptext=""
		for i in analysed:		
			if i not in punctuations:
				tmptext+=i
		analysed=tmptext
		
	if extraspaceremove=='on':
		operations_done.append("Extra Space Removed")
		tmptext=""
		for i in range(len(analysed)):
			if analysed[i]!=" " or analysed[i-1]!=" " :
				tmptext+=analysed[i]
		analysed=tmptext
		
	if newlineremove=='on':
		operations_done.append("Newline Removed")
		tmptext=""
		for i in analysed:
			if i!='\n' and i!='\r':
				tmptext+=i
		analysed=tmptext
	
	if charcount=='on':
		operations_done.append("Removed Punctuations")
		count="The character count of text is : {}".format(len(djtext))
		
	params={"analysed_text":analysed, "operations_done":operations_done , "count":count}
	if len(operations_done)==0:
		return HttpResponse('<h1>ERROR#!</h1>')
	return render(request,'analysedtext.html',params)
	
	
def contactus(request):
	return (HttpResponse("Contact Us<a href='/'> Back </a>"))	
	
def about(request):
	return (HttpResponse("About<a href='/'> Back </a>"))

