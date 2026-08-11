# GitHub Publishing Guide

## 1. Create a New Repository

1. Go to GitHub.
2. Select **New repository**.
3. Name the repository: `private-bank-investment-professional-simulation`.
4. Add this description:  
   `Synthetic private-bank investment professional workflow covering portfolio review, scenario analysis, trade controls, billing, and alternatives documentation.`
5. Set visibility to **Public** if you want recruiters to view it.
6. Do not initialize with a README if you are uploading this full project folder.

## 2. Upload the Project Through GitHub Website

1. Open the new repository.
2. Select **Add file** → **Upload files**.
3. Drag the full project folder contents into the upload window.
4. Commit with this message:  
   `Initial private bank investment professional simulation project`

## 3. Upload Using Git

From your computer terminal:

```bash
cd private-bank-investment-professional-simulation
git init
git add .
git commit -m "Initial private bank investment professional simulation project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/private-bank-investment-professional-simulation.git
git push -u origin main
```

## 4. Pin the Repository

1. Go to your GitHub profile.
2. Select **Customize your pins**.
3. Pin this project near the top.

## 5. Add the Link to Your Resume

Use the project name under a Selected Project section:

**Private Bank Investment Professional Simulation | Excel, Python, PowerPoint**  
Built a synthetic private-bank portfolio support workflow evaluating client allocations, risk/return profiles, scenario outcomes, trade/blotter exceptions, fee schedules, and alternatives documentation; produced an executive-ready Excel dashboard and PowerPoint presentation simulating support for Investors and Client Advisors.

## 6. Add Screenshots

Recommended screenshots:
- Excel dashboard
- portfolio summary
- scenario analysis
- trade control exceptions
- executive deck title slide

Place screenshots in an `assets/` folder and reference them in the README.
