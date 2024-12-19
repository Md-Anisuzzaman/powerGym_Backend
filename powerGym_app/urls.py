
from django.urls import path,include
# from powerGym_Backend.powerGym_app.membersViews import *
from .views.membersViews import *
from .views.membersActivityView import *
from powerGym_app.views.trainerActivityView import *

urlpatterns = [
    # path('members/', MemberListView.as_view(), name='allmemberslists'),
    path('members/', MemberListView.as_view(),name='allmemberslists'),
    path('members/<int:pk>', MemberDeatilsView.as_view(), name='memberlist-and-update-and-delete'),
    path('register/', MemberRegistrationView.as_view(), name='user_registration'),
    path('members-activity/', MembersActivityView.as_view(), name='membersActivityLists'),
    path('members-activity/<int:pk>', MemberActivityDeatilsView.as_view(), name='membersActivityLists'),
    path('members-activity/<int:pk>', MemberActivityDeatilsView.as_view(), name='membersActivitydetails'),
    path('trainers-activity/', TrainerActivityLists.as_view(), name='trainersActivityLists'),
    path('trainers-activity/<int:pk>', TrainerActivityDetails.as_view(), name='trainersActivityLists'),
]
 