# WikiJS Page Updater

A simple Python script that updates a WikiJS page by converting CSV-style content into a formatted Markdown table.

## ⚠️ Disclaimer

I'm **not** a Python developer. This script is hardcoded for my specific use case. You’ll likely need to modify the code to fit your own setup.

## 📝 What It Does

- Reads content from a WikiJS page (`id: 158`)
- Extracts the CSV-style data inside a code block
- Sorts the entries alphabetically by company name
- Converts the data into a Markdown table
- Updates a different WikiJS page (`id: 157`) with the formatted table

This helps me avoid manually formatting large tables in Markdown — the script handles alignment, sorting, and layout.

## 🧪 Example Input

The script looks for a block of data like this inside a WikiJS page:

```markdown
SolarTech Innovations,SunCharger 3000,Emily Johnson,555-0321,emily.johnson@solartech.com
GreenGro Solutions,HydroGrow Kit,Raj Patel,555-0472,raj.patel@greengro.com
Quantum Computing Inc.,Qubit Processor,Lee Huang,555-0603,lee.huang@quantumcomp.com
BlueOcean Technologies,AquaDrone,Maria Gomez,555-0784,maria.gomez@blueoceantech.com
...
```
## 📊 Example Output
The output looks like this:
```
| Firma                 | Produkt         | Navn            | Telefon  | Epost                             |
|-----------------------|------------------|------------------|----------|-----------------------------------|
| AI Solutions          | ChatBot Pro      | Jasmine Lee      | 555-1600 | jasmine.lee@aisolutions.com       |
| BlueOcean Technologies| AquaDrone        | Maria Gomez      | 555-0784 | maria.gomez@blueoceantech.com     |
| CyberSecure           | FirewallX        | Nora Khumalo     | 555-1036 | nora.khumalo@cybersecure.com      |
| EdTech Innovations    | SmartBoard 2025  | Sarah Tan        | 555-1328 | sarah.tan@edtechinnovations.com   |
| Future Mobility       | SkyHover Car     | Alex Smith       | 555-0925 | alex.smith@futuremobility.com     |
| GreenGro Solutions    | HydroGrow Kit    | Raj Patel        | 555-0472 | raj.patel@greengro.com            |
| HealthEase            | CardioFit Band   | Carlos Fernandez | 555-1177 | carlos.fernandez@healthease.com   |
| Quantum Computing Inc | Qubit Processor  | Lee Huang        | 555-0603 | lee.huang@quantumcomp.com         |
| SolarTech Innovations | SunCharger 3000  | Emily Johnson    | 555-0321 | emily.johnson@solartech.com       |
| SpaceFrontiers        | Orion Rocket     | Omar Al-Bashir   | 555-1469 | omar.albashir@spacefrontiers.com  |
```

# 🛠 How It Works (Summary)
1. Script runs every 12 hours via cron (or other scheduling)
2. Parses content from source WikiJS page (id: 158)
3. Converts to a clean, sorted Markdown table
4. Updates the target WikiJS page (id: 157)
