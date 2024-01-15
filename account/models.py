from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# cutom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, name,tc,password=None, password2=None):
        """
        Creates and saves a User with the given email, name,tc and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  name,tc, password=None):
        """
        Creates and saves a superuser with the given email, name,tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","tc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account/image/',default="account/image/profile_img.png")

class UserEducation(models.Model):
    CHOICES = [
                ("SSC", "SSC"),
                ("HSC", "HSC"),
                ("Graduation", "Graduation"),
                ("Post Graduation", "Post Graduation")
          ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=30,choices=CHOICES)
    passing_year = models.DateField()
    institute = models.CharField(max_length=100)
    board_or_university = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.name + ' ' + self.institute
    

class UserSkill(models.Model):
    user = models.ManyToManyField(User)
    skill = models.CharField(max_length=5000)

    def user_email(self):
        return ','.join([str(p) for p in self.user.all()])
    
class UserExperince(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=200)
    exprince = models.IntegerField()
    do_join = models.DateField()
    do_resign = models.DateField()

class UserPersonalInfo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.fname



