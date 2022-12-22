from django.db import models

# Create your models here.

class IndustryType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'IndustryType'
        verbose_name_plural = 'IndustryTypes'

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    industry_type = models.ForeignKey(IndustryType, related_name="industry_type_company",on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    contact=models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.company_name