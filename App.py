expo_config = {
    "expo": {
        "name": "bolt-expo-nativewind",
        "slug": "bolt-expo-nativewind",
        "version": "1.0.0",
        "orientation": "portrait",
        "icon": "./assets/images/icon.png",
        "scheme": "myapp",
        "userInterfaceStyle": "automatic",
        "newArchEnabled": True,
        "ios": {
            "supportsTablet": True
        },
        "web": {
            "bundler": "metro",
            "output": "single",
            "favicon": "./assets/images/favicon.png"
        },
        "plugins": ["expo-router", "expo-font", "expo-web-browser"],
        "experiments": {
            "typedRoutes": True
        }
    }
}

# Example usage: access app name
print(expo_config["expo"]["name"])  # Output: bolt-expo-nativewind
