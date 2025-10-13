from dateutil import parser

dates = {"Wednesday, October 2, 2002", "Friday, 11.10.13", "Thursday, 18 August 1977"}
for data in dates: dataobj = print (parser.parse(data))
