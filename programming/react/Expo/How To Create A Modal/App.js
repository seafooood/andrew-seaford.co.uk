import { Text, Pressable } from 'react-native';
import { useState } from 'react';
import EmojiPicker from "./EmojiPicker";

export default function App() {
  const [isModalVisible, setIsModalVisible] = useState(false);

  const onAddSticker = () => {
    setIsModalVisible(true);
  };

  const onModalClose = () => {
    setIsModalVisible(false);
  };

  return (
    <>
      <EmojiPicker isVisible={isModalVisible} onClose={onModalClose}>
        <Text>Hi from Modal</Text>
      </EmojiPicker>      
      <Pressable onPress={onAddSticker}><Text>click me</Text></Pressable>
    </>
  );
}