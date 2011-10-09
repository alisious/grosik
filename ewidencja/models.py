# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class SchoolGroup(models.Model):
	GROUP_TYPE_CHOICES = (
		('S','Stała'),
		('T','Tymczasowa'),
	)
	name = models.CharField("Nazwa",max_length=80,unique=True)
	number = models.CharField("Numer",max_length=5,blank=True)
	room_no = models.CharField("Sala",max_length=20,blank=True)
	group_type = models.CharField("Rodzaj",max_length=1,choices=GROUP_TYPE_CHOICES,default='S')

	class Meta:
  		verbose_name = 'grupa'
  		verbose_name_plural = 'grupy przedszkolne'
  		ordering = ('name',)

  	def __unicode__(self):
   		return self.name
  	

class Child(models.Model):
	GENDER_CHOICES = (
		('DZ','Dziewczynka'),
		('CH','Chłopiec'),
		)
	name = models.CharField("Nazwisko i imię",max_length = 100)
	pesel = models.CharField("PESEL",max_length = 11,unique=True)
	gender = models.CharField("Płeć",max_length = 2,choices=GENDER_CHOICES)
	school_group = models.ForeignKey('SchoolGroup',on_delete=models.PROTECT,limit_choices_to={'group_type':'S'},verbose_name="Należy do grupy")

	class Meta:
  		verbose_name = 'dziecko'
  		verbose_name_plural = 'dzieci'
  		ordering = ('name',)
	
	def __unicode__(self):
   		return self.name
 
