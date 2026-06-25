from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None, **extra_data):
        if not email:
            raise ValueError("Email must be set.")
        
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,**extra_data)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None , **extra_data):
        extra_data.setdefault('is_staff',True)
        extra_data.setdefault('is_superuser',True)

        return self.create_user(email,password,**extra_data)