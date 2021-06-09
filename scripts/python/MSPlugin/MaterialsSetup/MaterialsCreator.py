from ..Utilities.SingletonBase import Singleton
import inspect

class MaterialsCreator(metaclass = Singleton):
#    __metaclass__ = Singleton
    def __init__(self):
        self.materialMap = {}

    def registerMaterial(self, rendererName, materialType, materialCreator):
        if rendererName not in self.materialMap:
            self.materialMap[rendererName] = {materialType : materialCreator}

        else:
            self.materialMap[rendererName].update({materialType:materialCreator})
        

    def createMaterial(self, rendererName, materialType, assetData, importParams, importOptions):
        return self.materialMap[rendererName][materialType](assetData,importParams, importOptions)


# Metaclass implementation that ensures implementation of a creator function
class MaterialsBase:
    def __init__(self):
        pass





