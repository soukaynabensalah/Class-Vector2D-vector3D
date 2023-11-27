class vecteur2D :
    nvb = 0
    def __init__(self,x = 0,y = 0):
        self.__x = x
        self.__y = y
        vecteur2D.nvb += 1

    def get_x(self) :
        return self.__x
        
    def set_x(self,x) :
        self.__x = x

    def get_y(self) :
        return self.__y
        
    def set_y(self,y) :
        self.__y = y

    def Tostring (self) :
        return ("x = ", str(self.__x) " y = ",str(self.__y)

    def Equals(self) :
        if self.__x == self.__y :
            return True
        
    def Norm(self) :
        return (self.__x **2 + self.__y **2) * 1/2
        
    class Vecteur3D (Vecteur2D) :
        def __init__(self,z = 0) :
            self.z = z
 
    def Tostring (self) :
        return "x = ",str(self.x) ," y = ",str(self.y) , " z = ", str(self.z)

    def Equals(self) :
        if self.x == self.y == self.z :
            return True
        
    def Norm(self) :
        return (self.__x ** 2 + self.__y ** 2 + self.z ** 2) * 1/2
      

        
        
         

        
        
        


    
        
