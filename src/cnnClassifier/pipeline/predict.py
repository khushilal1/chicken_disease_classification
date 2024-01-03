import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))
        # print(model)
        
        image_name=self.filename #loading the file path
        test_image=image.load_img(image_name,target_size=(224,224)) #resize iage
        test_image=image.img_to_array(test_image)#image into array
        test_image=np.expand_dims(test_image,axis=0) #column wisw
        result=np.argmax(model.predict(test_image),axis=1) #rowise
        print(result)



        if result[0]==1:
            prediction="Healthy"
            return [{"image":prediction}]
        else:
            prediction="COccidiosis"
            return [{'image':prediction}]