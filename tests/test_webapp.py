from src import webapp

def test_button():
	webapp.config['TESTING'] = True
	with webapp.test_client() as test_client:
		response = test_client.post('/', data = {})
		assert b'Hello from James!' in response.data
	print('Test passed!')