from sqlalchemy.orm import Session
from loguru import logger

from db.models.example import Example
from schemas.example import CreateExampleRequest, UpdateExampleRequest


# NOTE: This was generated using AI but simply serves as a template for future code.


class ExampleService:
    """Service layer for Example entity database operations."""

    @staticmethod
    def create(db: Session, data: CreateExampleRequest):
        """
        Create a new Example record.

        :param db: SQLAlchemy session
        :param data: validated input data
        :return: created Example instance
        """
        logger.info(f"Creating Example: {data.model_dump()}")

        obj = Example(name=data.name)
        db.add(obj)
        db.commit()
        db.refresh(obj)

        logger.info(f"Created Example with id={obj.id}")
        return obj

    @staticmethod
    def get(db: Session, obj_id: int):
        """
        Retrieve a single Example by ID.

        :param db: SQLAlchemy session
        :param obj_id: Example ID
        :return: Example instance or None
        """
        logger.info(f"Fetching Example id={obj_id}")

        obj = db.query(Example).filter(Example.id == obj_id).first()

        if not obj:
            logger.warning(f"Example not found id={obj_id}")

        return obj

    @staticmethod
    def get_all(db: Session):
        """
        Retrieve all Example records.

        :param db: SQLAlchemy session
        :return: list of Example instances
        """
        logger.info("Fetching all Examples")

        return db.query(Example).all()

    @staticmethod
    def update(db: Session, obj_id: int, data: UpdateExampleRequest):
        """
        Update an existing Example record.

        :param db: SQLAlchemy session
        :param obj_id: Example ID
        :param data: fields to update
        :return: updated Example instance or None
        """
        logger.info(f"Updating Example id={obj_id} with {data.model_dump(exclude_none=True)}")

        obj = ExampleService.get(db, obj_id)
        if not obj:
            return None

        if data.name is not None:
            obj.name = data.name

        db.commit()
        db.refresh(obj)

        logger.info(f"Updated Example id={obj_id}")
        return obj

    @staticmethod
    def delete(db: Session, obj_id: int):
        """
        Delete an Example record.

        :param db: SQLAlchemy session
        :param obj_id: Example ID
        :return: True if deleted, False if not found
        """
        logger.info(f"Deleting Example id={obj_id}")

        obj = ExampleService.get(db, obj_id)
        if not obj:
            logger.warning(f"Delete failed, Example not found id={obj_id}")
            return False

        db.delete(obj)
        db.commit()

        logger.info(f"Deleted Example id={obj_id}")
        return True
