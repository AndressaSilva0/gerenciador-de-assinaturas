import __init__
from views.view import SubscriptionService
from models.model import Subscription, Payments
from models.database import engine
from datetime import datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)

    
    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        date_assinatura = datetime.strptime(input('Data de assinatura: '), '%d/%m/%Y')
        valor = Decimal(input('Valor: '))

        subscription = Subscription(empresa=empresa, site=site, date_assinatura=date_assinatura, valor=valor)
        self.subscription_service.create(subscription)
        print('Assinatura adicionada com sucesso.')

    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()

        if not subscriptions:
            print("Não há assinaturas cadastradas.")
            return

            print('Escolha qual assinatura deseja excluir:')

        for sub in subscriptions:
            print(f'[{sub.id}] -> {sub.empresa}')

        try:
            choice = int(input('Digite o ID da assinatura: '))
            # Chamando o método delete que vai excluir a assinatura e os pagamentos associados
            self.subscription_service.delete(choice)
            print('Assinatura e pagamentos excluídos com sucesso.')
            except ValueError:
            print("ID inválido! Digite um número válido.")

    
    def pay(self):
        all_subscriptions = self.subscription_service.list_all()
        
        if not all_subscriptions:
            print("Não há assinaturas cadastradas.")
            return

        print("Assinaturas disponíveis:")
        for sub in all_subscriptions:
            print(f'ID: {sub.id}, Empresa: {sub.empresa}, Valor: {sub.valor:.2f}')

        subscription_id = int(input('Digite o ID da assinatura: '))
        
        subscription = next((sub for sub in all_subscriptions if sub.id == subscription_id), None)
        
        if subscription is None:
            print("Assinatura não encontrada!")
            return

        
        print(f'Assinatura: {subscription.empresa}')
        print(f'Valor: {subscription.valor:.2f}')

        # Solicita o valor do pagamento atual
        payment_value = float(input('Valor do pagamento: '))
        
        # Cria o registro de pagamento atual
        payments = Payments(subscription_id=subscription_id, date=datetime.now(), value=payment_value)
        
        # Processa o pagamento atual
        self.subscription_service.pay(subscription, payments)
    def total_value(self):
        print(f'Seu valor total mensal em assinaturas: {self.subscription_service.total_value()}')

    def start(self):
        while True:
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Pagamento da assinatura
            [6] -> Sair
            ''')

            choice = int(input('Escolha uma opção: '))

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_value()
            elif choice == 4:
                self.subscription_service.gen_chart()
            elif choice == 5:
               self.pay()
                #TODO: Chamar o método pay na interface
            else:
                break



if __name__ == '__main__':
    UI().start()
