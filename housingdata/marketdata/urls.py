from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('Number_Of_Listings_Today_Chart.html', views.TodaysChart, name='TodaysChart'),
#     path('Trend_Overtime_Chart.html', views.TrendOvertimeChart, name='TrendOvertimeChart'),
# ]

urlpatterns = [
    path('', views.TodaysChart, name='TodaysChart'),
    path('Number_Of_Listings_Today_Chart.html', views.TodaysChart, name='TodaysChart'),
    path('Trend_Overtime_Chart.html', views.TrendOvertimeChart, name='TrendOvertimeChart'),
    path('Min_Overtime_Chart.html', views.MinOvertimeChart, name='MinOvertimeChart'),
    path('Max_Overtime_Chart.html', views.MaxOvertimeChart, name='MaxOvertimeChart'),
    path('Mean_Overtime_Chart.html', views.MeanOvertimeChart, name='MeanOvertimeChart'),
    path('Bar_Overtime_Chart.html', views.BarOvertimeChart, name='BarOvertimeChart'),
    path('Count_Overtime_Chart.html', views.CountOvertimeChart, name='CountOvertimeChart'),
]