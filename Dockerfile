FROM ubuntu:22.04

# -------------------
# Environment Setup
# -------------------
ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH="${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin:${ANDROID_SDK_ROOT}/platform-tools:${ANDROID_SDK_ROOT}/emulator:${PATH}"
ENV AVD_NAME=pixel_xl_avd

# -------------------
# Step 1: Install dependencies (excluding default nodejs/npm)
# -------------------
RUN apt-get update && apt-get install -y \
    curl unzip openjdk-17-jdk \
    libgl1-mesa-dev libglu1-mesa \
    python3 python3-pip \
    libvirt-daemon-system libvirt-clients bridge-utils \
    xz-utils ca-certificates gnupg \
    && apt-get clean

# -------------------
# Step 2: Install latest Node.js (v22.15.1) manually
# -------------------
RUN curl -fsSL https://nodejs.org/dist/v22.15.1/node-v22.15.1-linux-x64.tar.xz -o node.tar.xz && \
    mkdir -p /usr/local/lib/nodejs && \
    tar -xJf node.tar.xz -C /usr/local/lib/nodejs && \
    rm node.tar.xz

ENV NODEJS_HOME=/usr/local/lib/nodejs/node-v22.15.1-linux-x64
ENV PATH=$NODEJS_HOME/bin:$PATH

# -------------------
# Step 3: Install Appium globally
# -------------------
RUN npm install -g appium

# -------------------
# Step 4: Download and extract Android Command Line Tools
# -------------------
RUN mkdir -p ${ANDROID_SDK_ROOT}/cmdline-tools \
    && cd ${ANDROID_SDK_ROOT}/cmdline-tools \
    && curl -o tools.zip https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip \
    && unzip tools.zip -d temp \
    && mkdir -p ${ANDROID_SDK_ROOT}/cmdline-tools/latest \
    && mv temp/cmdline-tools/* ${ANDROID_SDK_ROOT}/cmdline-tools/latest/ \
    && rm -rf tools.zip temp

# -------------------
# Step 5: Accept licenses
# -------------------
RUN yes | ${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin/sdkmanager --licenses

# -------------------
# Step 6: Install basic SDK components
# -------------------
RUN ${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin/sdkmanager \
    "platform-tools" "emulator" \
    "platforms;android-36" \
    "system-images;android-36;google_apis;arm64-v8a"

# -------------------
# Step 7: Create AVD
# -------------------
RUN echo "no" | ${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin/avdmanager \
    create avd -n ${AVD_NAME} -k "system-images;android-36;google_apis;arm64-v8a" --device "pixel_xl"

# -------------------
# Step 8: Install Python dependencies
# -------------------
COPY requirements.txt /tmp/
RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt

# -------------------
# Step 9: Copy Appium Test Automation Framework
# -------------------
COPY . /app
WORKDIR /app

# -------------------
# Step 10: Entrypoint
# -------------------
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
