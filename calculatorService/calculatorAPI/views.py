from .models import IntegerNumber, SumOfIntegerNumbers, DiffOfIntegerNumbers, DivOfIntegerNumbers, MulOfIntegerNumbers, ErrorMessage
from .serializers import IntegerOperandsSerializer, SumOfIntegerNumbersSerializer, DiffOfIntegerNumbersSerializer, DivOfIntegerNumbersSerializer, MulOfIntegerNumbersSerializer, ErrorMessageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from calculatorModule import sumOperation, diffOperation, mulOperation, divOperation

class SumOperationView(APIView):

    def post(self, request):
        serializer = IntegerOperandsSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            operands = serializer.data
            try:
                sum = sumOperation(operands['firstOperand']['value'], operands['secondOperand']['value'])
                sumOfIntegerNumbers = SumOfIntegerNumbers(IntegerNumber(sum))
                serializer_response = SumOfIntegerNumbersSerializer(instance=sumOfIntegerNumbers)
                return Response(serializer_response.data)
            except ArithmeticError or MemoryError:
                serializerError = ErrorMessageSerializer(instance=ErrorMessage("calculation error", "Error while calculation"))
                return Response(serializerError.data, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            serializerError = ErrorMessageSerializer(instance=ErrorMessage("input data error", "Vatidation input data error. Please check your input data"))
            return Response(serializerError.data, status=status.HTTP_406_NOT_ACCEPTABLE)
            
class DiffOperationView(APIView):
    def post(self, request):
        serializer = IntegerOperandsSerializer(data=request.data)
        if serializer.is_valid():
            operands = serializer.data
            try:
                diff = diffOperation(operands['firstOperand']['value'], operands['secondOperand']['value'])
                diffOfIntegerNumbers = DiffOfIntegerNumbers(IntegerNumber(diff))
                serializer_response = DiffOfIntegerNumbersSerializer(instance=diffOfIntegerNumbers)
                return Response(serializer_response.data)
            except ArithmeticError or MemoryError:
                serializerError = ErrorMessageSerializer(instance=ErrorMessage("calculation error", "Error while calculation"))
                return Response(serializerError.data, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            serializerError = ErrorMessageSerializer(instance=ErrorMessage("input data error", "Vatidation input data error. Please check your input data"))
            return Response(serializerError.data, status=status.HTTP_406_NOT_ACCEPTABLE)
            

class MulOperationView(APIView):
    def post(self, request):
        serializer = IntegerOperandsSerializer(data=request.data)
        if serializer.is_valid():
            operands = serializer.data
            try:
                mul = mulOperation(operands['firstOperand']['value'], operands['secondOperand']['value'])
                mulOfIntegerNumbers = MulOfIntegerNumbers(IntegerNumber(mul))
                serializer_response = MulOfIntegerNumbersSerializer(instance=mulOfIntegerNumbers)
                return Response(serializer_response.data)

            except ArithmeticError or MemoryError:
                serializerError = ErrorMessageSerializer(instance=ErrorMessage("calculation error", "Error while calculation"))
                return Response(serializerError.data, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            serializerError = ErrorMessageSerializer(instance=ErrorMessage("input data error", "Vatidation input data error. Please check your input data"))
            return Response(serializerError.data, status=status.HTTP_406_NOT_ACCEPTABLE)

class DivOperationView(APIView):
    def post(self, request):
        serializer = IntegerOperandsSerializer(data=request.data)
        if serializer.is_valid():
            operands = serializer.data
            try:
                quotient, remainder = divOperation(operands['firstOperand']['value'], operands['secondOperand']['value'])
                divOfIntegerNumbers = DivOfIntegerNumbers(IntegerNumber(quotient), IntegerNumber(remainder))
                serializer_response = DivOfIntegerNumbersSerializer(instance=divOfIntegerNumbers)
                return Response(serializer_response.data)
                
            except ArithmeticError or MemoryError:
                serializerError = ErrorMessageSerializer(instance=ErrorMessage("calculation error", "Error while calculation"))
                return Response(serializerError.data, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            serializerError = ErrorMessageSerializer(instance=ErrorMessage("input data error", "Vatidation input data error. Please check your input data"))
            return Response(serializerError.data, status=status.HTTP_406_NOT_ACCEPTABLE)