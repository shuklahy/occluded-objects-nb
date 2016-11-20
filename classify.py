'''
    @Author : Hitendra Shukla
    Finding Occluded Objects in Images usign Naive Bayes

    Note:

'''


class Image(object):

    def __init__(self, link, objects, no):
        self.link = link
        self.objects = objects #List of Objects
        self.imageNo = no

    def printDetails(self):
        print self.imageNo
        print self.link
        print self.objects

    def getTotalObjects(self):
        return len(self.objects)

def getData(filename):

    #
    # Images consist of objects
    # Objects in turn consists vectors of words
    #
    # Data    = List of Images
    # Images  = List of img Objects
    # Objects = list of object tuple
    # object  = (objectName, listofObject Vectors)

    fp = open(filename, 'r')
    images = []
    objects = []

    while True:
        no = fp.readline()
        # Very inefficient way to check EOF but should work
        if no == '':
            break
        imageNo = int(no)
        imageLink = fp.readline()
        imageNoOfObjects = int(fp.readline())

        for i in xrange(imageNoOfObjects):
            objectDetails = fp.readline().split(' ')
            objectName = ' '.join(objectDetails[4:]).rstrip('\n')
            objectVectors = map(int, objectDetails[:4])

            objects.append((objectName, objectVectors))

        img = Image(imageLink, objects, imageNo)
        images.append(img)

    return images

images = getData('100images.txt')
print len(images)


# Implementing a Naives Bayes Model to classify data