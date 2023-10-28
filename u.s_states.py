
# I took this source code from GITHUB and then I edited it a bit and then added the U.S. Territories in a separate list.
# The capital for Guam has a circle above the a and the special letter n with the ~ above it.
# The | after each state and territory is the capital. 
state_names=["Alaska | Juneau", "Alabama | Montgomery  ", "Arkansas | Little Rock", "Arizona | Phoenix", "California | Sacramento", "Colorado | Denver", "Connecticut | Hartford", "Delaware | Dover", "Florida | Tallahassee", "Georgia | Atlanta","Hawaii | Honolulu", "Iowa | Des Moines", "Idaho | Boise", "Illinois | Springfiled", "Indiana | Indianapolis", "Kansas | Topeka", "Kentucky | Frankfort", "Louisiana | Baton Rouge", "Massachusetts | Boston", "Maryland | Annapolis", "Maine | Augusta", "Michigan | Lansing", "Minnesota | St. Paul", "Missouri | Jefferson City", "Mississippi | Jackson ", "Montana | Helena", "North Carolina | Raleigh", "North Dakota | Bismarck", "Nebraska | Lincoln", "New Hampshire | Concord", "New Jersey | Trenton", "New Mexico | Santa Fe", "Nevada | Carson City", "New York | Albany", "Ohio | Columbus", "Oklahoma | Oklahoma City ", "Oregon | Salem", "Pennsylvania | Harrisburg", "Rhode Island | Providence ","South Carolina | Columbia", "South Dakota | Pierre", "Tennessee | Nashville", "Texas | Austin", "Utah | Salt Lake City", "Vermon | Montpelier", "Virginia | Richmond", "Washington | Olympia", "Wisconsin | Madison", "West Virginia | Charleston", "Wyoming | Cheyenne"]
us_territories=["Guam | Hagatna","Puerto Rico | San Juan","Washington D.C. | United States Minor Outlying Islands ","American Samoa | Pago Pago","Northern Mariana Island |  Saipan","U.S. Virgin Islands | Charlotte Amalie","Federated States of Micronesia | Palikir","Marshall Island | Majuro","Palau | Ngerulmud"]

print("-----")
print("Here are the names of all 50 states in the USA with it's capitals.")
for i in state_names:
    print(state_names.index(i) +1, end=' ')
    print(" ",i)
print("-----")
print("After, here are some of the U.S. Territories and their capitals.")
print("-----")
for us in us_territories:
    print("- " +us)
print("-----")


print("Here are the initials of all the states.") 
states = ["AL - Alabama", "AK - Alaska", "AZ - Arizona", "AR - Arkansas", "CA - California", "CO - Colorado", "CT - Connecticut", "DC - District of Columbia", "DE - Delaware", "FL - Florida", "GA - Georgia", 
          "HI - Hawaii", "ID - Idaho", "IL - Illinois", "IN - Indiana", "IA - Iowa", "KS - Kansas", "KY - Kentucky", "LA - Louisiana" , "ME - Maine", "MD - Maryland", 
          "MA - Massachusetts", "MI - Michigan", "MN - Minnesota", "MS - Mississippi", "MO - Missouri", "MT - Montana", "NE - Nebraska", "NV - Nevada", "NH - New Hampshire", "NJ - New Jersey", 
          "NM - New Mexico", "NY - New York", "NC - North Carolina", "ND - North Dakota", "OH - Ohio", "OK - Oklahoma", "OR - Oregon", "PA - Pennsylvania", "RI - Rhode Island", "SC - South Carolina", 
          "SD - South Dakota", "TN - Tennessee", "TX - Texas", "UT - Uthah", "VT - Vermont", "VA - Virginia", "WA - Washington", "WV - West Virginia", "WI - Wisconsin", "WY - Wyoming"]
for states in states:
    print(states)

print("-----")
print("Here are the initals of the U.S Territories.")
us_territories = ["AS – American Samoa","FM – Federated States of Micronesia","GU – Guam","MH – Marshall Islands","MP – Northern Mariana Islands","PR – Puerto Rico","PW – Palau" "U.S. Virgin Islands","UM – U.S. Minor Outlying Islands"] 
for us in us_territories:
    print(us)
print("-----")

