
from yapf.yapflib.yapf_api import FormatCode

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler , OneHotEncoder , PowerTransformer
 
from sklearn.tree import DecisionTreeClassifier

import pickle
import warnings
warnings.filterwarnings("ignore")




#version 3 

def apply_preprocessing(raw_df, is_training=False):
    
        #X_train Feature Matrix  and  #y_train Target Variable
        X = raw_df.iloc[: , :-1]
        y = raw_df.iloc[ :, -1:] 
    
        #Separate numerical , and categorical variables 
        X_numeric_data = X.select_dtypes(include=[np.number])
        X_categorical_data = X.select_dtypes(exclude=[np.number])
        
        y.reset_index(drop=True, inplace=True)
        y = y.astype('int')
            
            
        if is_training:
         
        
                 #PowerTransformer on numerical variables 
            power = PowerTransformer()
            power.fit(X_numeric_data)

                #OneHotEncoder on categoricals  variables 
            encoder = OneHotEncoder(sparse=False, drop=None)
            encoder.fit(X_categorical_data)

            
                # Save/serialize the fitted encoder to local OS
            with open('pickle/OneHotEncoder.pkl', 'wb') as output_file:
                pickle.dump(encoder, output_file)

                # Save/serialize the fitted encoder to local OS
            with open('pickle/PowerTransformer.pkl', 'wb') as output_file:
                pickle.dump(power, output_file)
            
        else:

           
                # Load the fitted labelencoder from local OS
            with open('pickle/OneHotEncoder.pkl', 'rb') as input_file:
                encoder = pickle.load(input_file)


                # Load the fitted transformer from local OS
            with open('pickle/PowerTransformer.pkl', 'rb') as input_file:
                transformer = pickle.load(input_file)
            
            
                X_numeric_data = transformer.transform(X_numeric_data)
                X_categorical_data =encoder.transform(X_categorical_data)

        
        #Separate numerical , and categorical variables 
            
        #Dataframe
        X_numeric_data = pd.DataFrame(X_numeric_data)
        X_categorical_data = pd.DataFrame(X_categorical_data)
        
        #mege  
        pp_X = pd.merge(left=X_numeric_data, right=X_categorical_data, how='inner',left_index=True, right_index=True)
            
           
        return pp_X , y
        

def apply_preprocessing_V2(raw_df, is_training=False):
    
        #X_train Feature Matrix  and  #y_train Target Variable
        X, y = raw_df.drop(columns='Drug'), raw_df['Drug'] 
    
        #Separate numerical , and categorical variables 
        X_numeric_data = X.select_dtypes(include=[np.number])
        X_categorical_data = X.select_dtypes(exclude=[np.number])
        
        y.reset_index(drop=True, inplace=True)
        y = y.astype('int')
            
            
        if is_training:

    # scaler, encoder, transform
          # 1) fit and  2) tranform
        
                 #PowerTransformer on numerical variables 
            power = PowerTransformer()
            X_numeric_data = power.fit_transform(X_numeric_data)

                    #OneHotEncoder on categoricals  variables 
            encoder = OneHotEncoder(sparse=False, drop=None)
            X_categorical_data = encoder.fit_transform(X_categorical_data)

            # 3) save
                # Save/serialize the fitted encoder to local OS
            with open('pickle/OneHotEncoder.pkl', 'wb') as output_file:
                pickle.dump(encoder, output_file)

                # Save/serialize the fitted encoder to local OS
            with open('pickle/PowerTransformer.pkl', 'wb') as output_file:
                pickle.dump(power, output_file)
            
        else:

            # 1) load
                # Load the fitted labelencoder from local OS
            with open('pickle/OneHotEncoder.pkl', 'rb') as input_file:
                encoder = pickle.load(input_file)


                # Load the fitted labelencoder from local OS
            with open('pickle/PowerTransformer.pkl', 'rb') as input_file:
                transformer = pickle.load(input_file)
            
            
            X_numeric_data = transformer.transform(X_numeric_data)
            X_categorical_data =encoder.transform(X_categorical_data)
        # 2) transform
        
            #Separate numerical , and categorical variables 
            
        #Dataframe
        X_numeric_data = pd.DataFrame(X_numeric_data, 
                                      #columns=X_numeric_data.columns
                                     )
        X_categorical_data = pd.DataFrame(X_categorical_data,
                                          #columns=encoder.get_feature_names_out()
                                         )
        
        #mege  
        pp_X = pd.merge(left=X_numeric_data, right=X_categorical_data, how='inner',left_index=True, right_index=True)
            
           
        return pp_X , y
