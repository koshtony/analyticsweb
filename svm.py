from dec_tree import tree_class
from sklearn.svm import SVC
from sklearn import metrics
class svm_mod(tree_class): # support vector machine
    def __init__(self,x,y,xt,yt,kernel,c): # inherit from class forest
        super().__init__(x,y,xt,yt)
        self.kernel=kernel
        self.c=c
    def __imp__(self): # training the model sklearn
        return SVC(C=self.c,kernel=self.kernel).fit(self.x,self.y)
    def __eval__(self): # model evaluation
        pred= self.__imp__().predict(self.xt)
        res_dict ={"accuracy":metrics.accuracy_score(self.yt,pred),
        "precision":metrics.precision_score(self.yt,pred,average="micro"),
        "Recall":metrics.recall_score(self.yt,pred,average="micro"),
        }
        return res_dict
