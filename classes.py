import json
import os
import requests
from abc import ABC, abstractmethod


class Job(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJobAPI(Job):
    """
    Класс для получения вакансий с SuperJob
    """
    def __init__(self, town, search_query):
        """

        :param town: город пользователя
        :param search_query: поисковой запрос пользователя
        """
        self.town = town
        self.search_query = search_query

    def get_vacancies(self):
        """
        Метод для получения вакансий в формате JSON
        """
        sj_api_key: str = os.getenv('API_KEY_SJ')
        base_url = 'https://api.superjob.ru/2.0/'
        endpoint = 'vacancies'
        headers = {'X-Api-App-Id': sj_api_key}
        params = {
            # 'town': self.town,
            # 'keyword': self.search_query,
            'town': "Москва",
            'keyword': "Python",
            # 'experience': 'no_experience',  # Опыт работы (no_experience, between1And3, moreThan6)
        }
        response = requests.get(f'{base_url}{endpoint}', headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            vacancies = data['objects']
            for prof in vacancies:
                payment_from = prof['payment_from']
                payment_to = prof['payment_to']
                profession = prof['profession']
                education = prof['education']['title']
                experience = prof['experience']['title']
                town = prof['town']['title']
                link = prof['link']


                print(profession)
                if payment_to == 0:
                    print(f"от {payment_from}")
                else:
                    print(f"от {payment_from} до {payment_to}")
                print(education)
                print(experience)
                print(town)
                print(f"{link}\n")


                # break
                # print(profession['profession'])

            # print(vacancies)
            # print(type(data))

        else:
            print('Ошибка при запросе данных:', response.status_code)


class HeadHunterAPI(ABC):
    """
    Класс для получения вакансий с HeadHunter
    """

    def __init__(self, town, search_query):
        """

         :param town: город пользователя
         :param search_query: поисковой запрос пользователя
         """
        self.town = town
        self.search_query = search_query

    def get_vacancies(self):
        """
        Метод для получения вакансий по api
        в формате JSON
        """
        hh_api_key: str = os.getenv('API_KEY_HH')

        base_url = 'https://api.hh.ru/'
        endpoint = 'vacancies'
        headers = {'X-Api-App-Id': hh_api_key}
        params = {
            'town': 'Москва',
            'keyword': 'Python разработчик',
            'experience': 'no_experience',  # Опыт работы (no_experience, between1And3, moreThan6)
        }
        response = requests.get(f'{base_url}{endpoint}')

        if response.status_code == 200:
            data = response.json()
            # vacancies = data['objects']
            print(data)
            # Здесь вы можете обработать список вакансий
        else:
            print('Ошибка при запросе данных:', response.status_code)

# """
# HEADHUNTER
# """
#
#
# hh_api_key: str = os.getenv('API_KEY_HH')
#
# head_hunter = build('youtube', 'v3', developerKey=hh_api_key)
#
# print(super_job)