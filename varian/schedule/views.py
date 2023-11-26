from django.shortcuts import render

treatments = {
    "Craniospinal": {
        "machines": [1, 2],
        "fraction_opts": [13, 17, 20, 30],
        "avg_fraction_time": 30,
        "chance": 1
    },
    "Breast": {
        "machines": [1, 2, 3, 4, 5],
        "fraction_opts": [15, 19, 25, 30],
        "avg_fraction_time": 12,
        "chance": 25
    },
    "Special_Breast": {
        "machines": [1, 2],
        "fraction_opts": [15, 19, 25, 30],
        "avg_fraction_time": 20,
        "chance": 5
    },
    "Head+Neck": {
        "machines": [1, 2, 3, 4],
        "fraction_opts": [5, 10, 15, 25, 30, 33, 35],
        "avg_fraction_time": 12,
        "chance": 10
    },
    "Abdomen": {
        "machines": [1, 2, 3, 4],
        "fraction_opts": [1, 3, 5, 8, 10, 12, 15, 18, 20, 30],
        "avg_fraction_time": 12,
        "chance": 10
    },
    "Pelvis": {
        "machines": [1, 2, 3, 4],
        "fraction_opts": [1, 3, 5, 10, 15, 22, 23, 25, 28, 35],
        "avg_fraction_time": 12,
        "chance": 18
    },
    "Crane": {
        "machines": [1, 2, 3, 4],
        "fraction_opts": [1, 5, 10, 13, 25, 30],
        "avg_fraction_time": 10,
        "chance": 4
    },
    "Lung": {
        "machines": [1, 2, 3, 4],
        "fraction_opts": [1, 5, 10, 15, 20, 25, 30, 33],
        "avg_fraction_time": 12,
        "chance": 12
    },
    "Special_Lung": {
        "machines": [1, 2, 3, 4],
        "fraction_opts": [3, 5, 8],
        "avg_fraction_time": 15,
        "chance": 5
    },
    "Brain": {
        "machines": [3, 4, 5],
        "fraction_opts": [5, 10, 12],
        "avg_fraction_time": 10,
        "chance": 10
    },
}
# Create your views here.
