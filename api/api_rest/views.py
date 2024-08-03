from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date

from .models import Pessoas
from .serializers import PessoasSerializer


from django.db import connection

import json

@api_view(['GET'])
def selecionar_tudo(request):
    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                cursor.callproc('selecionar_tudo')
                resultados = cursor.fetchall()
                
                pessoasList = []
                for resultado in resultados:
                    pessoa={
                        "id_pessoa": resultado[0],
                        "nome": resultado[1],
                        "data_nascimento": resultado[2].strftime("%Y-%m-%d") if isinstance(resultado[2], date) else resultado[2],
                        "salario": float(resultado[3]),
                        "observacoes": resultado[4],
                        "nome_mae": resultado[5],
                        "nome_pai": resultado[6],
                        "cpf": resultado[7]
                    }
                    pessoasList.append(pessoa)
                serializer = PessoasSerializer(pessoasList, many=True)
                return Response(serializer.data)
                
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_400_BAD_REQUEST)
