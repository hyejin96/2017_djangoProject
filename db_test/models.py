from django.db import models

class JobTitle(models.Model): # 직함 = JobTitle
	title = models.CharField(max_length=10)  # id는 기본적으로 만들어 지니 title만 만들었다.
	def __str__(self):
		return str(self.id) + " " + self.title # title을 보이게 하라. id는 integer이고 title은 string이다. 그렇기에 id를 str로 변환한다.

class Department(models.Model):
    name = models.CharField(max_length=10)
    upper_department = models.ForeignKey('Department', blank = True, null=True, on_delete = models.CASCADE)  # 자기자신과 관계를 맺을 때에는 ' '을 써야한다. 그리고 null = True도 해야한다.
	# 기획 부는 상위 변수가 없어서 null이라 해야되니 null = True라 하자! blank로 남겨두어도 null로 처리를 할 것이다.
    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + str(self.upper_department)
