from django.db import models
import re 
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    
    def easy_register_validate(self, form):
        errors = []
        if len(form['first_name']) < 2:
            errors.append('First Name should be at least 2 characters')
        if len(form['last_name']) < 2:
            errors.append('Last Name should be at least 2 characters')
        if not EMAIL_REGEX.match(form['email']):
            errors.append('Email must be in a valid format')
        matching_users= User.objects.filter(email=form['email'])
        if matching_users:
            errors.append('Email already in use')
        return errors


    def easy_login_validate(self, form):
        errors =[]
        if len(form['email']) < 1:
            errors.append("Email can't be blank")
        else:
            matching_users = User.objects.filter(email=form['email'])
            if not matching_users:
                errors.append('Email not in system')
        if  len(form['password']) < 1:
                errors.append('Please enter a Password')
        else:
             matching_user = User.objects.filter(email=form['email'])
             if not bcrypt_checkpw(form['password'].encode(), matching_user.pw_hash.encode()):
                    errors.append('Password Incorrect')
        return errors

    def easy_user_create(self, form):
        pw_hash = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        existing_users = User.objects.all().count()
        if existing_users > 0:
            user_level = 1
        else:
            user_level = 9
        user = User.objects.create(
            first_name = form ['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            user_level = user_level,
            pw_hash = pw_hash
        )
        return user




class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    user_level = models.IntegerField()
    description = models.TextField(blank= True)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Post(models.Model):
    post_sender = models.ForeignKey(User, related_name='poster')
    post_reciever = models.ForeignKey(User, related_name='postee')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


