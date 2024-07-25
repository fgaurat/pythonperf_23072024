#!/usr/bin/env python
from contextlib import contextmanager

class FileManager:
    def __init__(self,filename,mode) -> None:
        self.filename=filename
        self.mode=mode
        self.thefile = None
    
    def __enter__(self):
        self.thefile = open(self.filename,self.mode)
        return self.thefile

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.thefile:
            self.thefile.close()

@contextmanager
def file_manager(filename,mode):
    try:
        file = open(filename,mode)
        print("avant yield")
        yield file
        print("après yield")
    finally:
        file.close()


def main():
    # try:
    #     with open("lefichier.txt",'w') as f:
    #         f.write('Hello\n')
    #         a = 2/0

    # finally:
    #     print("closed?",f.closed)
    # f.close()
    # print(f.closed)
    
    with FileManager("lefichier2.txt",'w') as f:
        f.write('Hello\n')

    print("start file_manager")    
    with file_manager("lefichier2.txt",'w') as f:
        print("start write")    
        f.write('Hello\n')
        print("end write")    
    print("end file_manager")    

if __name__ == '__main__':
    main()