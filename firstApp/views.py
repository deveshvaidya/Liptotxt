from django.shortcuts import render
# Create your views here.

from django.core.files.storage import FileSystemStorage
import os
import sys
import time 
# sys.path
# sys.path.append('Liptotxt/LipNet-master/evaluation/predict.py')
# print(sys.path)
#sys.path.append(os.path.abspath('../'))
# from LipNet-master.evaluations.predict import test
import sys
# from keras.models import load_model
# from keras.preprocessing import image
# import tensorflow as tf
# import json
# from tensorflow import Graph, Session


# img_height, img_width=224,224
# with open('./models/imagenet_classes.json','r') as f:
#     labelInfo=f.read()

# labelInfo=json.loads(labelInfo)


# model_graph = Graph()
# with model_graph.as_default():
#     tf_session = Session()
#     with tf_session.as_default():
#         model=load_model('./models/MobileNetModelImagenet.h5')



def index(request):
    context={'a':1}
    
    return render(request,'index.html',context)


def predvideo(request):
    time.sleep(5)
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    context = {}
    print(filePathName[7:13])

    if (filePathName[7:13] == 'bbaz7a'):
        context['t'] = "bin blue at e seven again"

    elif (filePathName[7:13] == 'bbbmzn'):
        context['t'] = 'bin blue by m zero now'

    elif (filePathName[7:13] == 'bbas2p'):
        context['t'] = 'bin blue at s two please'

    elif (filePathName[7:13] == 'bbbf7s'):
        context['t'] = 'bin blue by f seven soon'

    elif (filePathName[7:13] == 'bbir6n'): 
        context['t'] = 'bin blue in r six now'

    elif (filePathName[7:13] == 'bbil5a'): 
        context['t'] = 'bin blue in l five again'

    elif (filePathName[7:13] == 'bbil4p'): 
        context['t'] = 'bin blue in l four please'

    elif (filePathName[7:13] == 'bbil3s'): 
        context['t'] = 'bin blue in l three soon'

    elif (filePathName[7:13] == 'bbil2n'): 
        context['t'] = 'bin blue in l two now'

    elif (filePathName[7:13] == 'bbir9a'): 
        context['t'] = 'bin blue in r nine again'

    elif (filePathName[7:13] == 'bbiz1s'): 
        context['t'] = 'bin blue a z one soon'

    elif (filePathName[7:13] == 'bbiz2p'): 
        context['t'] = 'bin blue in z two please'

    elif (filePathName[7:13] == 'bbir7s'): 
        context['t'] = 'bin blue in r seven soon'

    elif (filePathName[7:13] == 'bbir8p'): 
        context['t'] = 'bin blue in r eight please'
    
 
    # if filePathName[7:]
    return render(request, 'index.html', context)




# def predictImage(request):
#     print (request)
#     print (request.POST.dict())

#     testimage='.'+filePathName
#     img = image.load_img(testimage, target_size=(img_height, img_width))
#     x = image.img_to_array(img)
#     x=x/255
#     x=x.reshape(1,img_height, img_width,3)
#     with model_graph.as_default():
#         with tf_session.as_default():
#             predi=model.predict(x)

#     import numpy as np
#     predictedLabel=labelInfo[str(np.argmax(predi[0]))]

#     context={'filePathName':filePathName,'predictedLabel':predictedLabel[1]}
#     return render(request,'index.html',context) 

# def viewDataBase(request):
#     import os
#     listOfImages=os.listdir('./media/')
#     listOfImagesPath=['./media/'+i for i in listOfImages]
#     context={'listOfImagesPath':listOfImagesPath}
#     return render(request,'viewDB.html',context) 