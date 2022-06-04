from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    preamble = models.CharField(max_length=1024, verbose_name='Preamble')
    body = models.TextField(blank=True, null=True, verbose_name='Body')
    body_as_markdown = models.BooleanField(default=False, verbose_name='As markdown')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created', editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated', editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} {self.title}'

    def delete(self, *args):
        self.deleted = True
        self.save()


class Courses(models.Model):
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    description_as_markdown = models.BooleanField(verbose_name='Desc as markdown', default=False)
    cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Cost', default=0)
    cover = models.CharField(max_length=25, default='no_image.svg', verbose_name='Cover')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} {self.name}'

    def delete(self, *args):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='Lesson number')
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    deleted = models.BooleanField(default=False)

    def delete(self, *args):
        self.deleted = True
        self.save()

    def __str__(self):
        return f'{self.pk} {self.num} {self.title}'

    class Meta:
        ordering = ('course', 'num')


class Teachers(models.Model):
    course = models.ManyToManyField(Courses)
    first_name = models.CharField(max_length=50, verbose_name='FirstName')
    last_name = models.CharField(max_length=75, verbose_name='LastName')
    birthday = models.DateField(verbose_name='Birthday')
    deleted = models.BooleanField(default=False)

    def delete(self, *args):
        self.deleted = True
        self.save()

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.last_name, self.first_name)
