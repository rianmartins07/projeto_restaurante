def get_columns():
    item_columns = [
        'ID PEDIDO',
        'NOME PEDIDO',
        'VALOR PEDIDO',
        'ID MESA',
        'Nº MESA'
        'NOME RESPONSÁVEL',
    ]
    
    return item_columns

def get_itens(queryset):
    
    for i in queryset:
        item_fields = [
            i.id,
            i.nome,
            i.valor,
            i.table_id,
            i.table_number,
            i.responsible_name,
        ]
        
        
    yield item_fields
    