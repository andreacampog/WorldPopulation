
from operator import itemgetter


def get_population(country_dict):
 
  population_dict ={
    '2022' :int(country_dict['2020 Population']),
    '2015' :int(country_dict['2015 Population']),
    '2010' :int(country_dict['2010 Population']),
    '2000' :int(country_dict['2000 Population']),
    '1990' :int(country_dict['1990 Population']),
    '1980' :int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  print(population_dict)

  return labels, values

def population_by_country(data,country):
  result = list(filter(lambda item: item['Country/Territory'] == country,data))
  print (result)
  return result

def country_percentage(data):
  
  #Este data_1 es una lista generada para filtrar por continente
  #si deseo omitirla pongo data en las lineas 34 y 35 
  data_1= list(filter(lambda item: item['Continent'] == 'South America', data))
  
  
  percentages = list(map(lambda item : item['World Population Percentage'],data_1))
  countries = list(map(lambda item : item['Country/Territory'],data_1))
  print(countries,percentages)
  new_dict = {countries : percentages for (countries,percentages) in zip (countries,percentages)}

  print(new_dict)

  return countries,percentages












