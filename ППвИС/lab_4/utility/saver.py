#Done (not verified(path))

import jsons

class Saver:
    def __init__(self, *objects,path = '/home/siarhei/Programming/IIT/Univer/ППвИС/lab_4/data'):
        
        with open(path+'/data.json','w') as write_file:
            write_file.write(jsons.dumps(objects, strip_nulls = True,
            strip_privates = True, strip_properties = True))

    def save_state(self, *objects,path = '/home/siarhei/Programming/IIT/Univer/ППвИС/lab_4/data'):
        with open(path+'/data.json','w') as write_file:
            write_file.write(jsons.dumps(objects, strip_nulls = True,
            strip_privates = True, strip_properties = True))
