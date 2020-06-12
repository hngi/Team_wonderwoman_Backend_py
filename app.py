from healthchecks.services.users import UserService
from healthchecks.services.sms_notifications import SmsService
from healthchecks.services.manage_pages import ManagePageService
from healthchecks.services.email_notifications import EmailService
from healthchecks.services.company_settings import CompanySettingsService
from healthchecks.services.auth import AuthService
import threading

def healthChecktimer():
    threading.Timer(600.0, healthChecktimer).start()
    
    # Managing Users Microservices Health Check
    Userhandler = UserService()
    Userhandler.create_service_url()
    UserhandlerHealthCheck = Userhandler.process_services(Userhandler.services)

    # SMS Notifications Microservices Health Check
    SmsNotificationHandler = SmsService()
    SmsNotificationHandler.create_service_url()
    SmsNotificationHandlerHealthCheck = SmsNotificationHandler.process_services(SmsNotificationHandler.services)

    # Managing Static and External Pages Microservices Health Check
    ManagePageHandler = ManagePageService()
    ManagePageHandler.create_service_url()
    ManagePageHandlerHealthCheck = ManagePageHandler.process_services(ManagePageHandler.services)

    # Email Notifications Microservices Health Check
    EmailHandler = EmailService()
    EmailHandler.create_service_url()
    EmailHandlerHealthCheck = EmailHandler.process_services(EmailHandler.services)

    # Managing Company Settings Microservices Health Check
    CompanyHandler = CompanySettingsService()
    CompanyHandler.create_service_url()
    CompanyHandlerHealthCheck = CompanyHandler.process_services(CompanyHandler.services)

    # Authentication Microservices Health Check
    AuthHandler = AuthService()
    AuthHandler.create_service_url()
    AuthHandlerHealthCheck = AuthHandler.process_services(AuthHandler.services)

    print(UserhandlerHealthCheck, SmsNotificationHandlerHealthCheck, ManagePageHandlerHealthCheck, EmailHandlerHealthCheck, CompanyHandlerHealthCheck, AuthHandlerHealthCheck)


healthChecktimer()