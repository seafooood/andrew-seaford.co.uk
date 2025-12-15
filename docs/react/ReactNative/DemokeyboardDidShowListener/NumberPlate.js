import React, { useState, useEffect, useRef  } from 'react';
import { TextInput, View, StyleSheet, LayoutAnimation, UIManager, useWindowDimensions, Keyboard  } from 'react-native';
import { ScaledSheet } from 'react-native-size-matters';


const NumberPlate = ({ value, onChangeText }) => {

  const [fontSize, setFontSize] = useState(90);
  const textContainerRef = useRef(null);
  const textRef = useRef(null);

  const calculateFontSize = () => {
    textRef.current.measureLayout(
      textContainerRef.current,
      (left, top, width, height) => {
        console.log("**** l=" + left + "t=" + top + " w=" + width + " h=" + height);

        const newFontSize = width / Math.max(7, 1) - 10
        console.log("**** newFontSize=" + newFontSize);
        setFontSize(newFontSize);
      },
    );
  }

  useEffect(() => {
    const keyboardDidShowListener = Keyboard.addListener(
      'keyboardDidShow',
      () => {
        // Keyboard is displayed, adjust layout as needed
        // You can implement logic here to handle the resizing of your components
        console.log('Keyboard is displayed');

        calculateFontSize();
      }
    );

    const keyboardDidHideListener = Keyboard.addListener(
      'keyboardDidHide',
      () => {
        // Keyboard is hidden, adjust layout as needed
        // You can implement logic here to handle the resizing of your components
        console.log('Keyboard is hidden');

        calculateFontSize();
      }
    );

    return () => {
      keyboardDidShowListener.remove();
      keyboardDidHideListener.remove();
    };
  }, []);

  return (
    <View style={styles.container} ref={textContainerRef}>
      <TextInput
      style={{ ...styles.input, fontSize: fontSize }}
      value={value}
      onChangeText={onChangeText}
      autoCapitalize="characters"
      maxLength={7}
      underlineColorAndroid="transparent" // Set to transparent to hide the inner border on Android
      ref={textRef}
      />            
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'yellow',
    padding: 10,
    borderRadius: 10,
    borderWidth: 2,
    borderColor: 'black',
    width: '96%',
    height: '25%',
    margin:'2%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    color: 'black',
    backgroundColor: 'red',
    textTransform: 'uppercase',
    fontFamily: 'monospace',
    borderWidth: 0, // Set to 0 to hide the inner border on iOS,
    textAlign:'center',
    flex: 1, 
    fontSize:'20@vs'
  },
});

export default NumberPlate;
