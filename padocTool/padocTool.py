import subprocess
import os

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
        # change to destionation
        os.chdir(dir)
        print ('Change dir to *' + dir + '*')
        # convert file
        for file in self.fileList:
            real = os.path.splitext(file)
            # convert our files now
            ret = subprocess.call(["pandoc","-s", "-S", file, "-o", real[0]+'.docx'], shell=True)
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
    file =  open('dir.txt','r')
    directory = file.readline().strip()
    print('get directory %s\n' %(directory))
    pan = PanTool('file.txt')
    pan.reader()
    pan.convert(directory)
