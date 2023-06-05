import streamlit as st
import pandas as pd
import pickle


#Load Model
with open("model/SVC_clf.pickle", 'rb') as file:
    model = pickle.load(file)

