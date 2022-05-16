import cv2

def main():
    from camera import Camera
    img = Camera().get_frame()
    eyes = Recognizer().detect_eyes(img)
    new_image = Recognizer().draw_rectangle(eyes, img)
    cv2.imshow('winname', new_image)
    cv2.waitKey(0)

class Recognizer:    
    def __init__(self, *args):
        super(Recognizer, self).__init__(*args)
        
    # TO DO: try to generelize it so that it can detect objects in general, not just eyes
    def detect_eyes(self, img, scaleFactor=1.2, minNeighbors=5):
        """detects all eyes in a given image

        Args:
            img (numpy.array): the image you wish to process
            scaleFactor (float, optional): how much the image is resized. higher value means faster detection at the loss of accuracy. Defaults to 1.2
            minNeighbors = (int, optional): how many neighboring squares a square needs to have to be considered. higher value means more accuracy, at the risk of missing some objects. Defaults to 5

        Returns:
            tuple: representing a rectangle around the found eyes. the tuple consists of (x, y, w, h) where x and y are the top left coordinates while w and h are the width and the height of the rectangle
        """
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        
        # scaleFactor: higher value = faster detection at the loss of accuracy. optimal 1.2
        # minNeighbors: higher value = more accuracy, at the risk of missing some eyes. optimal 5
        eyes = eye_cascade.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
        return eyes
    
    # TO DO: seperate adding the rectangle and displaying the image
    def draw_rectangle(self, obj, img, color=(0, 255, 0), thickness=2):
        """adds a rectangle around an object in a given img

        Args:
            obj (tuple or list of tuples): consists of (x, y, w, h) representing x y coordinates, width, and height. can be multiple tuples
            img (numpy.array): the image you wish to add rectangles to
            color (tuple, optional): RGB value representing the color of the rectangole. Defaults to (0, 255, 0) which is green.
            thickness (int, optional): controls how thick the outline is. Defaults to 2.
            
        Returns:
            numpy.array: representing the original image with the added rectangles
        """
        for (x,y,w,h) in obj:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),color,thickness)
            
        return img
        
if __name__ == '__main__':
    main()