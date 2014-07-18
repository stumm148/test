class model:
    def __init__(self):
        self.data = {'profession':'statybininkas', 'atlyginimas':'3000'}
    def info(self):
        return self.data

class controler:
    def __init__(self):
        self.model = model()
        self.view = view()
    def control_mvc(self):
        part = self.model.info()
        etc = self.view.tttt(part)
        #print self.view
        
class view:
    def tttt(self,part):
        print 'cia toks {0} tekstas {1}' .format(part['profession'],part['atlyginimas'])

if __name__ == '__main__':
    controler().control_mvc() 
