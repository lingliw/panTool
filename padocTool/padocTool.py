import subprocess
import os
from docPreProcessing import replaceInclude
service_folders = ["app-service-web","automation","HDInsight","media-services","redis-cache","traffic-manager","virtual-network"]

class PanTool(object):
    def __init__(self, filePath):
        self.filePath = filePath
        self.fileList = []
        
    def reader(self):
        with open(self.filePath, 'r') as source:
            for fileName in source:
                if fileName.strip() != '':
                    self.fileList.append(fileName.strip())

        # return self.fileList

    def convert(self, dir):
        errmsg = '\nError files:\n'
        oldmsg = errmsg
        # convert file
        os.chdir("input/"+dir)
        for file in self.fileList:
            real = os.path.splitext(file)
            # convert our files now
            replaceInclude(dir,file)
            ret = subprocess.call(["pandoc","-s", "-S", file, "-o", "../../../output/"+dir+"/"+real[0]+'.docx'], shell=True)
            if ret == 0:
                continue
            else:
                errmsg += file
                errmsg += '\n'
        if oldmsg == errmsg:
            errmsg = "Convert all files success"
        
        print errmsg

if __name__ == '__main__':
    # open dir.txt to get directory
    for folder in service_folders:
        current_dir = os.getcwd()
        print('get directory %s\n' %(folder))
        pan = PanTool(folder+'.txt')
        pan.reader()
        pan.convert("articles/"+folder)
        os.chdir(current_dir)
