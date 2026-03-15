from loguru import logger

class DatabaseConnectionError(Exception):
    pass

def db_connect():
    logger.info("Connecting to database...")
    raise ConnectionError("Database not reachable")

class RepositoryError(Exception):
    pass
def fetch_user_from_db(user_id):
    try:
        db_connect()
        return {"id": user_id, "name": "Bikram"}
    except ConnectionError as e:
        logger.exception("Database connection failed in repository layer")
        raise RepositoryError("Failed to fetch user from database") from e

class ServiceError(Exception):
    pass


def get_user_profile(user_id):
    try:
        user = fetch_user_from_db(user_id)
        return user
    
    except RepositoryError as e:
        logger.exception("Service layer could not retrieve user")
        raise ServiceError("User profile retrieval failed") from e

def handle_request(user_id):
    try:
        profile = get_user_profile(user_id)
        logger.info(f"User profile: {profile}")
    
    except ServiceError:
        logger.exception("Request failed at controller level")
        print("Returning HTTP 500 to client")

handle_request(101)
   