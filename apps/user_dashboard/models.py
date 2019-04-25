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
             matching_user = User.objects.get(email=form['email'])
             if not bcrypt.checkpw(form['password'].encode(), matching_user.pw_hash.encode()):
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



class PostManager(models.Manager):
    def validate_post(self, form):
        errors = []
        if len(form['content']) < 1:
            errors.append('Post cannot be left empty')
        return errors
    

    def easy_post_create(self, form, user_id, target_id):
        post = Post.objects.create(
            content = form['content'],
            post_sender = User.objects.get(id=user_id),
            post_receiver = User,objects.get(id=target_id)
        )
        return post.id

    def easy_post_delete(self,post_id, user_id):
        try:
            post = Post.objects.get(id=post_id)
            if post.post_reciever.id != user_id and post.post_sender.id != user_id:
                return 
            post.delete()
            except:
                print("Post doesn't exist")
    





class Post(models.Model):
    post_sender = models.ForeignKey(User, related_name='poster')
    post_reciever = models.ForeignKey(User, related_name='postee')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()


