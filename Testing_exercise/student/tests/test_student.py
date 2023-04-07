from unittest import TestCase
import unittest
from project.student import Student


class StudentTests(TestCase):
    STUDENT_NAME = "Pesho"

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_student_init_without_courses(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init_with_courses(self):
        course = {"P": [1, 2], "Y": [2, 3]}
        student = Student(self.STUDENT_NAME, course)
        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(course, student.courses)

    def test_enroll_student_updates_course_notes_when_course_is_already_enrolled(self):
        course_name = "P"
        course = {course_name: [1, 2], "Y": [2, 3]}
        student = Student(self.STUDENT_NAME, course)
        result = student.enroll(course_name, [5, 7])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual([1, 2, 5, 7], student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_and_notes_when_add_course_notes_have_been_added(self):
        course_name = "P"
        result = self.student.enroll(course_name, [1, 2])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual([1, 2], self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_and_notes_when_add_course_notes_have_been_added_with_Y(self):
        course_name = "P"
        result = self.student.enroll(course_name, [1, 2], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual([1, 2], self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_without_notes(self):
        course_name = "P"
        result = self.student.enroll(course_name, [1, 2], "A")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes_when_course_is_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("asd", "dsa")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertFalse("asd" in self.student.courses)

    def test_add_notes_when_course_is_found(self):
        course = "asd"
        notes = [1, 2]
        extra_notes = [3, 4]
        self.student.courses = {course: notes}
        result = self.student.add_notes(course, extra_notes)
        self.assertEqual("Notes have been updated", result)
        self.assertTrue(extra_notes in self.student.courses[course])

    def test__leave_course_when_course_not_in_courses(self):
        course = "dsa"
        self.student.courses = {"test": "test"}
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test__leave_course_when_course_is_actually_in_courses_happy_case(self):
        course = "asd"
        self.student.courses = {course: "test"}
        result = self.student.leave_course(course)
        self.assertEqual("Course has been removed", result)
        self.assertFalse(course in self.student.courses)

