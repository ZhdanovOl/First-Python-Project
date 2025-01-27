"""
This module contains unit tests for the emotion detection functionality.
The tests validate that the emotion detector correctly identifies the dominant emotion
from given text inputs.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Unit test class for testing the emotion_detector function.
    """

    def test_emotion_detector(self):
        """
        Tests the emotion_detector function for various inputs to ensure it
        correctly identifies the dominant emotion.
        """
        # Test case for joy as a dominant emotion
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for anger as a dominant emotion
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for disgust as a dominant emotion
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case for sadness as a dominant emotion
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case for fear as a dominant emotion
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
