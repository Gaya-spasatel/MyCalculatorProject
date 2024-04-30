from rest_framework import serializers

class IntegerNumberSerializer(serializers.Serializer):
    value = serializers.IntegerField()

class IntegerOperandsSerializer(serializers.Serializer):
    firstOperand = IntegerNumberSerializer()
    secondOperand = IntegerNumberSerializer()


class SumOfIntegerNumbersSerializer(serializers.Serializer):
    sum = IntegerNumberSerializer()

class DiffOfIntegerNumbersSerializer(serializers.Serializer):
    difference = IntegerNumberSerializer()

class MulOfIntegerNumbersSerializer(serializers.Serializer):
    product = IntegerNumberSerializer()

class DivOfIntegerNumbersSerializer(serializers.Serializer):
    quotient = IntegerNumberSerializer()
    remainder = IntegerNumberSerializer()

class ErrorMessageSerializer(serializers.Serializer):
    type = serializers.CharField()
    message = serializers.CharField()


