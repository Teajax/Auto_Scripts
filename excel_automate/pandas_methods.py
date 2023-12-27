import pandas as pd 

df=pd.read_csv("./dummy_car_details.csv",index_col=0)

#get headers
df_headers_columns=df.columns.values  #return type array 
print(df_headers_columns)
print(type(df_headers_columns))

df_headers_head=df.axes[1]  #returns horizondal- df.axes[1] and vertical- df.axes[0] 1st index 
print(df_headers_head.to_list())
print(type(df_headers_head))

df_headers_sort=sorted(df)  #get the output in the form of the list as well as in ascending order too
print(df_headers_sort)
print(type(df_headers_sort))

#filter data
#1]get data of only Maruti brands
maruti_data=df[(df['Brand']=="Maruti") | (df['Brand']=="Tata")]   
print(maruti_data)
print(maruti_data.shape)   #get the cell no 

#2]get unique brands
unique_brands=df['Brand'].unique()
print(unique_brands)

#3]names of the brand hyundai
hyundai_brand_names=df.loc[(df['Brand']=='Hyundai'),'name']
print(hyundai_brand_names)

#4]get rows 4-9 and column 3,4
fetch_rows=df.iloc[3:9,2:4]
print(fetch_rows)

def clean_price(num):
    units=["lakhs","crore"," "]
    new_prc=num
    for i in units:
        print(i)
        new_prc=new_prc.replace(i,"")
    return float(new_prc)

#new colums 
df['clean_price']=df["price"].apply(clean_price)
df['2%_discount']=df["clean_price"]*100000*0.2
print(df)












