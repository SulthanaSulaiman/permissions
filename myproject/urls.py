"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from accounts import views as accounts_views
from permissions import views

urlpatterns = [
    url(r'^art_proof/(?P<pk>\d+)/$', views.generate_art_proof, name='generate_art_proof'),
    url(r'^$', views.BookListView.as_view(), name='home'),
    url(r'^books$', views.BookListView.as_view(), name='home'),
    url(r'^books/search$', views.book_search, name='book_search'),
    url(r'^contacts$', views.ContactListView.as_view(), name='contacts'),
    url(r'^contacts/new/$', views.NewContactView.as_view(), name='new_contact'),
    url(r'^contacts/(?P<contact_pk>\d+)/edit/$', views.ContactUpdateView.as_view(), name='edit_contact'),
    url(r'^contacts/(?P<pk>\d+)/deactivate/$', views.deactivate_contact, name='deactivate_contact'),
    url(r'^contacts/(?P<pk>\d+)/activate/$', views.activate_contact, name='activate_contact'),
    url(r'^contacts/inactive$', views.ContactListInactiveView.as_view(), name='contact_inactive'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^books/(?P<pk>\d+)/process_images/$', views.process_images, name='process_images'),
    url(r'^books/(?P<pk>\d+)/process_data/$', views.process_data, name='process_data'),
    url(r'^books/import_contacts/$', views.import_contact, name='import_contact'),  
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),   
    url(r'^books/export/$', views.export_books, name='export_books'),
    url(r'^books/import/$', views.import_book, name='import_book'),
    url(r'^books/(?P<book_pk>\d+)/edit/$', views.BookUpdateView.as_view(), name='edit_book'),
    url(r'^books/inactive$', views.BookListInactiveView.as_view(), name='home_inactive'),
    url(r'^books/(?P<pk>\d+)/deactivate/$', views.deactivate_book, name='deactivate_book'),
    url(r'^books/(?P<pk>\d+)/activate/$', views.activate_book, name='activate_book'),
    url(r'^books/list/$', views.book_list, name='book_list'),
    url(r'^books/(?P<pk>\d+)/export/$', views.export_book, name='export_book'),
    # url(r'^books/(?P<pk>\d+)/$', views.book_units, name='book_units'),
    url(r'^books/(?P<pk>\d+)/$', views.UnitsListView.as_view(), name='book_units'),
    #url(r'^books/new/$', views.new_book, name='new_book'),
    url(r'^books/new/$', views.NewBookView.as_view(), name='new_book'),
    # url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/$', views.unit_elements, name='unit_elements'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/$', views.ElementsListView.as_view(), name='unit_elements'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/(?P<element_pk>\d+)/edit/$', views.ElementUpdateView.as_view(), name='edit_element'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/(?P<pk2>\d+)/delete/$', views.delete_element, name='delete_element'),
    url(r'^books/(?P<pk>\d+)/importunit/$', views.import_units, name='import_units'),
    url(r'^books/(?P<pk>\d+)/exportunits/$', views.export_units, name='export_units'),
    url(r'^books/(?P<pk>\d+)/(?P<unit_pk>\d+)/edit/$', views.UnitUpdateView.as_view(), name='edit_unit'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/delete/$', views.delete_unit, name='delete_unit'),
    # url(r'^books/(?P<pk>\d+)/(?P<unit_pk>\d+)/delete/$', views.UnitDelete.as_view(), name='delete_unit'),
    url(r'^books/(?P<pk>\d+)/new/$', views.new_unit, name='new_unit'),
    #url(r'^books/(?P<pk>\d+)/new/$', views.NewUnitView.as_view(), name='new_unit'),
    url(r'^books/(?P<pk>\d+)/new/(?P<pk1>\d+)/$', views.new_element, name='new_element'),
    url(r'^books/(?P<pk>\d+)/list$', views.unit_list, name='unit_list'),
    url(r'^books/(?P<pk>\d+)/requested$', views.requested_list, name='requested_list'),
    url(r'^books/(?P<pk>\d+)/granted$', views.granted_list, name='granted_list'),
    url(r'^books/(?P<pk>\d+)/denied$', views.denied_list, name='denied_list'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/exportelements/$', views.export_elements, name='export_elements'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/importelements/$', views.import_elements, name='import_elements'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/followup/(?P<fu>\d+)/$', views.element_followups, name='element_followups'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/followup/(?P<fu>\d+)/new/$', views.new_followup, name='new_followup'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/followup/(?P<fu>\d+)/(?P<followup_pk>\d+)/edit/$', views.FollowUpUpdateView.as_view(), name='edit_followup'),
    url(r'^books/(?P<pk>\d+)/(?P<pk1>\d+)/followup/(?P<pk2>\d+)/(?P<pk3>\d+)/delete/$', views.delete_followup, name='delete_followup'),
    url(r'^books/(?P<pk>\d+)/genagreement/(?P<ems>.+)/$', views.generate_agreement, name='generate_agreement'),
    url(r'^books/(?P<pk>\d+)/followupagreement/(?P<ems>.+)/$', views.followup_agreement, name='followup_agreement'),
    url(r'^books/(?P<pk>\d+)/followupagreemente/(?P<pk1>.+)/(?P<pk2>.+)/$', views.followup_agreement_e, name='followup_agreement_e'),
    url(r'^books/(?P<pk>\d+)/emailagreement/(?P<ems>.+)/$', views.email_agreement, name='email_agreement'),
    url(r'^books/(?P<pk>\d+)/testemailagreement/(?P<ems>.+)/$', views.test_email_agreement, name='test_email_agreement'),
    url(r'^books/(?P<pk>\d+)/followupemailagreement/(?P<ems>.+)/$', views.followup_email_agreement, name='followup_email_agreement'),
    url(r'^books/(?P<pk>\d+)/testfollowupemailagreement/(?P<ems>.+)/$', views.test_followup_email_agreement, name='test_followup_email_agreement'),
    url(r'^books/(?P<pk>\d+)/followupemailagreemente/(?P<pk1>.+)/(?P<pk2>.+)/$', views.followup_email_agreement_e, name='followup_email_agreement_e'),
    url(r'^books/(?P<pk>\d+)/testfollowupemailagreemente/(?P<pk1>.+)/(?P<pk2>.+)/$', views.test_followup_email_agreement_e, name='test_followup_email_agreement_e'),
    url(r'^books/(?P<pk>\d+)/emailbody/(?P<ems>.+)/$', views.email_body, name='email_body'),
    url(r'^books/(?P<pk>\d+)/followupemailbody/(?P<ems>.+)/$', views.followup_email_body, name='followup_email_body'),
    url(r'^books/(?P<pk>\d+)/followupemailbodye/(?P<pk1>.+)/(?P<pk2>.+)/$', views.followup_email_body_e, name='followup_email_body_e'),
    url(r'^books/(?P<pk>\d+)/followups/(?P<ems>.+)/$', views.update_followups, name='update_followups'),
    url(r'^books/(?P<pk>\d+)/granted/(?P<ems>.+)/$', views.update_granted, name='update_granted'),
    url(r'^books/(?P<pk>\d+)/granted/(?P<pk1>.+)/(?P<pk2>.+)$', views.update_granted_e, name='update_granted_e'),
    url(r'^books/(?P<pk>\d+)/status_denied/(?P<pk1>.+)/(?P<pk2>.+)$', views.update_status_denied, name='update_status_denied'),
    url(r'^books/(?P<pk>\d+)/status_restore/(?P<pk1>.+)/(?P<pk2>.+)$', views.update_status_restore, name='update_status_restore'),
    url(r'^admin/', admin.site.urls),
    url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
    url(r'^reset/done/$',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
    url(r'^reset/complete/$',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)