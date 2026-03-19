from file_manger import FileManager
from exceptions.file_exceptions import (
    ValidationError,
    DuplicateEntryError,
)

if __name__ == "__main__":
    import sys

    print("=" * 70)
    print("FileManager - Comprehensive Error Handling Test")
    print("=" * 70)

    try:
        # Test 1: Initialize files
        print("\n[TEST 1] Initializing files...")
        FileManager.initialize_files()
        print("✓ Files initialized successfully")

        # Test 2: Add valid admin user
        print("\n[TEST 2] Adding valid admin user...")
        FileManager.add_user("mr_teacher", "securepass123", "admin")
        print("✓ Admin user added successfully")

        # Test 3: Add valid student
        print("\n[TEST 3] Adding valid student...")
        FileManager.add_user("john_doe", "student123", "student")
        print("✓ Student user added successfully")

        # Test 4: Attempt duplicate username (should fail)
        print("\n[TEST 4] Attempting to add duplicate username...")
        try:
            FileManager.add_user("john_doe", "password", "student")
            print("✗ Should have raised DuplicateEntryError")
        except DuplicateEntryError as e:
            print(f"✓ Correctly rejected duplicate: {e}")

        # Test 5: Invalid username (should fail)
        print("\n[TEST 5] Attempting invalid username with comma...")
        try:
            FileManager.add_user("bad,user", "password123", "student")
            print("✗ Should have raised ValidationError")
        except ValidationError as e:
            print(f"✓ Correctly rejected invalid username: {e}")

        # Test 6: Invalid password (too short)
        print("\n[TEST 6] Attempting short password...")
        try:
            FileManager.add_user("newuser", "123", "student")
            print("✗ Should have raised ValidationError")
        except ValidationError as e:
            print(f"✓ Correctly rejected short password: {e}")

        # Test 7: Invalid role
        print("\n[TEST 7] Attempting invalid role...")
        try:
            FileManager.add_user("baduser", "password123", "superadmin")
            print("✗ Should have raised ValidationError")
        except ValidationError as e:
            print(f"✓ Correctly rejected invalid role: {e}")

        # Test 8: Add valid MCQ question
        print("\n[TEST 8] Adding valid MCQ question...")
        FileManager.add_question(
            "mcq",
            "What is the capital of France?",
            "Paris|London|Berlin|Madrid",
            "Paris",
            1,
        )
        print("✓ MCQ question added successfully")

        # Test 9: Add valid True/False question
        print("\n[TEST 9] Adding valid True/False question...")
        FileManager.add_question("tf", "Python is a compiled language.", "", "False", 2)
        print("✓ True/False question added successfully")

        # Test 10: Invalid MCQ (answer not in options)
        print("\n[TEST 10] Attempting MCQ with invalid answer...")
        try:
            FileManager.add_question(
                "mcq", "Invalid question?", "A|B|C", "D", 1  # Not in options
            )
            print("✗ Should have raised ValidationError")
        except ValidationError as e:
            print(f"✓ Correctly rejected invalid MCQ: {e}")

        # Test 11: Invalid difficulty
        print("\n[TEST 11] Attempting question with invalid difficulty...")
        try:
            FileManager.add_question(
                "mcq", "Test question?", "A|B|C", "A", 10  # Out of range
            )
            print("✗ Should have raised ValidationError")
        except ValidationError as e:
            print(f"✓ Correctly rejected invalid difficulty: {e}")

        # Test 12: Save quiz result
        print("\n[TEST 12] Saving quiz result...")
        FileManager.save_quiz_result(2, 8, 10)
        print("✓ Quiz result saved successfully")

        # Test 13: Invalid quiz result (score > total)
        print("\n[TEST 13] Attempting invalid quiz result...")
        try:
            FileManager.save_quiz_result(2, 15, 10)
            print("✗ Should have raised ValidationError")
        except ValidationError as e:
            print(f"✓ Correctly rejected invalid result: {e}")

        # Test 14: Read and display users
        print("\n[TEST 14] Reading users...")
        users = FileManager.read_csv(FileManager.USERS_FILE)
        print(f"✓ Found {len(users)} users:")
        for user in users:
            print(f"  - {user['username']} ({user['role']})")

        # Test 15: Read and display questions
        print("\n[TEST 15] Reading questions...")
        questions = FileManager.read_csv(FileManager.QUESTIONS_FILE)
        print(f"✓ Found {len(questions)} questions:")
        for q in questions:
            print(f"  - [{q['type'].upper()}] {q['text'][:50]}...")

        # Test 16: Find user
        print("\n[TEST 16] Finding user...")
        user = FileManager.find_user("john_doe")
        if user:
            print(f"✓ Found user: {user['username']}")
        else:
            print("✗ User not found")

        # Test 17: Get questions by type
        print("\n[TEST 17] Getting MCQ questions...")
        mcq_questions = FileManager.get_questions_by_type("mcq")
        print(f"✓ Found {len(mcq_questions)} MCQ questions")

        # Test 18: Get student results
        print("\n[TEST 18] Getting student results...")
        results = FileManager.get_student_results(2)
        print(f"✓ Found {len(results)} results for student 2")

        print("\n" + "=" * 70)
        print("All tests completed successfully!")
        print("=" * 70)

    except Exception as e:
        print(f"\n✗ FATAL ERROR: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
