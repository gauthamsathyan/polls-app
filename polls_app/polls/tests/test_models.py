from django.test import TestCase
from models import Poll, Option
from django.utils import timezone

class PollModelTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(question="What's new?", pub_date=timezone.now())

    def test_question_label(self):
        poll = Poll.objects.get(id=1)
        field_label = poll._meta.get_field('question').verbose_name
        self.assertEqual(field_label, 'question')

    def test_question_max_length(self):
        poll = Poll.objects.get(id=1)
        max_length = poll._meta.get_field('question').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_question(self):
        poll = Poll.objects.get(id=1)
        expected_object_name = poll.question
        self.assertEqual(str(poll), expected_object_name)

class OptionModelTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(question="What's new?", pub_date=timezone.now())
        self.option = Option.objects.create(poll=self.poll, option_text="Nothing much", votes=0)

    def test_option_text_label(self):
        option = Option.objects.get(id=1)
        field_label = option._meta.get_field('option_text').verbose_name
        self.assertEqual(field_label, 'option text')

    def test_option_text_max_length(self):
        option = Option.objects.get(id=1)
        max_length = option._meta.get_field('option_text').max_length
        self.assertEqual(max_length, 20)

    def test_object_name_is_option_text(self):
        option = Option.objects.get(id=1)
        expected_object_name = option.option_text
        self.assertEqual(str(option), expected_object_name)
