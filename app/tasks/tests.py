from django.test import TestCase, Client
from django.urls import reverse
from app.tasks.models import Task, Status
from app.users.models import Role, User
from datetime import datetime, timedelta


class TaskViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        self.role1 = Role.objects.create(
            name = "1",
            level = 1
        )


        self.role2 = Role.objects.create(
            name = "2",
            level = 2
        )

        # Создание пользователей
        self.user1 = User.objects.create_user(
            email="user1@example.com",
            password="password123",
            first_name="Иван",
            last_name="Иванов",
            surname="Петрович",
            role_id=self.role2.id,
        )
        self.user2 = User.objects.create_user(
            email="user2@example.com",
            password="password123",
            first_name="Петр",
            last_name="Петров",
            surname="Сергеевич",
            role_id=self.role1.id,
        )

        # Создание статусов
        self.status1 = Status.objects.create(name="Не выполнена", level=1)
        self.status2 = Status.objects.create(name="Выполнена", level=4)

        # Авторизация пользователя
        self.client.login(email="user1@example.com", password="password123")

    def test_create_task_for_me(self):
        """Тест создания задачи для себя"""
        url = reverse('tasks:create_task_for_me')
        data = {
            'title': 'Моя задача',
            'description': 'Описание моей задачи',
            'deadline': (datetime.now() + timedelta(days=7)).date(),
            'status': self.status1.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Task.objects.filter(title='Моя задача').exists())

    def test_create_task_for_other(self):
        """Тест создания задачи для другого пользователя"""
        url = reverse('tasks:create_task_for_other', args=[self.user2.slug])
        data = {
            'title': 'Задача для Петра',
            'description': 'Описание задачи для другого пользователя',
            'deadline': (datetime.now() + timedelta(days=7)).date(),
            'status': self.status1.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='Задача для Петра', worker=self.user2).exists())

    def test_task_detail(self):
        """Тест отображения задачи"""
        task = Task.objects.create(
            title="Детальная задача",
            description="Описание задачи",
            deadline=datetime.now() + timedelta(days=5),
            status=self.status1,
            author=self.user1,
            worker=self.user2
        )
        url = reverse('tasks:task_detail', args=[task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task.title)

    # def test_edit_task(self):
    #     """Тест редактирования задачи"""
    #     task = Task.objects.create(
    #         title="Редактируемая задача",
    #         description="Описание задачи",
    #         deadline=datetime.now() + timedelta(days=5),
    #         status=self.status1,
    #         author=self.user1,
    #         worker=self.user2
    #     )
    #     url = reverse('tasks:edit_task', args=[task.id])
    #     data = {
    #         'title': 'Обновленная задача',
    #         'description': 'Обновленное описание',
    #         'deadline': (datetime.now() + timedelta(days=10)).date(),
    #         'status': self.status1.id,
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, 302)
    #     task.refresh_from_db()
    #     self.assertEqual(task.title, 'Обновленная задача')

    def test_delete_task(self):
        """Тест удаления задачи"""
        task = Task.objects.create(
            title="Удаляемая задача",
            description="Описание задачи",
            deadline=datetime.now() + timedelta(days=5),
            status=self.status1,
            author=self.user1,
            worker=self.user2
        )
        url = reverse('tasks:delete_task', args=[task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_complete_task(self):
        """Тест завершения задачи"""
        task = Task.objects.create(
            title="Завершаемая задача",
            description="Описание задачи",
            deadline=datetime.now() + timedelta(days=5),
            status=self.status1,
            author=self.user1,
            worker=self.user2
        )
        url = reverse('tasks:complete_task', args=[task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.status, self.status2)

    def test_user_list_ajax(self):
        """Тест поиска пользователей через AJAX"""
        url = reverse('tasks:user_list')
        response = self.client.get(url, {'q': 'Иван'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user1.first_name)
