import unittest

from models import IrisSpecies
from Model import IrisModel


class TestIrisModel(unittest.TestCase):
   def test_model_initialization(self):
       new_model = IrisModel()
       self.assertIn('iris_model.pkl',new_model.model_fname_)
