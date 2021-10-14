from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from task.models import Task
from rest_framework.test import APITestCase


class CreateTaskTest(APITestCase):
    """
    Test create a task
    """
    def test_can_create_task(self):
        """
        Test create a task successfully and response the instance
        """
        data = {'name': 'name1'}
        expect = {'name': 'name1', 'status': 0, 'id': 1}
        response = self.client.post(reverse('task-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expect)

    def test_cannot_create_task(self):
        """
        Test failed to create task
        """
        data = {'name': ''}
        response = self.client.post(reverse('task-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReadTaskTest(TestCase):
    """
    Test read tasks
    """
    def setUp(self):
        """
        Create 2 tasks, define expect value, get the response
        """
        Task.objects.create(name='name1')
        Task.objects.create(name='name2')
        self.expect = [{'name': 'name1', 'status': 0, 'id': 1}, {'name': 'name2', 'status': 0, 'id': 2}]
        self.response = self.client.get(reverse('tasks'))

    def test_can_read_tasks(self):
        """
        Test can get the task list
        """
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data, self.expect)


class UpdateTaskTest(TestCase):
    """
    Test update a task
    """
    def setUp(self):
        """
        Create 3 task, define their expect, get their response
        """
        # 1: change name
        Task.objects.create(name='name1')
        change_task1 = '{"name": "newname1", "status": 0, "id": 1}'
        self.expect1 = {"name": "newname1", "status": 0, "id": 1}
        self.response1 = self.client.put(
            reverse('task', kwargs={'pk': 1}),
            change_task1, format='json'
        )
        # 2: change status
        Task.objects.create(name='name2')
        change_task2 = '{"name": "name2", "status": 1, "id": 2}'
        self.expect2 = {"name": "name2", "status": 1, "id": 2}
        self.response2 = self.client.put(
            reverse('task', kwargs={'pk': 2}),
            change_task2, format='json'
        )
        # 3: status type and value not match
        Task.objects.create(name='name3')
        change_task3 = '{"name": "newname3", "status": 3, "id": 3}'
        self.response3 = self.client.put(
            reverse('task', kwargs={'pk': 3}),
            change_task3, format='json'
        )

    def test_can_update_task(self):
        """
        Test can update a task
        """
        # 1
        self.assertEqual(self.response1.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response1.data, self.expect1)
        # 2
        self.assertEqual(self.response2.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response2.data, self.expect2)

    def test_cannot_update_task(self):
        """
        Test failed to update a task
        """
        self.assertEqual(self.response3.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteTaskTest(TestCase):
    """
    Test delete a task
    """
    def setUp(self):
        """
        Create a task and get the response
        """
        Task.objects.create(name='name1')
        self.response = self.client.delete(
            reverse('task', kwargs={'pk': 1})
        )

    def test_can_delete_task(self):
        """
        Test can delete a task
        """
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
