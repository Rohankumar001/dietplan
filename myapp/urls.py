from turtle import home
from django.shortcuts import *
from django.urls import path, include
from . import views 
from .views import *
from .views import user_register
from django.contrib.auth import views as auth_views
from .views import product_list
urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login'),
    path('search/', views.search_view, name='search'),
    path('user_login/', views.user_login, name='user_login'),
    path('user/register/', views.user_register, name='user_register'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin_add/', views.admin_add, name='admin_add'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('reoder/', views.reoder, name='reoder'),
    path('adminpageorder/', views.admin_order_view, name='adminorders'),
    path('adminordersiteam/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('userpageorder/', views.user_order_view, name='orders'),
    path('index', views.index, name='index'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_to_wishlist/<int:product_id>/', views.remove_to_wishlist, name='remove_to_wishlist'),
    path('dec_from_cart/<int:product_id>/', views.decrease_to_cart, name='decrease_quantity'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('view_to_wishlist/', views.view_to_wishlist, name='view_to_wishlist'),
    path('checkout/', views.checkout_view, name='checkout'),  
    path('order_summary/', views.order_summary_view, name='order_summary'),  
    # path('profile/update/', views.profile_update, name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    path('profile/update/', views.profile_update, name='profile_update'),
    path('update_status/<int:order_id>/', views.update_status, name='update_status'),
    path('order_list_and_detail/', views.order_list_and_detail, name='order_list_and_detail'),
    path('products/', products, name='products'),  
    path('home/', home, name='home'),
    
    
     path('prod/', product_list, name='product_list'),
     path('supplier_add/',views.supplier_add,name='supplier_add'),
     path('send_request/<int:product_id>/', views.send_request, name='send_request'),
     path('supplier/<int:id>',views.supplier_replay,name="supplier_replay"),
     path('supplier_replies/', views.supplier_replies, name='supplier_replies'),  # New URL pattern for supplier replies

     #path for dashboard
    path('diet/',views.diet_plan, name='diet_plan_form'),
    path('diet_plan_result/', views.diet_plan_result, name='diet_plan_result'),
    # path('diet-plan-form/', views.diet_plan_form, name='diet_plan_form'),
    path('add-health-record/', views.add_health_record, name='add_health_record'),
    path('progress-visualization/', views.progress_visualization, name='progress_visualization'),

 #for track order urls
    path('record/', views.record_data, name='record_data'),
    path('progress/', views.progress_visualization, name='progress_visualization'),
    path('generate_report/', views.report_generate, name='report_generate'),  # New path for report generation
    #chatbot
    path('chat/', chatbot_view, name='chatbot'), 
    path('weight_tracking/', weight_tracking_form_view, name='weight_tracking_form'),
    path('weight_tracking/results/', weight_tracking_results_view, name='weight_tracking_results'),
    #weekly process
   path('weight-tracking-results-all/', weight_tracking_result_entire, name='weight_tracking_results_all'),

   #  path('weight_tracking/', weight_tracking_view, name='weight_tracking'),]

   path('',views.welcome, name='welcome'),  # Root URL for the welcome page
   path('add_product', views.add_product, name='add_product'),
    
]
