from sklearn.neighbors import KNeighborsClassifier as knn
from random_forest import forest
import sklearn.metrics as met
from tree_models import fet_imp_plot
class knn_model(forest): # class to perform k-nearest neighbor algo
    def model(self):
        mod=knn(neighbors=self.n_est)
        return mod.fit(self.x,self.y)
    def class_report(self):
        return met.classification_report(self.yt,self.model().predict(self.xt))
    def features_imp(self):
        return self.model().features_importances_
    def conf_matrix(self):
        return met.confusion_matrix(self.yt,self.model().predict(self.xt))
def knn_entry(data,col1,col2,col3,testsize):
    x_val=col2.multiselect("Features",data.columns)
    y_val=col2.selectbox("Target",data.columns)
    tree_reg_type=col1.radio("models",['Decision Tree',"Random Forest"])
    nei=col2.slider("no of neighbors",1,1000)
    x_tr,x_te,y_tr,y_te=split_data(data[x_val],data[y_val],testsize).split_imp()
    col2.info("train set length: "+str(x_tr.shape[0]))
    col3.info("test set length: "+str(x_te.shape[0]))
    st.write("Training--->")
    progress=st.progress(0)
    for i in range(100):
        knn=knn_model(x_tr,y_tr,x_te,y_te,nei)
        time.sleep(0.01)
        progress.progress(i+1)
    fet_imp_plot(knn.features_imp())
    st.write(knn.class_report())
    st.write(knn.conf_matrix())
