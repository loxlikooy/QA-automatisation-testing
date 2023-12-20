import requests


# BDD-like step definitions
class APITestBDDStyle:
    def __init__(self):
        self.api_url = None
        self.response = None

    def given_the_API_endpoint_is_up(self):
        self.api_url = 'https://jsonplaceholder.typicode.com/posts'

    def when_the_client_sends_a_GET_request_to_the_API_endpoint(self):
        self.response = requests.get(self.api_url)

    def then_the_response_status_code_should_be_200(self):
        assert self.response.status_code == 200, "Status code is not 200"

    def then_the_response_should_contain_data(self):
        assert len(self.response.json()) > 0, "Response does not contain data"


# Test runner
def run_tests():
    test = APITestBDDStyle()

    # Run the BDD steps
    test.given_the_API_endpoint_is_up()
    test.when_the_client_sends_a_GET_request_to_the_API_endpoint()
    test.then_the_response_status_code_should_be_200()
    test.then_the_response_should_contain_data()

    print("All tests passed!")


# Execute the test runner
run_tests()
