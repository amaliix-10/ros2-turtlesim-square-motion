]import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TurtleSquarePublisher(Node):
    def __init__(self):
        super().__init__('turtle_square_publisher')
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        self.timer = self.create_timer(1.0, self.move_in_square)
        self.state = 0

    def move_in_square(self):
        msg = Twist()

        if self.state == 0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.get_logger().info(
                'Executing forward movement along square path'
            )
            self.state = 1

        else:
            msg.linear.x = 0.0
            msg.angular.z = math.pi / 2.0
            self.get_logger().info(
                'Executing 90-degree turn for square corner'
            )
            self.state = 0

        self.publisher_.publish(msg)