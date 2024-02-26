def padroniza_codigo(cod_produto, padrão='m'):
    for i, item in enumerate(cod_produto):
        item = item.replace('  ',' ' )
        item = item.strip()
        if padrão == 'm':
            item = item.casefold()
        elif padrão =='M':
            item = item.upper()
        cod_produto[i] = item
    return cod_produto

cod_produtos = [' ABC12 ', 'abc34', 'AbC37']

print(f'{cod_produtos} ---- {padroniza_codigo(cod_produtos, 'M')}')