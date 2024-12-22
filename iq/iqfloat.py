import numpy
import sys

class IqFloat():
    filename = None
    data = None

    @staticmethod
    def check_format(filename):
        file_parts = filename.split('.')
        if file_parts[-1] == "float32":
            return
        else:
            print(f"Error: The file '{filename}' is no float32 file")
            sys.exit(1)


    def __init__(self, filename):
        IqFloat.check_format(filename)
        self.filename = filename
        try:
            self.data = numpy.fromfile(self.filename, dtype="float32")
            #self.iqdata = self.data[0::2] + 1j*self.data[1::2]
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
        pass


    def getIqData(self):
        iqdata = self.data[0::2] + 1j*self.data[1::2]
        return iqdata