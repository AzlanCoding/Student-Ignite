#https://ourcodeworld.com/articles/read/1347/how-to-detect-nudity-nudity-detection-nsfw-content-with-machine-learning-using-nudenet-in-python
# Example #1
# classification.py

# Import module
from nudenet import NudeClassifier
from pathlib import Path
import sys
import requests
import os
global classifier
classifier = NudeClassifier()
if not os.path.exists("./Cache"):
    os.mkdir("Cache")
class nudeDetect():
    def check(url):
        global classifier
        try:
            p = Path(url)
            #if is_downloadable(url):
            #requests.get(url, allow_redirects=True)
            try:
                r = requests.get(url, allow_redirects=True)  
                with open('./Cache/'+str(p.name), 'wb') as f:
                    f.write(r.content)
            except exception as e:
                print("cannot dl")
                print(e)
                return False #cannot dl so just skip
        except exception as e:
            print("failed to dl")
            print(e)
            try:
                os.remove('./Cache/'+str(p.name))
            except exception as e:
                print("failed to clear cache")
                print(e)
            return False
        try:
            # initialize classifier (downloads the checkpoint file automatically the first time)
            classifier = NudeClassifier()
            r = classifier.classify('./Cache/'+str(p.name))
            print(r)
            if r['./Cache/'+str(p.name)]['unsafe'] > 0.50:
                out = True # explicit
            else:
                out = False
        except excpetion as e:
            print("detector failed")
            print(e)
            try:
                os.remove('./Cache/'+str(p.name))
            except exception as e:
                print("failed to clear cache")
                print(e)
            return False
        os.remove('./Cache/'+str(p.name))
        return out
        

'''
imgs = sys.argv
import os
del imgs[0]
try:
    url = imgs[0]
    p = Path(url)
    if is_downloadable(url):
        #requests.get(url, allow_redirects=True)
        r = requests.get(url, allow_redirects=True)  
        with open('./Cache/'+str(p.name), 'wb') as f:
            f.write(r.content)
except:
    os._exit(0)
try:
    # initialize classifier (downloads the checkpoint file automatically the first time)
    classifier = NudeClassifier()
    r = requests.get(sys.argv[1], allow_redirects=True)
    r = classifier.classify(img)
    if r[str(p.name)]['unsafe'] > 0.50:
        out = True # explicit
    else:
        out = False
    return out
except:
    os._exit(0)
''''''
# A. Classify single image
print(classifier.classify('./image1.jpg'))

# This would print something like:
# {
#   './image1.jpg': {
#      'safe': 0.00015856953, 
#      'unsafe': 0.99984145
#   }
# }

# B. Classify multiple images
# Returns {'path_to_image_1': {'safe': PROBABILITY, 'unsafe': PROBABILITY}}
# Classify multiple images (batch prediction)
# batch_size is optional; defaults to 4
print(
    classifier.classify(
        ['./image1.jpg', './image2.jpg', './image3.jpg', './image4.jpg'],
        batch_size=4
    )
)

# {
#    './image1.jpg': {
#         'safe': 0.00015856922, 
#         'unsafe': 0.99984145
#     },
#     './image2.jpg': {
#         'safe': 0.019551795, 
#         'unsafe': 0.9804482
#     },
#    './image3.jpg': {
#         'safe': 0.00052562816,
#         'unsafe': 0.99947435
#    }, 
#    './image4.jpg': {
#         'safe': 3.3454136e-05,
#         'unsafe': 0.9999665
#    }
# }
'''
