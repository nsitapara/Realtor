from plotly.offline import download_plotlyjs, plot
import plotly.graph_objs as go
from .models import HouseDataPoint, HousingQueryData, ListOfCities
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import numpy as np



# https://www.codingwithricky.com/2019/08/28/easy-django-plotly/
# https://plotly.com/python/creating-and-updating-figures/
# https://plotly.com/python/reference/
def Number_Of_Listings_Today():
    condition_to_test = str(HousingQueryData.objects.last().datetime).split(":")[0]
    city = []
    total_records = []
    data_table_values = []
    for x in HousingQueryData.objects.all():   
        current_value = str(x.datetime).split(":")[0]
        if condition_to_test == current_value:
            # print(x.city)
            city.append(x.city)
            # print(x.datetime)
            datetime_str = str(x.datetime)
            datetime_str_split = datetime_str.split(" ")[-1].split(".")[0]
            # print(datetime_str_split)
            # print(x.total_records)
            total_records.append(x.total_records)
            data_table_values.append(x)
    bar_chart = go.Bar(x=city, y=total_records,text=total_records,textposition='auto')
    fig = go.Figure(
        data = bar_chart,
        layout = go.Layout(
            # height = 900,
            # width = 1800,
            title = "Number Of Listings Today",)
        )
    
    # (height=600, width=800)
    html_to_return = fig.to_html()
    context = {
    'chart_html_content':html_to_return,
    'data_table_values':data_table_values,
    }
    # html_to_return = plot(fig, output_type='div')

    # print(html_to_return)
    return (context)

def Get_Trend_Overtime():
    query_all = HousingQueryData.objects.all()
    print(query_all)
    df = pd.DataFrame(query_all.values())
    df["date"] = df["datetime"].apply(lambda x:str(x).split(" ")[0])
    fig = px.line(df, x="date", y="total_records", color='city',text="total_records",title="Trend Overtime")
    html_to_return = fig.to_html()
    context = {
    'chart_html_content':html_to_return,
    'data_table_values':query_all,
    }
    # html_to_return = plot(fig, output_type='div')

    # print(html_to_return)
    return (context)


def Make_SQL_Query():
    table_names = ["marketdata_housedatapoint", "marketdata_housingquerydata","marketdata_listofcities"]
    create_statement = "mysql+pymysql://root:kajal2131@zion.usbx.me:11815/housingdata"
    engine = create_engine(create_statement)

    max_price = 3000000
    sql_statement = f"""select * 
    from marketdata_housingquerydata mh 
    join marketdata_housedatapoint mhp on  mh.query_id  = mhp.link_id 
    where mhp.prop_type not in ('mobile', 'land') and
    price < {max_price} and
    query_id > 8 
    """
    joined_table_sql = pd.read_sql(sql_statement,engine)
    joined_table_sql["date"] = joined_table_sql["datetime"].apply(lambda x : str(x).split(' ')[0] )
    sub_table = joined_table_sql[['date','city','query_id', 'line', 'postal_code',
        'state_code', 'state', 'county','prop_type', 'prop_status', 'price', 'baths_full', 'baths', 'beds',
        'size', 'units', 'lot_size', 'lot_size_units', 'presentation_status', 'price_change',
        'is_new_listing']]
    sub_table = sub_table.loc[:, ~sub_table.columns.duplicated()]
    sub_table["prop_type"].unique()
    grouped_data = sub_table[["date","city","price"]].groupby(by=['date','city']).agg({"price" : [np.min,np.mean,np.max]})
    grouped_data['count'] = sub_table[["date","city","price"]].groupby(by=['date','city']).count()
    grouped_data.reset_index(inplace=True)
    flatend_table = pd.DataFrame(grouped_data.to_records())
    flatend_table.rename({"('date', '')": 'date',
                        "('city', '')": 'city',
                        "('price', 'amin')": 'min',
                        "('price', 'mean')": 'mean',
                        "('price', 'amax')": 'max',
                        "('count', '')": 'count'}, axis=1,inplace=True)
    flatend_table = flatend_table[["date","city","min","mean","max",'count']]
    to_plotly = sub_table[["date","city","price"]]
    print("Returning Data for Next Method to Plot")
    return(to_plotly,flatend_table)

def Get_Bar_Overtime():
    data = Make_SQL_Query()
    plotting_data = data[0]
    fig = px.box(plotting_data, x="date", y="price",color='city')
    html_to_return = fig.to_html()
    context = {
    'chart_html_content':html_to_return
    }
    return (context)

def Get_Min_Overtime():
    data = Make_SQL_Query()
    plotting_data = data[1]
    fig = px.line(plotting_data, x="date", y="min", color="city")
    html_to_return = fig.to_html()
    context = {
    'chart_html_content':html_to_return
    }
    return (context)
    
def Get_Mean_Overtime():
    data = Make_SQL_Query()
    plotting_data = data[1]
    fig = px.line(plotting_data, x="date", y="mean", color="city")
    html_to_return = fig.to_html()
    context = {
    'chart_html_content':html_to_return
    }
    return (context)

def Get_Max_Overtime():
    data = Make_SQL_Query()
    plotting_data = data[1]
    fig = px.line(plotting_data, x="date", y="max", color="city")
    html_to_return = fig.to_html()
    context = {
    'chart_html_content':html_to_return
    }
    return (context)


def Get_Count_Overtime():
    data = Make_SQL_Query()
    plotting_data = data[1]
    fig = px.line(plotting_data, x="date", y="count", color="city")
    html_to_return = fig.to_html()
    context = {
    'chart_html_content':html_to_return
    }
    return (context)