from rest_framework import serializers
from mysites.models import TCommissionDetail

# class SnippetSerializer(serializers.Serializer):
#     kael_id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(required=False,allow_blank=False,max_length=100)
#     created_time=serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Kael.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.kael_id=validated_data.get('kael_id',instance.kael_id)
#         instance.name=validated_data.get('name',instance.name)
#         instance.created_time=validated_data.get('created_time',instance.created_time)


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=TCommissionDetail
        # fields=('id','creditor_id','org_id','settle_month','sum_amout','refund_principal','refund_interest','refund_compensation','refund_poundage','refund_poundage_compensation','principal_commission','interest_commission','compensation_commission','poundage_commission','poundage_compensation_commission','min_overdue_day','max_overdue_day','status','create_time')
        fields='__all__'