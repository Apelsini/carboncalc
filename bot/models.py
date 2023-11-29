from django.db import models
import csv
import json
from django.core.files.storage import FileSystemStorage

class AdvancedText (models.Model):
    enabled = models.BooleanField(default=False)
    menu = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    short = models.CharField(max_length=100)
    long = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    url=models.TextField(blank=True, null=True)
    parameters=models.TextField(blank=True, null=True)

class Constants(models.Model):
    create_date = models.DateTimeField('date created', auto_now=True)
    author = models.CharField(max_length=75)
    measure_controlling = models.CharField(max_length=5)  # Управляющий параметр:  номер константы
    measure_name = models.TextField()  # название меры
    measure_gravity = models.TextField()  # удельный параметр
    influence = models.TextField()  # влияние
    product = models.TextField()  # продукт
    unit = models.TextField()  # единица измерения
    comment = models.TextField()  # пояснение
    perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    json_numbers = models.TextField()  #

class PatternForMeasureSet(models.Model):
    create_date = models.DateTimeField('date created', auto_now=True)
    author = models.CharField(max_length=75)
    measure_controlling = models.CharField(max_length=5)  # Управляющий параметр:  control,
    measure_name = models.TextField()  # название меры
    measure_gravity = models.TextField()  # удельный параметр
    influence = models.TextField()  # влияние
    product = models.TextField()  # продукт
    unit = models.TextField()  # единица измерения
    comment = models.TextField()  # пояснение
    perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный

class Research(models.Model):
    create_date = models.DateTimeField('date created', auto_now=True)
    research_name = models.CharField(max_length=175)
    investments_values = models.TextField()  # сумма инвестиций по набору мер
    carboneffect_values = models.TextField()  # сумма Углеродэффект по набору мер
    naturaleffect_values = models.TextField()  # список и суммы по эффекту в натуральном выражении
    additbenefit_values = models.TextField()  # список и суммы по Допвыгодам
    constants_selected = models.TextField()  # список и суммы по Допвыгодам

class Scenario(models.Model):
    create_date = models.DateTimeField('date created', auto_now=True)
    scenario_name = models.CharField(max_length=175)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    investments_values = models.TextField()  # сумма инвестиций по набору мер
    carboneffect_values = models.TextField()  # сумма Углеродэффект по набору мер
    naturaleffect_values = models.TextField()  # список и суммы по эффекту в натуральном выражении
    additbenefit_values = models.TextField()  # список и суммы по Допвыгодам
    constants_selected = models.TextField()  # список и суммы по Допвыгодам

class PackageMeasureSet(models.Model):
    create_date = models.DateTimeField('date created', auto_now=True)
    packagemeasureset_name = models.CharField(max_length=175)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    investments_values = models.TextField()  # сумма инвестиций по набору мер
    carboneffect_values = models.TextField()  # сумма Углеродэффект по набору мер
    naturaleffect_values = models.TextField()  # список и суммы по эффекту в натуральном выражении
    additbenefit_values = models.TextField()  # список и суммы по Допвыгодам
    constants_selected = models.TextField()  # список и суммы по Допвыгодам

class MeasureSet(models.Model):
    create_date = models.DateTimeField('date created', auto_now=True)
    measureset_name = models.CharField(max_length=175)
    package = models.ForeignKey(PackageMeasureSet, on_delete=models.CASCADE)
    investments_values = models.TextField() # сумма инвестиций по набору мер
    carboneffect_values = models.TextField() # сумма Углеродэффект по набору мер
    naturaleffect_values = models.TextField() # список и суммы по эффекту в натуральном выражении
    additbenefit_values = models.TextField() # список и суммы по Допвыгодам

class Measure(models.Model):
    create_date = models.DateTimeField('date created', auto_now=True)
    measure_set = models.ForeignKey(MeasureSet, on_delete=models.CASCADE)
    author = models.CharField(max_length=75)

    measure_textfield = models.TextField()
    measure_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    measure_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    measure_json_numbers = models.TextField()  #

    invest_textfield = models.TextField() # measure_name, measure_gravity, influence, product, unit, comment
    invest_perunit_parameter_preinstalled = models.FloatField() #Удельный параметр - предустановленный
    invest_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    invest_json_numbers = models.TextField() # значения с 2021 по 2025 г. для numbers = [25, 36, 48, 54] используется json_numbers = json.dumps(numbers)

    carboneffect_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    carboneffect_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    carboneffect_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    carboneffect_json_numbers = models.TextField()  #

    nateffect1_enabled = models.BooleanField(default=False)
    nateffect1_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    nateffect1_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    nateffect1_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    nateffect1_json_numbers = models.TextField()  #

    nateffect2_enabled = models.BooleanField(default=False)
    nateffect2_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    nateffect2_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    nateffect2_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    nateffect2_json_numbers = models.TextField()  #

    nateffect3_enabled = models.BooleanField(default=False)
    nateffect3_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    nateffect3_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    nateffect3_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    nateffect3_json_numbers = models.TextField()  #

    nateffect4_enabled = models.BooleanField(default=False)
    nateffect4_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    nateffect4_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    nateffect4_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    nateffect4_json_numbers = models.TextField()  #

    nateffect5_enabled = models.BooleanField(default=False)
    nateffect5_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    nateffect5_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    nateffect5_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    nateffect5_json_numbers = models.TextField()  #

    additben1_enabled = models.BooleanField(default=False)
    additben1_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    additben1_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    additben1_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    additben1_json_numbers = models.TextField()  #

    additben2_enabled = models.BooleanField(default=False)
    additben2_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    additben2_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    additben2_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    additben2_json_numbers = models.TextField()  #

    additben3_enabled = models.BooleanField(default=False)
    additben3_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    additben3_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    additben3_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    additben3_json_numbers = models.TextField()  #

    additben4_enabled = models.BooleanField(default=False)
    additben4_textfield = models.TextField()  # measure_name, measure_gravity, influence, product, unit, comment
    additben4_perunit_parameter_preinstalled = models.FloatField()  # Удельный параметр - предустановленный
    additben4_perunit_parameter_user = models.FloatField()  # Удельный параметр - предустановленный
    additben4_json_numbers = models.TextField()  #

    # jsonStr = '[1, 2.1, 3, 4.3]'
    # aList = json.loads(jsonStr)
    # print(aList[1] + aList[2])
    @parameter
    def json_to_list(self, json_numbers):
        aList=json.loads(json_numbers)
        return aList

    @parameter
    def list_to_json(self, aList):
        json_numbers = json.dumps(aList)
        return json_numbers

    @parameter
    def recalculate(self, scale, multiplier, aList):
        rlist = []
        for num in aList:
            if type(num) == int or type(num) == float:
                rlist.append(num*multiplier*scale)
            else:
                rlist.append(0)
        return rlist

    @parameter
    def text_to_field(self, measure_controlling, measure_name, measure_gravity, influence, product, unit, comment):
        out = []
        out.append(measure_controlling)
        out.append(measure_name)
        out.append(measure_gravity)
        out.append(influence)
        out.append(product)
        out.append(unit)
        out.append(comment)
        jsonout = json.dumps(out)
        return jsonout
  #    measure_controlling = models.CharField(max_length=5) #Управляющий параметр:  control,
  # measure_name = models.TextField() # название меры
  #  measure_gravity = models.TextField() # удельный параметр
   # influence = models.TextField() # влияние
  #  product = models.TextField() # продукт
  #  unit = models.TextField() # единица измерения
   # comment = models.TextField() # пояснение

    @parameter
    def field_to_text(self, field):
        aList=json.loads(field)
        return aList



# measures are indicated in strings No
    # 1
    # 9
    # 14
    # 19
    # 23
    # 28
    # 33
    # 38
    # 43
    # 48
    # 52
    # 56
    # 60
    # 66
    # 71
    # 76
    # 81
    # 86
    # 91
    # 96

