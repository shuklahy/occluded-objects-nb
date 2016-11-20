'''
    @Author : Hitendra Shukla
    Finding Occluded Objects in Images using Naive Bayes
	
	''Chages
'''


class Image(object):

    def __init__(self, link, objects, no):
        self.link = link
        self.objects = objects #List of Objects
        self.imageNo = no
        self.objNames = []
        for obj in self.objects:
            self.objNames.append(obj[0])


    def printDetails(self):
        print self.imageNo
        print self.link
        print self.objects

    def getTotalObjects(self):
        return len(self.objects)

    def getObjectNames(self):
        return self.objNames

    def contains(self,object):
		return object in self.objNames
		
    def isListContained(self, object):
		for i in object:
			if not(i in self.objNames):
				return False
		return True

def getData(filename):

    #
    # Images consist of objects
    # Objects in turn consists vectors
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
        objects = []
        for i in xrange(imageNoOfObjects):
            objectDetails = fp.readline().split(' ')
            objectName = ' '.join(objectDetails[4:]).rstrip('\n')
            objectVectors = map(int, objectDetails[:4])

            objects.append((objectName, objectVectors))

        img = Image(imageLink, objects, imageNo)
        images.append(img)

    return images

# Calculates conditional probability of word1 given word2
def getProbability(word1, word2):
    imgData = getData('100images.txt')
    word2Cnt = 0
    word1Cnt = 0
    prob = 0
    for i in xrange(len(imgData)):
        img =  imgData[i]
        #print img.link
        if img.isListContained(word2):
            objNames = img.getObjectNames()

            word2Cnt += 1
            if img.contains(word1):
                word1Cnt += 1

    return word1Cnt/float(word2Cnt)


print "PROBABILITY = ",getProbability('tree',['window'])



    # Implementing a Naives Bayes Model to classify data