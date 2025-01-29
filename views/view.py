import __init__
from models.database import engine
from sqlmodel import Session, select
from models.model import Subscription, Payments
from datetime import date, datetime

class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            session.refresh(subscription)
            return subscription

    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
            return results

    def delete(self, id):
        with Session(self.engine) as session:
            # Buscando a assinatura
            subscription_statement = select(Subscription).where(Subscription.id == id)
            subscription = session.exec(subscription_statement).one_or_none()

            if subscription is None:
                print("Assinatura não encontrada!")
                return

            # Excluindo os pagamentos associados a essa assinatura
            payments_statement = select(Payments).where(Payments.subscription_id == id)
            payments = session.exec(payments_statement).all()

            if payments:
                for payment in payments:
                    print(f"Excluindo pagamento da assinatura {subscription.empresa}")
                    session.delete(payment)

            # Excluindo a assinatura
            session.delete(subscription)

            # Comitando as alterações no banco de dados
            session.commit()
            print("Assinatura e seus pagamentos foram excluídos com sucesso.")




    def _has_pay(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False

    def pay(self, subscription: Subscription, payments: Payments):
        with Session(self.engine) as session:
            statement = (
                select(Payments)
                .join(Subscription, Subscription.id == Payments.subscription_id)
                .where(Subscription.empresa == subscription.empresa)
            )
            results = session.exec(statement).all()

            if self._has_pay(results):
                question = input('Essa conta já foi paga esse mês, deseja pagar novamente? Y ou N: ')
                if not question.upper() == 'Y':
                    return
            
            # Agora, usa `payments` passado como argumento
            payments.subscription_id = subscription.id  
            session.add(payments)
            session.commit()


    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement).all()
        total = 0
        for result in results:
            total += result.valor
        return float(total)

    def _get_last_12_months_native(self):
        today = datetime.now()
        year = today.year
        month = today.month
        last_12_months = []
        for _ in range(12):
            last_12_months.append((month, year))
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        return last_12_months[::-1]

    def _get_values_for_months(self, last_12_months):
        with Session(self.engine) as session:
            statement = select(Payments)
            results = session.exec(statement).all()

            value_for_months = []
            for i in last_12_months:
                value = 0
                for result in results:
                    if result.date.month == i[0] and result.date.year == i[1]:
                        value += float(result.subscription.valor)
                value_for_months.append(value)
        return value_for_months

    def gen_chart(self):
        last_12_months = self._get_last_12_months_native()
        values_for_months = self._get_values_for_months(last_12_months)
        months = list(map(lambda x: x[0], last_12_months))

        import matplotlib.pyplot as plt
        plt.plot(months, values_for_months)
        plt.show()

ss = SubscriptionService(engine)
# subscription = Subscription(empresa='Netflix', site="netflix.com.br", date_assinatura=date.today(), valor=25)
# print(ss.gen_chart)
