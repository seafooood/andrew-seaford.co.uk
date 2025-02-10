# React Native System Setup

## Installation

- `choco install node`
- `choco install openjdk`
- [https://developer.android.com/studio](https://developer.android.com/studio)
- Add envioment variable `ANDROID_HOME` with value `%LOCALAPPDATA%\Android\Sdk`
- Add`%LOCALAPPDATA%\Android\Sdk\platform-tools` to the `PATH` envioment variable.

## Test App

Create a test app to check the installation

- Create a new app called MyReactNativeApp `npx react-native init MyReactNativeApp`
- Change directory `cd MyReactNativeApp`
- Start ADV fr androd studio
- Start the app on the ADV `npx react-native run-android`
- Start the app `npm run start`
- Press `a` for Android.

DemoReactNativeRouting
- npm install @react-navigation/native @react-navigation/stack
- install `npm install react-native-reanimated react-native-gesture-handler`
- Install `npm install react-native-screens react-native-safe-area-context`
- Install `npm install @react-native-community/masked-view`


C:\Users\seafo\AppData\Local\jdk-11.0.2

C:\Program Files\OpenJDK\jdk-21.0.1

## Signing the app

- Open `cmd` as admin
- Change directory `cd C:\Program Files\OpenJDK\jdk-21.0.1\bin` 
- Generate the key `keytool -genkeypair -v -keystore andrew-upload-key.keystore -alias andrew -keyalg RSA -keysize 2048 -validity 1000`
- Password ``
- Copy `C:\Program Files\OpenJDK\jdk-21.0.1\bin\andrew-upload-key.keystore` to `android\app`
- `android\grade.properties` add

    ```
    MYAPP_UPLOAD_STORE_FILE=andrew-upload-key.keystore
    MYAPP_UPLOAD_KEY_ALIAS=andrew
    MYAPP_UPLOAD_STORE_PASSWORD=Askey_123
    MYAPP_UPLOAD_KEY_PASSWORD=Askey_123
    ```

- `android\app\build.grade` update sign config

    ```
    signingConfigs {
            release {
                if (project.hasProperty('MYAPP_UPLOAD_STORE_FILE')) {
                    storeFile file( MYAPP_UPLOAD_STORE_FILE)
                    storePassword MYAPP_UPLOAD_STORE_PASSWORD
                    keyAlias MYAPP_UPLOAD_KEY_ALIAS
                    keyPassword MYAPP_UPLOAD_KEY_PASSWORD
                }
            }
        }
    ```
-  Change `signingConfig signingConfigs.debug` to `signingConfig signingConfigs.release`
- `cd android`
- `gradlew bundleRelease`
- Output should be in `android\app\build\outputs\release\app-release.aab`
