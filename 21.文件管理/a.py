#encoding:utf8
import os
                
def maxSizeFile(dir_path):
    dic_max = {'size':0, 'path':None}
    for (root, dirs, files) in os.walk(dir_path):
        for filename in files:
            filePath = os.path.join(root,filename)
            size =  os.path.getsize(filePath)
            if size>dic_max['size']:
                dic_max['size'] = size
                dic_max['path'] = filePath
    print(dic_max)
    
def main():
    maxSizeFile(r'root')
    
if '__main__'==__name__:
    main()
    