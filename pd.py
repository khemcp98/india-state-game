import pandas

data_dict = {
    "States": ["uttar pradesh", "jammu & kashmir", "himachal pradesh", "panjab", "uttranchal", "haryana", "rajassthan",
               "gujrat", "maharastra", "goa", "karnataka", "kerala", "tamil nadu", "andhra pradesh", "orisa",
               "chhattisgadh", "madhya pradesh", "jharkhand", "bihar", "west bangal", "sikkim", "assam",
               "arunachal pradesh", "nagaland", "manipur", "mizoram", "tripura"],

    "x": [-31.0, -106.0, -88.0, -125.0, -43.0, -108.0, -152.0, -207.0, -126.0, -156.0, -120.0, -104.0, -49.0,
          -45.0, 66.0, 7.0, -80.0, 64.0, 80.0, 123.0, 129.0, 221.0, 244.0, 249.0, 243.0, 222.0, 198.0],

    "y": [110.0, 276.0, 215.0, 188.0, 178.0, 154.0, 94.0, 19.0, -57.0, -144.0, -159.0, -255.0, -220.0, -121.0, -41.0,
          -20.0, 15.0, 35.0, 74.0, 26.0, 120.0, 103.0, 150.0, 103.0, 73.0, 38.0, 43.0]
}

data = pandas.DataFrame(data_dict)
data.to_csv("states.csv")
