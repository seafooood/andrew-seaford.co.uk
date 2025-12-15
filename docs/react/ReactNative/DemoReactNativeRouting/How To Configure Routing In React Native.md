# How To Configure Routing In React Native

- In `app.tsx`, import `import 'react-native-gesture-handler';`
- Add navigation container

   ```js
   <NavigationContainer>
         
   </NavigationContainer>
   ```

- Add stack navigator

   ```js
   import { createStackNavigator } from '@react-navigation/stack';

   const Stack = createStackNavigator();
   ```
