from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('change-pass', views.ChangePasswordPage.as_view(), name='change_password_page'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
]
