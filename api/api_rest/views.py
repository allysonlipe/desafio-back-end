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
                print(serializer.data)
                return Response(serializer.data)
                
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def selecionar_pessoa(request, id):
    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                cursor.callproc('selecionar_pessoa',[id])
                resultados = cursor.fetchall()
                
                if not resultados:
                    return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
                
                pessoaJson = []
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
                    pessoaJson.append(pessoa)
                serializer = PessoasSerializer(pessoaJson, many=True)
                print(serializer.data)
                return Response(serializer.data)              
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def inserir_pessoa(request):
    if request.method == 'POST':
        try:
            data = request.data
            nome = data.get('nome')
            data_nascimento = data.get('data_nascimento')
            salario = data.get('salario')
            observacoes = data.get('observacoes')
            nome_mae = data.get('nome_mae')
            nome_pai = data.get('nome_pai')
            cpf = data.get('cpf')    
            with connection.cursor() as cursor:
                cursor.callproc('inserir_pessoa', [nome, data_nascimento, salario, observacoes, nome_mae, nome_pai, cpf, 0])
                resultado = cursor.fetchone()
                id_pessoa = resultado[0] if resultado else None
                if id_pessoa:
                    print("id_pessoa: " + str(id_pessoa))
                    return Response({"id_pessoa": id_pessoa}, status=status.HTTP_201_CREATED)

        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_pessoa(request):
    if request.method == 'PUT':
        try:
            data = request.data
            id = data.get('id')
            nome = data.get('nome')
            data_nascimento = data.get('data_nascimento')
            salario = data.get('salario')
            observacoes = data.get('observacoes')
            nome_mae = data.get('nome_mae')
            nome_pai = data.get('nome_pai')
            cpf = data.get('cpf')
            with connection.cursor() as cursor:
                cursor.callproc('atualizar_pessoa', [id, nome, data_nascimento, salario, observacoes, nome_mae, nome_pai, cpf])
                resultado = cursor.fetchone()

                if resultado and resultado[0] == 'OK':
                    print(resultado[0])
                    return Response({"status": resultado[0]}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Falha ao atualizar pessoa"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        except Exception as e:
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_pessoa(request, id):
    if request.method == 'DELETE':
        try:
            with connection.cursor() as cursor:
                cursor.callproc('deletar_pessoa',[id])
                resultado = cursor.fetchone()

                if resultado and resultado[0] == 'OK':
                    print(resultado[0])
                    return Response({"status": resultado[0]}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Falha ao deletar pessoa"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        except Exception as e:
                    return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_400_BAD_REQUEST)