# I have created this file --> Anup
from string import punctuation

from django.http import HttpResponse
from django.shortcuts import render
import string

#The request object contains information about the incoming HTTP request
#--------------------------------
def index(request):
    # return HttpResponse('''<h1>Hello</h1> <a href="https://www.youtube.com/">Django code with harry</a> ''')
    params = {"name":"Anup",
             "place":"Dubai"}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')

#--------------------------------
def about(request):
    return HttpResponse("Hello Anup")

#----------------------------------
def text(request):
    file_path = "C:/Users/javal/PycharmProjects/textutils/txt1"
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return HttpResponse(content, content_type="text/plain")
    except FileNotFoundError:
        return HttpResponse("File not found!", status=404)

#----------------------------------
def removepunc(request):
    # request.GET is a querydict(python dict) it holds all query parameters
    # .get("text") extracts a simgle value from request.GET()
    djtext = request.GET.get("text", "default")
    print(djtext)
    return HttpResponse("remove punc")

#----------------------------------

def capfirst(request):
    return HttpResponse("capitalize first")

#----------------------------------
def newlineremove(request):
    return HttpResponse("newline remover")

#----------------------------------
def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back<a/>")

#----------------------------------
def charcount(request):
    return HttpResponse("charcount")

#----------------------------------

# def analyze(request):
#     djtext = request.GET.get("text", "default")
#     djcheck = request.GET.get("check", "off")
#     analyzed = djtext
#     params= {'purpose': 'Remove Punctuations',
#              'analyzed_text':analyzed}
#     return render(request, 'analyze.html', params)

def analyze(request):
    # POST sends data in request body not in urls
    djtext = request.POST.get("text", "default")
    djcheckpunct = request.POST.get("checkpunct", "off")
    djfullcaps = request.POST.get("fullcaps", 'off')
    djchecknlr = request.POST.get("checknlr", "off")
    djcheckesr = request.POST.get("checkesr", "off")
    djcheckcount = request.POST.get("checkcount", "off")
    # analyzed = ''
    params = {"target" : "ERROR",
              'purpose': 'Please Select Atleast One option'}
    punct = []
    for i in string.punctuation:
        punct.append(i)

    if djcheckpunct == "on":
        analyzed = ''
        for char in djtext:
            if char not in punct:
                analyzed+=char
        params = {"target" : "Your Anlalyzed Text",
                  'purpose': 'Remove Punctuations',
                          'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if djfullcaps == "on":
        analyzed = ''
        analyzed = djtext.upper()
        params = {"target" : "Your Anlalyzed Text",
                  'purpose': 'Change to Uppercase ',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if djchecknlr == "on":
        analyzed = ''
        for char in djtext:
            if char == "\n" and char == "\r":
                continue
            else:
                analyzed+=char
        params = {"target" : "Your Anlalyzed Text",
                  'purpose': 'Newline Remover ',
                  'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if djcheckesr == "on":
        analyzed = ''
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                continue
            else:
                analyzed+=char
        params = {"target" : "Your Anlalyzed Text",
                  "purpose" : "Extraspace Remover",
                  "analyzed_text": analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if djcheckcount == "on":
        count = 0
        for char in djtext:
            count+=1
        params = {"target" : "Your Anlalyzed Text",
                  "purpose":"Character Counter",
                  "analyzed_text":djtext,
                  "char_count": count}

        # return render(request, "analyze.html", params)

    return render(request, "analyze.html", params)

