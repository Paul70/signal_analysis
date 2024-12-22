import sys
import RsWaveform

class IqTar():
    iqtar = None

    @staticmethod
    def check_format(filename):
        file_parts = filename.split('.')
        if "iq" in file_parts and "tar" in file_parts and file_parts[-1] == "tar":
            return
        else:
            print(f"Error: The file '{filename}' is no iq tar file")
            sys.exit(1)
    
    def __init__(self, filename):
        IqTar.check_format(filename)
        try:
            self.iqtar = RsWaveform.IqTar(file=filename)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
        pass

    def getSampleRate(self):
        return self.iqtar.meta[0]["clock"]
    
    def getNofSamples(self):
        return len(self.iqtar.data[0])
    
    def getData(self):
        return self.iqtar.data[0]
    

