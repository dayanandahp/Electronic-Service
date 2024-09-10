from django.db import models
#import user model 

# Create your models here.


# request_type=(
#     ("--PLEASE CHOOSE A SERVICE--","--Please choose a service--"),
#     ("laptop","LAPTOP"),
#     ("tv","TV"),
#     ("smart phone","SMART PHONE"),
#     ("wifi","WIFI"),
#     ("ac","AC"),
# )

# class customer_request(models.Model):
#     customer_name=
#     email_ID=
#     phone_number=
#     address=
#     city=
#     state=
#     pin_code=
#     request_Type=models.CharField(max_length=50, choices=request_type, default=" ")
#     description=
#     date=
#     connect=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)
#     cdate=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.customer_name
    
    
    
# class customer_message(models.Model):
#     name=
#     email_ID=
#     phone_number=
#     subject=
#     message=
#     author=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.name



# class subscriber(models.Model):
#     email_ID =

#     def __str__(self):
#         return self.email_ID
    
    
    

# class review(models.Model):
#     review_message=
#     boss=models.ForeignKey(User,default=None, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.boss.first_name