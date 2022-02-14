
def copyRecord(self,recordId):
    emailDetail=EmailDetail.objects.get(id=recordId)
    copyEmailDetail= CopyEmailDetail()
    for field in emailDetail.__dict__.keys():
       copyEmailDetail.__dict__[field] = emailDetail.__dict__[field]
    copyEmailDetail.save()
    logger.info("Record Copied %d"%copyEmailDetail.id)