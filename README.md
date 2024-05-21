
# What is This
This script was coded in python (3.10) and is able to generate a csv file containing data that can be used to generate/test aws personalize e-commerce insights

# How does it works

To run the script just issue => python generate_personalize_csv.py

This will generate a file named data.csv containing records to be submited to personalize data set 

# CSV Example:
USER_ID,ITEM_ID,TIMESTAMP,EVENT_TYPE
2,8,1672550520,remove_from_cart
26,9,1672548420,add_to_cart
9,6,1672547880,view
4,4,1672549560,add_to_cart
12,3,1672547460,view
4,9,1672549500,remove_from_cart
13,7,1672548540,view
22,3,1672548420,view
3,4,1672549620,add_to_cart
18,4,1672548900,click
22,6,1672548960,view
25,10,1672550400,remove_from_cart
10,6,1672550640,add_to_cart
2,5,1672548360,click
10,10,1672548960,click

# Configuration
Data configuration, can be changed by editing #constants.py file