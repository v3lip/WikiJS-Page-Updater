# WikiJS-Page-Updater

NOT at all a Python programmer.
You will need to edit the code yourself if you need something like this for your project, as this is pretty hard coded into the Matrix.

Seemed useful for me as I have a pretty big list that needs to be formatted as a table. So this is great as I dont have to manage the markdown table myself with spacings and what not.

This is a simple script that reads a page 'id: 158', sorts the info alphabetically formats the content in the codeblock into a markdown table, and puts the formated markdown table into another page 'id: 157'.

Output from page 'id: 158':
Where >``` ignore >
```
[Tilbake](.)

Kjører et pythonscript hver 12 time som oppdaterer forrige side automatisk. <kbd>Kode ligger [her](kode)</kbd>

---

>```
SolarTech Innovations,SunCharger 3000,Emily Johnson,555-0321,emily.johnson@solartech.com
GreenGro Solutions,HydroGrow Kit,Raj Patel,555-0472,raj.patel@greengro.com
Quantum Computing Inc.,Qubit Processor,Lee Huang,555-0603,lee.huang@quantumcomp.com
BlueOcean Technologies,AquaDrone,Maria Gomez,555-0784,maria.gomez@blueoceantech.com
Future Mobility,SkyHover Car,Alex Smith,555-0925,alex.smith@futuremobility.com
CyberSecure,FirewallX,Nora Khumalo,555-1036,nora.khumalo@cybersecure.com
HealthEase,CardioFit Band,Carlos Fernandez,555-1177,carlos.fernandez@healthease.com
EdTech Innovations,SmartBoard 2025,Sarah Tan,555-1328,sarah.tan@edtechinnovations.com
SpaceFrontiers,Orion Rocket,Omar Al-Bashir,555-1469,omar.albashir@spacefrontiers.com
AI Solutions,ChatBot Pro,Jasmine Lee,555-1600,jasmine.lee@aisolutions.com
>```
```
Code:
 > Sorts it by company    
 > Formats it into a markdown table like this:

Posts the result to the page (id: 157)

```
| Firma                | Produkt        | Navn           |Navn         |Epost                           |
|----------------------|----------------|----------------|-------------|--------------------------------|
|SolarTech Innovations | SunCharger 3000|Emily Johnson   |555-0321     |emily.johnson@solartech.com     |
|GreenGro Solutions    | HydroGrow Kit  |Raj Patel       |555-0472     |raj.patel@greengro.com          |
|Quantum Computing Inc | Qubit Processor|Lee Huang       |555-0603     |lee.huang@quantumcomp.com       |
|BlueOcean Technologies| AquaDrone      |Maria Gomez     |555-0784     |maria.gomez@blueoceantech.com   |
|Future Mobility       | SkyHover Car   |Alex Smith      |555-0925     |alex.smith@futuremobility.com   |
|CyberSecure           | FirewallX      |Nora Khumalo    |555-1036     |nora.khumalo@cybersecure.com    |
|HealthEase            | CardioFit Band |Carlos Fernandez|555-1177     |carlos.fernandez@healthease.com |
|EdTech Innovations    | SmartBoard 2025|Sarah Tan       |555-1328     |sarah.tan@edtechinnovations.com |
|SpaceFrontiers        | Orion Rocket   |Omar Al-Bashir  |555-1469     |omar.albashir@spacefrontiers.com|
|AI Solutions          | ChatBot Pro    |Jasmine Lee     |555-1600     |jasmine.lee@aisolutions.com     |
```
| Firma                | Produkt        | Navn           |Navn         |Epost                           |
|----------------------|----------------|----------------|-------------|--------------------------------|
|SolarTech Innovations | SunCharger 3000|Emily Johnson   |555-0321     |emily.johnson@solartech.com     |
|GreenGro Solutions    | HydroGrow Kit  |Raj Patel       |555-0472     |raj.patel@greengro.com          |
|Quantum Computing Inc | Qubit Processor|Lee Huang       |555-0603     |lee.huang@quantumcomp.com       |
|BlueOcean Technologies| AquaDrone      |Maria Gomez     |555-0784     |maria.gomez@blueoceantech.com   |
|Future Mobility       | SkyHover Car   |Alex Smith      |555-0925     |alex.smith@futuremobility.com   |
|CyberSecure           | FirewallX      |Nora Khumalo    |555-1036     |nora.khumalo@cybersecure.com    |
|HealthEase            | CardioFit Band |Carlos Fernandez|555-1177     |carlos.fernandez@healthease.com |
|EdTech Innovations    | SmartBoard 2025|Sarah Tan       |555-1328     |sarah.tan@edtechinnovations.com |
|SpaceFrontiers        | Orion Rocket   |Omar Al-Bashir  |555-1469     |omar.albashir@spacefrontiers.com|
|AI Solutions          | ChatBot Pro    |Jasmine Lee     |555-1600     |jasmine.lee@aisolutions.com     |





