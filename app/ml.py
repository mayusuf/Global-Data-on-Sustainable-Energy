# Import python libraries
import pickle
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

# Import user modules
from functions import cleanOperation, cleankSymbol, cleanDuration, preprocess

def ml():

    st.image('images/access_elect_2020.png')
    st.title("Model to predict CO2 Emissions")

    # loading the model
    models_path = 'models/'
    model_name = models_path + 'model_value_co2_emissions_kt_by_country.pkl'
    loaded_model = pickle.load(open(model_name, 'rb'))

    # loading the scaler
    transformers_path = 'transformers/'
    transformer_name = transformers_path + 'scaler_value_co2_emissions_kt_by_countryscaler.pkl'
    loaded_transformer = pickle.load(open(transformer_name, 'rb'))

    # loading the encoder
    # encoders_path = 'encoders/'
    # encoder_name = encoders_path + 'one_hot_encoder.pkl'
    # loaded_encoder = pickle.load(open(encoder_name, 'rb'))

    # Lists of accptable values
    # valid_types = ['PRIJEM', 'VYDAJ', 'VYBER']
    # valid_operation = ['PREVOD Z UCTU', 'VKLAD', 'VYBER', 'PREVOD NA UCET','VYBER KARTOU']
    # valid_ksymbol = ['UROK', 'SIPO', 'SLUZBY']
    # valid_duration = ['12', '24', '36', '48', '60']

    # Get input values.
    # type = st.selectbox("Please enter the type of transaction: ",valid_types, key = '2')
    # operation = st.selectbox("Please enter the operation: ",valid_operation, key = '3')
    fossil = st.number_input("Please enter the electricity from fossil fuels(twh): ")
    nuclear = st.number_input("Please enter the electricity from nuclear(twh): ")
    # k_symbol = st.selectbox("Please enter the k_symbol: ",valid_ksymbol, key = '4')
    renewables = st.number_input("Please enter the electricity from renewables(twh): ")
    # duration = st.radio("Please enter the loan duration: ",valid_duration, key = '5')
    land_areakm2 = st.number_input("Please enter the land area in km2: ")

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Get Your Prediction"):

        X = pd.DataFrame({
                      'electricity_from_fossil_fuels_twh':[fossil],
                      'electricity_from_nuclear_twh':[nuclear],
                      'electricity_from_renewables_twh':[renewables],
                      'land_areakm2':[land_areakm2]
                     })

        # X = preprocess(X)
        # numerical = X.select_dtypes(include = np.number)
        # categorical = X.select_dtypes(include = np.object)

        # cat_transformed = loaded_encoder.transform(categorical)
        # col_names = ['type_VYDAJ','type_VYBER','operation_vklad','operation_unknown','operation_vyber','k_symbol_UROK',
        #          'k_symbol_SIPO','k_symbol_SLUZBY','k_symbol_POJISTNE','duration_12','duration_36','duration_other']
        # categorical = pd.DataFrame(cat_transformed.toarray(), columns = col_names)

        # Joning dataframes
        # X = pd.concat([numerical, categorical], axis=1)
        # Scaling data
        X_scaled = loaded_transformer.transform(X)
        X_scaled_df = pd.DataFrame(X_scaled, columns = X.columns)

        # Making predictions
        prediction = loaded_model.predict(X_scaled_df)
        # prediction_probs = loaded_model.predict_proba(X_scaled_df)

        # st.success(prediction)
        
        st.success("The model predicts value of CO2 emissions(kt) is {:.2f}".format(prediction[0]))
        
