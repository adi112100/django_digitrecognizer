from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import joblib
import sklearn
import base64
from io import BytesIO
from PIL import Image
import cv2

# Create your views here.

def index(request):
  clf = joblib.load('./staticfiles/finalized_model.sav')
  return render(request, "index2.html")

def result(request):
  if request.method =='POST':
    
    url = request.POST.get('url')
    offset = url.index(',')+1
    img_bytes = base64.b64decode(url[offset:])
    img = Image.open(BytesIO(img_bytes))
    img  = np.array(img)
    smaller = cv2.resize(img, (28, 28))
    gray = cv2.cvtColor(smaller, cv2.COLOR_BGR2GRAY)
    resize_gray = gray.reshape(1,-1) 
    clf = joblib.load('./staticfiles/finalized_model.sav')
    ans = clf.predict(resize_gray)
    log_proba = clf.predict_log_proba(resize_gray)
    proba = clf.predict_proba(resize_gray)

    context ={ 'mytext' : url, 'data': ans[0], 'logp' : log_proba, 'prob' : proba }
    return render(request, "display.html", context)
  return HttpResponse("hey there! use post method instead")