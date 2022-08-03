import nep
import time

node = nep.node('python_sender')
pub = node.new_pub('/blackboard','json')

# Dummy perceptual function
def isHeadTouched():
	return True

#  Publish the current state when 
while True:
    # Here your code that recognize something
    # Example: 
    head_touched = isHeadTouched()
    if head_touched:
        msg = {'primitive':'touched', 'input':{"head":1}, "robot":"ROS"}	
        pub.publish(msg)
        print("perception send")
    time.sleep(10)