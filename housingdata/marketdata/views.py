from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import HouseDataPoint, HousingQueryData, ListOfCities
from .charts import Number_Of_Listings_Today, Get_Trend_Overtime, Get_Min_Overtime, Get_Bar_Overtime, Get_Max_Overtime, Get_Mean_Overtime, Get_Count_Overtime


def index(request):
    data_table_values = HouseDataPoint.objects.all()
    context = {
    'table_values':data_table_values,
    }

    return render(request,'marketdata/dashboard.html',context)

def TodaysChart(request):
    returned_data = Number_Of_Listings_Today()
    context = {
    'chart_html':returned_data['chart_html_content'],
    'table_values':returned_data['data_table_values'],
    }
    return render(request,'marketdata/Number_Of_Listings_Today_Chart.html',context)

def TrendOvertimeChart(request):
    returned_data = Get_Trend_Overtime()
    context = {
    'chart_html':returned_data['chart_html_content'],
    'table_values':returned_data['data_table_values'],
    }
    return render(request,'marketdata/Trend_Overtime_Chart.html',context)

def BarOvertimeChart(request):
    returned_data = Get_Bar_Overtime()
    context = {
    'chart_html':returned_data['chart_html_content']
    }
    return render(request,'marketdata/Bar_Overtime_Chart.html',context)


def MinOvertimeChart(request):
    returned_data = Get_Min_Overtime()
    context = {
    'chart_html':returned_data['chart_html_content']
    }
    return render(request,'marketdata/Min_Overtime_Chart.html',context)

def MaxOvertimeChart(request):
    returned_data = Get_Max_Overtime()
    context = {
    'chart_html':returned_data['chart_html_content']
    }
    return render(request,'marketdata/Max_Overtime_Chart.html',context)

def MeanOvertimeChart(request):
    returned_data = Get_Mean_Overtime()
    context = {
    'chart_html':returned_data['chart_html_content']
    }
    return render(request,'marketdata/Mean_Overtime_Chart.html',context)

def CountOvertimeChart(request):
    returned_data = Get_Count_Overtime()
    context = {
    'chart_html':returned_data['chart_html_content']
    }
    return render(request,'marketdata/Count_Overtime_Chart.html',context)