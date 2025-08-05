from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from .models import Challenge, ChallengeQuota

def get_callenge_quota(db: Session, user_id: str):
    return db.query(ChallengeQuota).filter(ChallengeQuota.user_id == user_id).first()

def create_challenge_quota(db: Session, user_id: str):
    new_quota = ChallengeQuota(user_id=user_id)
    db.add(new_quota)
    db.commit()
    db.refresh(new_quota)
    return new_quota

def reset_quota_if_needed(db: Session, quota: ChallengeQuota):
    now = datetime.now()
    if now - quota.last_reset_date > timedelta(hours=24):
        quota.quota_remaining = 10
        quota.last_reset_date = now
        db.commit()
        db.refresh(quota)
    return quota

def create_challenge(
    db:Session,
    difficulty: str,
    created_by: str,
    title: str,
    options: str,
    correct_answer_id: int,
    explanation: str):
    new_challenge = Challenge(
        difficulty=difficulty,
        created_by=created_by,
        title=title,
        options=options,
        correct_answer_id=correct_answer_id,
        explanation=explanation
    )
    db.add(new_challenge)
    db.commit()
    db.refresh(new_challenge)
    return new_challenge

def get_user_challenges(db: Session, user_id: str):
    return db.query(Challenge).filter(Challenge.created_by == user_id).all()