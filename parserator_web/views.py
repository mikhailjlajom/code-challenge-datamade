import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    # visited following websites to learn more about python
    # https://www.django-rest-framework.org/api-guide/exceptions/
    # https://www.django-rest-framework.org/api-guide/responses/
    # https://www.w3schools.com/python/python_conditions.asp
    # https://www.programiz.com/python-programming/function

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.

        try:
            input_string = request.data
            address_components, address_type = self.parse(input_string)

            if(address_components is None) or (address_type is None):
                return None
            else:
                details = (input_string, address_components, address_type)

        except ParseError:
            print("Request contains malformed data")
        return Response(details)

        # never learned python yet so had to do research about all of it
        # https://usaddress.readthedocs.io/en/latest/

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress

        try:
            address_components, address_type = usaddress.tag(address)
        
        except usaddress.RepeatedLabelError as e :
            print(e.original_string, "An exception occurred")
            return None

        return address_components, address_type
