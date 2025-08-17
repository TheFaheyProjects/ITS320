#Kyle Fahey
#Module 3: Critical Thinking
#ITS320-1

#Weather-Based Outfit Advisor

#Weather Variables
temperature = 0.0
weatherType = ""
windSpeed = 0.0

#Get User Temperature Input
while True:
    userTempInput = input("Please enter the current Temperature in °F: ")
    try:
        temperature = float(userTempInput)
        break
    except:
        print("Please enter a valid number for the Temperature.")

#Get User Weather Type Input
while True:
    userWeatherTypeInput = input("Please enter the current Weather. ie Sunny, Rainy, or Snowy: ").lower()
    if userWeatherTypeInput == "sunny" or userWeatherTypeInput == "rainy" or userWeatherTypeInput == "snowy":
        weatherType = userWeatherTypeInput
        break
    else:
        print("Please enter one of the following for the Weather: Sunny, Rainy, or Snowy.")

#Get User Wind Speed Input
while True:
    userWindSpeedInput = input("Please enter the current Wind Speed in MPH: ")
    try:
        windSpeed = float(userWindSpeedInput)
        break
    except:
        print("Please enter a valid number for the Wind Speed.")

#Advised Outfit
advisedOutfit = ""

#Outfit Advisor
if temperature < 40 and temperature > 32 and windSpeed > 10 and weatherType == "sunny" or weatherType == "rainy":
    advisedOutfit = "Its quite cold and windy out there. \nI suggest that you wear a coat and scarf to stay warm!"
elif temperature >= 40 and temperature <= 70 and weatherType == "sunny":
    advisedOutfit = "Its not too warm out there, but it is sunny. \nI suggest that you wear a light jacket and jeans!"
elif temperature > 70 and weatherType == "sunny":
    advisedOutfit = "Its hot out there! \nI suggest that you wear a t-shirt and shorts! Don't forget to use sunscreen!"
elif weatherType == "rainy":
    advisedOutfit = "Its raining quite hard out there. \nI suggest that you wear a rain coat as well as bring an umbrella so you can stay dry!"
elif weatherType == "snowy":
    advisedOutfit = "Its cold and snowy. \nI suggest that you wear a beanie or hat, a thick coat with underlayers to stay warm, \nand some thick snow boots to keep your feet dry and warm! Oh and don't forget your snow gloves!"
else:
    advisedOutfit = "Wear something that makes you happy! \nDon't dress too warm or too cold depending on your currnt weather!"

#Printing Advised Outfit
print("\nWeather-Based Outfit Advisor\n")
print(advisedOutfit)

#User MUST Press Enter to EXIT the Program
input("\nPress Enter to Exit")