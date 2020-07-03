from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import joblib
import sklearn
import base64
from io import BytesIO
from PIL import Image
import cv2
from keras import models

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

    # keras model
    model = models.load_model("./staticfiles/model_img_augmentation.h5")
    pred = gray/255
    
    pred = pred.reshape(1,28,28,1)
    
    keras_predict = np.argmax(model.predict(pred)[0])

    context ={ 'mytext' : url, 'data': keras_predict, 'data1': ans, 'logp' : model.predict(pred)[0] , 'prob' : proba }
    return render(request, "display.html", context)
  return HttpResponse("hey there! use post method instead")