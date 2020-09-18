# Pilha e Fila
Criar lista e fila com o Python sem utilizar as bibliotecas built-in da linguagem.

## Como foi feito
Foram criadas duas classes principais Stack e Queue, cujos métodos foram criados segundo os testes em tests.py. Ambas as classes foram criadas seguindo a ideia de "linked lists" e utilizam uma terceira classe chamada Node para alimentar novos itens dentro dos nós.

Os métodos das duas classes são iguais, exceto pelos métodos de adicionar itens em cada uma -- push em Stack e enqueue em Queue. No caso do stack.push() o método verifica se há itens. Caso positivo, o novo item aponta para o primeiro (que se torna o segundo), e o novo passa a ser o primeiro da pilha.
Já no caso do queue.enqueue(), se houver itens previamente, eles são colocados ao fim da lista.

Além disso, também foram criadas classes de exceção para quando se tenta retirar itens da pilha e da fila e não há itens para serem retirados.

## Observações
Havia alguns erros nos testes automatizados, que foram modificados.

i.e.:
```
stack.is_empty() == 1
```

## Requisitos
- Python 3.6+
Sem libs externas

## Como rodar os testes
```
python3 -m unittest tests.py
```

## That's all, follks