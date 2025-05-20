#!/bin/bash

set -e

echo "[INFO] Starting Android Emulator..."
$ANDROID_SDK_ROOT/emulator/emulator -avd $AVD_NAME -no-audio -no-window -gpu off &

trap "echo '[INFO] Shutting down emulator...'; adb -s emulator-5554 emu kill || true; exit" SIGINT SIGTERM EXIT

echo "[INFO] Waiting for emulator to boot..."
$ANDROID_SDK_ROOT/platform-tools/adb wait-for-device

BOOT_COMPLETE=""
until [[ "$BOOT_COMPLETE" == "1" ]]; do
  BOOT_COMPLETE=$($ANDROID_SDK_ROOT/platform-tools/adb shell getprop sys.boot_completed | tr -d '\r')
  echo "[INFO] Emulator boot status: $BOOT_COMPLETE"
  sleep 5
done

echo "[INFO] Unlocking emulator screen..."
$ANDROID_SDK_ROOT/platform-tools/adb shell input keyevent 82

APK_PATH="/app/kwa_demo_automation/app_apk/Android_Demo_App.apk"
if [[ -f "$APK_PATH" ]]; then
  echo "[INFO] Installing APK: $APK_PATH"
  $ANDROID_SDK_ROOT/platform-tools/adb install "$APK_PATH"
else
  echo "[WARN] APK not found at $APK_PATH — skipping install"
fi

echo "[INFO] Starting Appium server..."
nohup appium > /tmp/appium.log 2>&1 &
sleep 10

echo "[INFO] Running tests using Pytest..."
pytest kwa_demo_automation/tests
