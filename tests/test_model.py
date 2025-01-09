from app.models import User, ImageAnalysis, SessionLocal

def test_create_user():
    session = SessionLocal()
    new_user = User(username="testuser_db", password_hash="hashed_password")
    session.add(new_user)
    session.commit()

    user = session.query(User).filter(User.username == "testuser_db").first()
    assert user is not None
    assert user.username == "testuser_db"

def test_create_analysis():
    session = SessionLocal()
    new_analysis = ImageAnalysis(user_id=1, image_name="test.jpg", objects_detected="car, tree", summary="Detected a car and a tree")
    session.add(new_analysis)
    session.commit()

    analysis = session.query(ImageAnalysis).filter(ImageAnalysis.image_name == "test.jpg").first()
    assert analysis is not None
    assert "car" in analysis.objects_detected
