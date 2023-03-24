from config import settings

if settings.DEPLOYMENT_ENV == 'local':
    from env.local.storage import LocalFirestore, LocalBucket
    DOC_REF = LocalFirestore()
    bucket = LocalBucket()
else:
    from google.cloud import firestore, storage
    FIRESTORE_CLIENT = firestore.Client()
    DOC_REF = FIRESTORE_CLIENT.collection(
        settings.COLLECTION).document('state')
    bucket = storage.Client().bucket(settings.BUCKET)