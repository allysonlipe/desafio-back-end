from rest_framework import serializers
from .models import Pessoas

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = '__all__'
    #     extra_kwargs = {
    # 'cpf': {'validators': []}  # Desativa a validação única se não for necessário
#}
