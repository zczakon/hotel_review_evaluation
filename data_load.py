import pandas as pd
import numpy as np


def load_hotel_reviews():
    data = pd.read_csv("tripadvisor_hotel_reviews.csv", encoding="ISO-8859-1")
    return data

data = load_hotel_reviews().to_numpy()

# this will be 5 cluster classification problem, after that we will try to find rationales in those reviews.
# [number of review, review, rating /5]

