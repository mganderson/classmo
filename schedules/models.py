from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Base model for others to inherit from
class BaseModel(models.Model):
    """Base model exists for the sole purpose of creating the created_date
    & modified_date with the correct date format
    """
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)


class Subject(BaseModel):
    """Subject its a dump table that contains the list of subjects that the 
    system supports
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Location(BaseModel):
    """Location contains information about the location of a session.
    """
    name = models.CharField(max_length=200)
    max_capacity = models.IntegerField(default=0)
    address_1 = models.CharField(max_length=128, default="")
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, default="New York")
    state = models.CharField(max_length=2, default="NY")
    zip_code = models.CharField(max_length=5, default="00000")
    country = models.CharField(max_length=128, default="United States")

    def __str__(self):
        return self.name


class Session(BaseModel):
    """Session is the main entity for the scheduling app, which creates a rela-
    tionship between a subject, a location and a student.
    """
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    max_capacity = models.IntegerField(default=0)
    registered_students = models.IntegerField(default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def is_registered(self,user):
        check=self.registration_set.filter(user=user).exists()
        return check

    def is_instructor(self,user):
        if self.instructor.pk==user.pk:
            return True
        else:
            return False

    @classmethod    
    def instructor_assignments(self,instructor):
        """Returns list of sessions assigned to current instructor
        """
        return self.objects.filter(instructor=instructor.pk)


class Registration(BaseModel):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """On save, update session and validate this registration
        """
        if not self.registration_validator():
            # updating session registration count
            session = self.session
            session.registered_students += 1
            session.save()
            super(Registration, self).save(*args, **kwargs)
            return True
        else:
            return False

    def delete(self, *args, **kwargs):
        """On delete, update session
        """
        session = self.session
        current_registered = session.registered_students - 1

        if current_registered < 0:
            current_registered = 0
        session.registered_students=current_registered
        session.save()
        return super(Registration, self).delete(*args, **kwargs)

    def registration_validator(self):
        """Validating registration before creation. A registration will be 
        created, only if any of the following violations occur:
        - registered_students == max_capacity
        - some undefined ones yet
        """
        registered_students_count = self.session.registered_students
        max_capacity = self.session.max_capacity

        print("Registered Count: {}".format(registered_students_count))
        print("Max Capacity: {}".format(max_capacity))

        violations = []

        if registered_students_count >= max_capacity:
            # session is full
            violations.append(1)
        return bool(violations)
        
    @classmethod    
    def student_registrations(cls,student):
        """Returns list of registrations for given students
        """
        return cls.objects.filter(user=student.pk)

    @classmethod
    def student_registration_for_session(cls, student, session):
        """Returns the student's registration for a given session
        """
        return cls.objects.get(user=student, session=session)

    @classmethod
    def session_students(cls, session_id):
        """Returns a list of students for a given session
        """
        return cls.objects.filter(session=session_id)

    @classmethod
    def subjects_for_student(cls, student_id):
        """Returns all subjects for a given student
        """
        registrations = cls.objects.filter(user=student_id)
        subjects = []

        for registration in registrations:
            # for registration check if subject is in list
            if registration.session.subject not in subjects:
                # new subject
                subjects.append(registration.session.subject) 
        return subjects


class Homework(BaseModel):
    """Homework contains data about homework assignments
    """
    name=models.CharField(max_length=200)
    #instructor=models.ForeignKey(User,on_delete=models.CASCADE)
    session=models.ForeignKey(Session,on_delete=models.CASCADE,
        default=1,null=True)
    description=models.CharField(max_length=200)
    due_date=models.DateTimeField(auto_now=False)
    def __str__(self):
        return self.name


class Profile(models.Model):
    """Profile contains metadata from the user that are not essential, 
    but its useful to have
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=128, default="")
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, default="New York")
    state = models.CharField(max_length=128, default="NY")
    zip_code = models.CharField(max_length=128, default="00000")
    country = models.CharField(max_length=128, default="United States")
    phone = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username


    @classmethod
    def update_profile(cls, user, **profile_data):
        """Updating the user's profile with the information passed from the form
        """
        user.first_name = profile_data.get("first_name")
        user.last_name = profile_data.get("last_name")
        user.profile.address_1 = profile_data.get("address_1")
        user.profile.address_2 = profile_data.get("address_2")
        user.profile.city = profile_data.get("city")
        user.profile.state = profile_data.get("state")
        user.profile.zip_code = profile_data.get("zip_code")
        user.profile.country = profile_data.get("country")
        user.profile.phone = profile_data.get("phone_number")
        user.save()
        return True

    @classmethod
    def update_account(cls, user, **account_data):
        """Updating the user account with the information passed from the form
        """
        user.username = account_data.get("username")
        user.email = account_data.get("email")
        user.save()
        return True


        




