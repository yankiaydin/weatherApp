from django.shortcuts import render

def home(request):
    import requests
    import json


    if request.method == "POST":
        city = request.POST["zipcode"]
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + city + "&distance=5&API_KEY=C76C453E-9382-400B-9F0F-0A3C7E269E52")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error...."

        if api[0]['Category']['Name'] == "Good":
            category_status = "(0 to 50)-Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_status = "(51 to 100)-Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_status = "(101 to 150)-Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_status = "(151 to 200)-Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_status = "(201 to 300)-Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_status = "(300 and higher)-Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {"city":city, "api":api, "category_status":category_status, "category_color": category_color})
    else:
        api_request = requests.get(
            'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C76C453E-9382-400B-9F0F-0A3C7E269E52')
        # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=C76C453E-9382-400B-9F0F-0A3C7E269E52
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error...."

        if api[0]['Category']['Name'] == "Good":
            category_status = "(0 to 50)-Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_status = "(51 to 100)-Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_status = "(101 to 150)-Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_status = "(151 to 200)-Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_status = "(201 to 300)-Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_status = "(300 and higher)-Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"


        return render(request, 'home.html', {"api":api, "category_status":category_status, "category_color": category_color})


def about(request):
    return render(request, 'about.html', {})
