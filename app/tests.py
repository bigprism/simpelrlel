from django.test import TestCase

from .models import Task



class TaskCreateTestCase(TestCase):
    def test_task_create(self):
        task = Task.objects.create(title="Test Task", description="This is a test task.")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")



class TaskReadTestCase(TestCase):
    def test_task_read(self):
        task = Task.objects.create(title="Test Task", description="This is a test task.")
        task_from_db = Task.objects.get(pk=task.id)
        self.assertEqual(task_from_db.title, "Test Task")
        self.assertEqual(task_from_db.description, "This is a test task.")



class TaskUpdateTestCase(TestCase):
    def test_task_update(self):
        task = Task.objects.create(title="Test Task", description="This is a test task.")
        task.title = "Updated Test Task"
        task.description = "This is an updated test task."
        task.save()
        task_from_db = Task.objects.get(pk=task.id)
        self.assertEqual(task_from_db.title, "Updated Test Task")
        self.assertEqual(task_from_db.description, "This is an updated test task.")



class TaskDeleteTestCase(TestCase):
    def test_task_delete(self):
        task = Task.objects.create(title="Test Task", description="This is a test task.")
        task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=task.id)