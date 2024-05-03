from os import listdir
from os.path import isfile,join



files = [f for f in listdir('/Users/shashank/Projects/Python practice/') if isfile(join('/Users/shashank/Projects/Python practice/',f))] 

print(files)

