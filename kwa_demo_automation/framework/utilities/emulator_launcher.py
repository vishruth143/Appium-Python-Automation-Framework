import subprocess
import time

def launch_emulator(avd_name="Pixel_9_Pro_XL"):
    try:
        # Check if any emulator is already running
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if "emulator" in result.stdout:
            print("Emulator is already running.")
            return

        print(f"Launching emulator: {avd_name}")
        subprocess.Popen(["emulator", "-avd", avd_name])

        # Wait for emulator to appear in 'adb devices'
        for i in range(60):
            result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            if "emulator" in result.stdout and "device" in result.stdout:
                print("Emulator detected in adb devices.")
                break
            print("Waiting for emulator to appear in adb devices...")
            time.sleep(5)
        else:
            raise RuntimeError("Emulator did not appear in adb devices.")

        # Now check sys.boot_completed
        for i in range(60):
            try:
                output = subprocess.check_output(
                    "adb shell getprop sys.boot_completed", shell=True
                ).decode().strip()
                if output == "1":
                    print("Emulator booted successfully.")
                    return
            except subprocess.CalledProcessError:
                pass
            print("Waiting for emulator to finish booting...")
            time.sleep(5)

        raise RuntimeError("Emulator failed to boot within timeout.")
    except Exception as e:
        raise RuntimeError(f"Failed to start emulator: {e}")
