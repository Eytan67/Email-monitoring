from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
import uuid


Base = declarative_base()


class Email(Base):
    __tablename__ = 'email'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    suspicious_explosive_contents = relationship('SuspiciousExplosiveContent', back_populates='email1')
    suspicious_hostage_contents = relationship('SuspiciousHostageContent', back_populates='email2')
    location = relationship('Location', back_populates='email', uselist=False)
    device_info = relationship('DeviceInfo', back_populates='email', uselist=False)

def create_email_obj(email_data):
    return Email(
            id=str(uuid.uuid4()),
            email=email_data['email'],
            username=email_data['username'],
            ip_address=email_data['ip_address'],
            created_at=email_data['created_at']
        )

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    email_id = Column(String, ForeignKey('email.id'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    email = relationship('Email', back_populates='location')

def create_location_obj(location_data, email_id):
    return Location(
            email_id=email_id,
            latitude=location_data['latitude'],
            longitude=location_data['longitude'],
            city=location_data ['city'],
            country=location_data['country']
        )

class DeviceInfo(Base):
    __tablename__ = 'device_info'
    id = Column(Integer, primary_key=True)
    email_id = Column(String, ForeignKey('email.id'), nullable=False)
    browser = Column(String, nullable=False)
    os = Column(String, nullable=False)
    device_id = Column(String, nullable=False)

    email = relationship('Email', back_populates='device_info')

def create_device_info_obj(device_data, email_id):
    return DeviceInfo(
            email_id=email_id,
            browser=device_data['browser'],
            os=device_data['os'],
            device_id=device_data['device_id']
        )


class SuspiciousExplosiveContent(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = Column(Integer, primary_key=True)
    email_id = Column(String, ForeignKey('email.id'), nullable=False)
    sentences = Column(Text, nullable=False)

    email1 = relationship('Email', back_populates='suspicious_explosive_contents')

def create_suspicious_explosive_content_obj(sentences = None, email_id = None):
    if sentences is None:
        sentences = None
    return  SuspiciousExplosiveContent(
            email_id=email_id,
            sentences=sentences
        )


class SuspiciousHostageContent(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = Column(Integer, primary_key=True)
    email_id = Column(String, ForeignKey('email.id'), nullable=False)
    sentences = Column(Text, nullable=False)

    email2 = relationship('Email', back_populates='suspicious_hostage_contents')

def create_suspicious_hostage_content_obj(sentences = None, email_id = None):
    if sentences is None:
        sentences = None
    return  SuspiciousHostageContent(
            email_id=email_id,
            sentences=sentences
        )
