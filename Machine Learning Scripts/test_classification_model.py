import unittest
from classification_model import model

class TestClassificationModel(unittest.TestCase):
    def test_model_accuracy(self):
        # Mock input data for testing
        test_data = [[1, 80, 2, 3]]  # Replace with actual data format
        prediction = model.predict(test_data)
        self.assertTrue(prediction in [1, 2])

if __name__ == "__main__":
    unittest.main()