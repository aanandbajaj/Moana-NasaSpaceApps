# Moana

MOANA is a web application that helps city governments understand the risk of droughts or floods, and what impact these disasters could have on the local population. Considering 800 million people will live in under-resourced communities by 2050, low-cost water management tools like MOANA are a need.

The software:
+ Identifies nearby waterbodies based on satellite data,
+ Calculates change in sea levels overtime, and
+ Provides a call for action for city officials to re-route water supply if needed

## How it Works

### Data Visualization

![Image of Yaktocat](https://github.com/aanandbajaj/Moana-NasaSpaceApps/blob/master/images/Image1.png)"Logo Title Text 2"

As the above image displays, the dashboard has a section called "Data Visualization". On the left-hand side, I used the Plot.ly and D3.JS libraries to display (as an example) the change in sea levels of Salton Sea over the past 27 years.

On the right-hand side of the page section, we used the LandSat API to get the satellite images of the Salton Sea overtime and used OpenCV and Python to calculate surface area of the water body. This allows MOANA to show the user whether the water body is shrinking or growing overtime, which can inform users about risk of drought/flooding.
