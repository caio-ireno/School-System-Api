import requests
import unittest

class TestStringMethods(unittest.TestCase):

    def test_000_alunos_retorna_lista(self):
        print("Iniciando o teste...")
        r = requests.get('http://192.168.147:8000/alunos')
        
        if r.status_code == 404:
            self.fail("Você não definiu a página /alunos no seu servidor")
        
        try:
            obj_retornado = r.json()
            print(f"Resposta recebida: {obj_retornado}")  # Exibe o retorno para depuração
        except:
            self.fail("Queríamos um JSON mas você retornou outra coisa")
        
        self.assertEqual(type(obj_retornado), type([]))
        print("Teste concluído com sucesso!")
