#  create by me
from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    # context = {'name':'aman'}
    return render(request ,'index.html')
    # return HttpResponse("hello")

def analyze(request):
    
    get_text = request.POST.get('text', 'default')

    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    new_line_remover = request.POST.get('newlineremove', 'off')
    space_remover = request.POST.get('spaceremove', 'off')
    
    if remove_punc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%*&_~^'''
        analyze_text = ""
        for char in get_text:
            if char not in punctuation:
                analyze_text = analyze_text + char
        context = {'purpose' : 'Removed Punctuation','analyzed_text' : analyze_text}
        get_text = analyze_text
        

    if full_caps == 'on':
        analyze_text = ""
        for char in get_text:
            analyze_text = analyze_text + char.upper()
        context = {'purpose' : 'changed to upper case','analyzed_text' : analyze_text}
        get_text = analyze_text
        
    
    if new_line_remover == 'on':
        analyze_text = ""
        for char in get_text:
            if char != "\n" and char != "\r":
                analyze_text = analyze_text + char
        context = {'purpose' : 'Remover New Line','analyzed_text' : analyze_text}
        get_text = analyze_text
        

    if space_remover == 'on':
        analyze_text = ""
        for  index, char in  enumerate(get_text):
            if not(get_text[index] == " " and get_text[index+1] == " "):
               analyze_text = analyze_text + char
        context = {'purpose' : 'Remover New Line','analyzed_text' : analyze_text}
        get_text = analyze_text
    
    
    return render(request,'analyze.html',context)

