# 🧪 Appium-Python-Automation-Framework

A robust and scalable test automation framework using **Appium**, **Pytest**, and **Python**. Supports mobile testing with environment-driven configuration and Docker integration.

---

## 🚀 Install Node JS

---

## 🚀 Install Appium Server
```bash
    npm install -g appium
    appium --version
    appium
```
---

## 🚀 Install UIAutomator2 and XCUITest Driver
```bash
    appium driver install uiautomator2
    appium driver install xcuitest
    appium driver list --installed 
```
---   
## 🚀 Install Appium Inspector
    1. Search 'appium-inspector' on google
    2. Visit the link https://github.com/appium/appium-inspector
    3. Under 'Installation' section click on 'Releases'
    4. Under 'Assets' section click on 'Appium-Inspector-2025.3.1-win-x64.exe'
---   
## 🚀 Android Studio Installation
    1. Search 'android studio' on google
    2. Download android studio and install
---   
## 🚀 Add ANDROID_HOME variable to System variables
    ANDROID_HOME=C:\Users\Vishvambruth_Javagal\AppData\Local\Android\Sdk
---  
## 🚀 Add below to Path variable    
    %ANDROID_HOME%\platforms
    %ANDROID_HOME%\platform-tools
    %ANDROID_HOME%\emulator
---  
## 🚀 Emulator Setup
    1. Open the Android Studio.
    2. Go to 'Tools' and Click on the 'Device Manager'.
    3. Select + Add a new device 'Create Virtual Device'.
    4. Select the required device and 'Select system image'.
    5. Click on 'Finish' the device will be added.
---  
## 🚀 Appium Inspector
    1. Remote Host: 127.0.0.1
    2. Remote Port: 4723
    3. Remote Path
    4. JSON Representation
        {
        "automationName" : "uiautomator2",
        "platformName" : "Android",
        "deviceName" : "Pixel 9 Pro XL",
        "udid" : "emulator-5554",
        "appPackage" : "com.code2lead.kwad" ,
        "appActivity" : "com.code2lead.kwad.MainActivity"       
        }
--- 
# 📱 Appium Commands

## 🔧 Install Appium Drivers
```bash
    appium driver install uiautomator2
    appium driver install xcuitest 
    appium driver install chromium
    appium driver install gecko
    appium driver install safari
    appium driver install espresso
    appium driver install mac2
```
## 🔄 Update a Driver
```bash
    appium driver update chromium
```
## 📋 List Installed Drivers
```bash
    appium driver list
    appium driver list --installed
```

# 📲 Android Device & Emulator Commands
## 🔍 View Connected Devices and Emulators
```bash
    adb devices
```  
## 🔍 Install .apk file
```bash
    adb install <.apk file path>
```
## 📦 Find App Package and App Activity
```bash
    adb shell 
    dumpsys window displays | grep -E 'mCurrentFocus’
```
## 🧾 Check Android Version of Emulator
```bash
    adb shell getprop ro.build.version.release
```
## 🧱 List Configured AVDs (Android Virtual Devices)
```bash
    emulator -list-avds
```
