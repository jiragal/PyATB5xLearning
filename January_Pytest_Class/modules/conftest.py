import pytest
@pytest.fixture   #Decorator
def setup():
    print("Launching a Browser.....")  # Executes once before every test
    yield
    print("Closing a Browser.......")  # Executes once after every test


