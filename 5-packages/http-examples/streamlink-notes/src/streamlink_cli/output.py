import logging 
import os 

from .compat import stdout

log = logging.getLogger("streamlink.cli.output")


class Output(object):
    def __init__(self):
        self.opened = False 
    
    def open(self):
        self._open()
        self.opened = True 
    
    def close(self):
        if self.opened:
            self._close()
        
        self.opened = False 
    
    def write(self, data):
        if not self.opened:
            raise IOError("output is not opened")

        return self._write(data)
    
    def _open(self):
        pass 
    
    def _close(self):
        pass 
    
    def _write(self):
        pass 


class FileOutput(Output):
    def __init__(self, filename=None, fd=None, record=None):
        super(FileOutput, self).__init__()
        self.filename = filename 
        self.fd = fd 
        self.record = record 
    
    def _open(self):
        if self.filename:
            self.fd = open(self.filename, "wb")
        
        if self.record:
            self.record.open()
        
    def _close(self):
        if self.fd is not stdout:
            self.fd.close()
        if self.record:
            self.record.close()
    
    def _write(self, data):
        self.fd.write(data)
        if self.record:
            self.record.write(data)
        
