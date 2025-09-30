from django.test import TestCase

class TestSimples(TestCase):
    def test_soma_basica(self):
        """ Um teste muito simples para garantir que o Pytest está funcionando. """
        self.assertEqual(2 + 2, 4)